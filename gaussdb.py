# -*- coding: utf-8 -*-
# File : gaussdb.py
# Author : XJH
# Date : 2025/5/12 09:45

import psycopg2
from psycopg2 import pool
import random
from typing import List, Dict, Any, Optional
import pandas as pd
import io


class GaussDB:
    """GaussDB Database Connection and Operation Class"""

    def __init__(self, host_list: [str], dbname: str, user: str, password: str, port: int, min_conn: int, max_conn: int):
        """
         Initialize the connection pool manager

        Args:
            dbname (str): Database name
            user (str): Database user
            password (str): Database password
            host_list ([str]): List of database server hostnames or IPs
            port (int): Database port (default: 5432)
            min_conn (int): Minimum number of connections in the pool (default: 5)
            max_conn (int): Maximum number of connections in the pool (default: 20)
        """
        self.host_list = host_list
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.min_conn = min_conn
        self.max_conn = max_conn

        # Initialize connection pools for each host
        self.pools: Dict[str, pool.SimpleConnectionPool] = {}
        for host in self.host_list:
            try:
                self.pools[host] = pool.SimpleConnectionPool(
                    self.min_conn,
                    self.max_conn,
                    dbname = self.dbname,
                    user = self.user,
                    password = self.password,
                    host = host,
                    port = self.port
                )
                print(f"Connection pool initialized for host: {host}")
            except Exception as e:
                print(f"Failed to initialize pool for host {host}: {str(e)}")

    def _get_random_host(self) -> str:
        """Get a random host from the host list for load balancing"""
        return random.choice(self.host_list)

    def get_connection(self):
        """
        Get a database connection from the pool with load balancing

        Returns:
            A database connection or None if all connections failed
        """
        # Attempt to get a connection with retry logic
        for _ in range(len(self.host_list)):
            host = self._get_random_host()
            pool = self.pools.get(host)

            if not pool:
                continue

            try:
                conn = pool.getconn()
                print(f"Connection acquired from pool of host: {host}")
                return conn
            except Exception as e:
                print(f"Failed to get connection from host {host}: {str(e)}")

        print("Failed to get connection from all hosts")
        return None

    def release_connection(self, conn: psycopg2.extensions.connection) -> None:
        """
        Release a database connection back to the pool

        Args:
            conn: Database connection to release
        """
        if not conn:
            return

        host = conn.info.host
        if host and host in self.pools:
            self.pools[host].putconn(conn)
            print(f"Connection released back to pool of host: {host}")
        else:
            print("Warning: Could not determine host for connection release")

    def close_all_connections(self) -> None:
        """Close all connections in the pools and clean up resources"""
        for host, pool in self.pools.items():
            try:
                if pool:
                    pool.closeall()
                    print(f"All connections closed for host: {host}")
            except Exception as e:
                print(f"Error closing connections for host {host}: {str(e)}")

    def __enter__(self) -> 'GaussDB':
        """Support for context manager (with statement)"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Ensure resources are cleaned up when exiting context manager"""
        self.close_all_connections()

    def insert_data(self, df: pd.DataFrame, table_name: str, constraint_keys: list) -> bool | None:
        """
        Batch insert data into specified table, handle null values and support conflict updates

        Args:
            df (pd.DataFrame): pandas DataFrame data
            table_name (str): Target table name
            constraint_keys (list): The constraint key of the table

        Returns:
            True if insertion is successful, False otherwise
        """
        conn = self.get_connection()
        if not conn:
            return False

        try:
            cur = conn.cursor()

            # Convert DataFrame to CSV
            df = df.replace(r'\n|\r|\t', '', regex=True)
            output = io.StringIO()
            df.to_csv(
                output,
                index = False,
                header = False,
                na_rep = '',
                sep = ',',
                quoting = 3,
                escapechar = '\\'
            )
            output.seek(0)

            # Get column names
            columns = [col.lower() for col in df.columns]

            # Create stg table
            temp_table = self.generate_stg_table_name(table_name)
            cur.execute(f"create table if not exists {temp_table} (like {table_name});")

            # Truncate stg table
            cur.execute(f"truncate table {temp_table};")

            # Copy data from CSV to stg table
            schema_name = table_name.split('.', 1)[0]
            cur.execute(f"set search_path to {schema_name};")
            cur.copy_from(
                file = output,
                table = temp_table.split('.')[-1],
                sep = ',',
                null = '',
                columns = columns
            )

            # Construct SQL insert statement
            insert_sql = f"insert into {table_name} ({', '.join(columns)}) select {', '.join(columns)} from {temp_table}"

            # Construct ON DUPLICATE KEY UPDATE clause
            constraint_keys = constraint_keys
            update_clauses = []

            for col in columns:
                if col.upper() not in constraint_keys and col not in constraint_keys:  # Do not update primary keys or constraint key
                    update_clauses.append(f'{col} = values({col})')

            if update_clauses:
                on_conflict_sql = f"on duplicate key update {', '.join(update_clauses)}"
                final_sql = f'{insert_sql} {on_conflict_sql}, {schema_name[5:]}_update_time = current_timestamp'
            else:
                final_sql = insert_sql

            cur.execute(final_sql)
            conn.commit()

            print(f'Successfully inserted {len(df)} records into table: {table_name}')

            return True

        except Exception as e:
            print(f'Data insertion failed: {e}')
            conn.rollback()
            return False

        finally:
            if conn:
                self.release_connection(conn)

    def fetch_data(self, query: str):
        """
        Retrieve data from table, supporting batch retrieval

        Args:
            query (str): SELECT query statement

        Returns:
            Query results if successful, None otherwise
        """
        conn = self.get_connection()
        if not conn:
            return None

        try:
            # Execute query and return results
            with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()

            return result

        except Exception as e:
            print(f'Error retrieving table data: {e}')
            return None

        finally:
            if conn:
                self.release_connection(conn)

    def generate_stg_table_name(self, table_name):
        """
        Generates a staging table name by inserting '_stg' before the matched model suffix in the original table name.

        This function searches for predefined model suffixes (e.g., '_mini', '_hi') in the input table name,
        then inserts '_stg' immediately before the matched suffix to form a new STG (staging) table name.

        Args:
            table_name (str): Original table name that contains one of the predefined model suffixes.

        Returns:
            str: New table name with '_stg' inserted before the matched model suffix.

        Raises:
            ValueError: If no valid model suffix is found in the input table name.
        """
        # Predefined model suffix keywords for table pattern matching
        update_model = ['_mini', '_minf', '_hi', '_hf', '_di', '_df', '_wi', '_wf', '_mi', '_mf', '_cqi', '_cqf', '_yi',
                        '_yf']

        # Iterate through keywords to find the matching pattern in the table name
        matched_key = None
        for key in update_model:
            if table_name.endswith(key):
                return table_name + '_stg'
            elif (key + '_') in table_name:
                parts = table_name.split(key + '_', 1)
                matched_key = '_di_' + parts[1]
                print(matched_key)
                break  # Stop once found to prioritize long keywords

        if not matched_key:
            return table_name + '_stg'

        # Locate the matched keyword position and insert '_stg' before it
        prefix = table_name[:-len(matched_key)]
        return f"{prefix}_stg{matched_key}"