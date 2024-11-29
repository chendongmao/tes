vice:[307] - Closed AlertBootstrapService...
[INFO] 2024-11-29 16:09:23.727 +0800 org.apache.dolphinscheduler.alert.rpc.AlertRpcServer:[56] - Closing alert rpc server...
[ERROR] 2024-11-29 16:09:23.727 +0800 org.apache.dolphinscheduler.alert.AlertServer:[98] - Alert server stop failed, cause: alert server destroy
java.lang.NullPointerException: null
        at org.apache.dolphinscheduler.alert.registry.AlertRegistryClient.close(AlertRegistryClient.java:53)
        at org.apache.dolphinscheduler.alert.AlertServer.destroy(AlertServer.java:93)
        at org.apache.dolphinscheduler.alert.AlertServer.close(AlertServer.java:70)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:483)
        at org.springframework.beans.factory.annotation.InitDestroyAnnotationBeanPostProcessor$LifecycleElement.invoke(InitDestroyAnnotationBeanPostProcessor.java:389)
        at org.springframework.beans.factory.annotation.InitDestroyAnnotationBeanPostProcessor$LifecycleMetadata.invokeDestroyMethods(InitDestroyAnnotationBeanPostProcessor.java:347)
        at org.springframework.beans.factory.annotation.InitDestroyAnnotationBeanPostProcessor.postProcessBeforeDestruction(InitDestroyAnnotationBeanPostProcessor.java:177)
        at org.springframework.beans.factory.support.DisposableBeanAdapter.destroy(DisposableBeanAdapter.java:197)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.destroyBean(DefaultSingletonBeanRegistry.java:587)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.destroySingleton(DefaultSingletonBeanRegistry.java:559)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.destroySingleton(DefaultListableBeanFactory.java:1163)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.destroySingletons(DefaultSingletonBeanRegistry.java:520)
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.destroySingletons(DefaultListableBeanFactory.java:1156)
        at org.springframework.context.support.AbstractApplicationContext.destroyBeans(AbstractApplicationContext.java:1106)
        at org.springframework.context.support.AbstractApplicationContext.doClose(AbstractApplicationContext.java:1075)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.doClose(ServletWebServerApplicationContext.java:174)
        at org.springframework.context.support.AbstractApplicationContext.close(AbstractApplicationContext.java:1021)
        at org.springframework.boot.SpringApplication.handleRunFailure(SpringApplication.java:790)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:326)
        at org.springframework.boot.builder.SpringApplicationBuilder.run(SpringApplicationBuilder.java:164)
        at org.apache.dolphinscheduler.alert.AlertServer.main(AlertServer.java:55)
        Suppressed: java.lang.NullPointerException: null
                at org.apache.dolphinscheduler.alert.rpc.AlertRpcServer.close(AlertRpcServer.java:57)
                ... 23 common frames omitted
[INFO] 2024-11-29 16:09:23.727 +0800 org.apache.dolphinscheduler.alert.registry.AlertRegistryClient:[52] - AlertRegistryClient closing...
[WARN] 2024-11-29 16:09:23.727 +0800 org.springframework.beans.factory.support.DisposableBeanAdapter:[248] - Invocation of close method failed on bean with name 'alertRegistryClient': java.lang.NullPointerException
[INFO] 2024-11-29 16:09:23.729 +0800 org.apache.curator.framework.imps.CuratorFrameworkImpl:[998] - backgroundOperationsLoop exiting
[WARN] 2024-11-29 16:09:23.751 +0800 org.apache.zookeeper.ClientCnxn:[1286] - An exception was thrown while closing send thread for session 0x100010b8ec90020.
org.apache.zookeeper.ClientCnxn$EndOfStreamException: Unable to read additional data from server sessionid 0x100010b8ec90020, likely server has closed socket
        at org.apache.zookeeper.ClientCnxnSocketNIO.doIO(ClientCnxnSocketNIO.java:77)
        at org.apache.zookeeper.ClientCnxnSocketNIO.doTransport(ClientCnxnSocketNIO.java:350)
        at org.apache.zookeeper.ClientCnxn$SendThread.run(ClientCnxn.java:1282)
[INFO] 2024-11-29 16:09:23.853 +0800 org.apache.zookeeper.ClientCnxn:[568] - EventThread shut down for session: 0x100010b8ec90020
[INFO] 2024-11-29 16:09:23.853 +0800 org.apache.zookeeper.ZooKeeper:[1232] - Session: 0x100010b8ec90020 closed
[INFO] 2024-11-29 16:09:23.854 +0800 org.apache.dolphinscheduler.alert.rpc.AlertRpcServer:[56] - Closing alert rpc server...
[WARN] 2024-11-29 16:09:23.854 +0800 org.springframework.beans.factory.support.DisposableBeanAdapter:[248] - Invocation of close method failed on bean with name 'alertRpcServer': java.lang.NullPointerException
[INFO] 2024-11-29 16:09:23.854 +0800 org.apache.dolphinscheduler.alert.service.AlertBootstrapService:[307] - Closed AlertBootstrapService...
[INFO] 2024-11-29 16:09:23.859 +0800 com.zaxxer.hikari.HikariDataSource:[350] - DolphinScheduler - Shutdown initiated...
[INFO] 2024-11-29 16:09:23
