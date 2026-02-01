
---

``` properties
management.endpoints.web.exposure.include=*
```

---

1. **/health:** This endpoint provides basic health information about the application. It's often used by software orchestration tools to check the application's health status.

2. **/info:** It returns arbitrary application information. By default, this endpoint is empty. You can populate it with information such as build version, Git commit ID, and more by customizing it via the application properties.

3. **/metrics:** It provides detailed metrics information about the JVM, application usage, and system details. These metrics are useful for monitoring and diagnosing performance issues.

4. **/loggers:** It allows you to view and change the logging level of your application dynamically. This can be particularly useful when diagnosing problems in a live application.

5. **/threaddump:** This endpoint is useful for troubleshooting and diagnostics. It performs a thread dump, allowing you to see what every thread in the JVM is doing.

6. **/heapdump:** This endpoint returns a heap dump from the JVM used by the application. This is especially useful when diagnosing memory-related issues.

7. **/auditevents:** It exposes audit events in your application, including authentication events (like login and logout). You can customize which events get captured based on your needs.

8. **/httptrace:** It keeps trace information about the last 100 HTTP request-response exchanges. It's an invaluable tool for diagnosing issues or understanding how traffic flows through the application.

9. **/env:** It provides details about the environment in which the application is running. This includes property sources and system properties.

---
