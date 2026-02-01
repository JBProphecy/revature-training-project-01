
---
# Logback Dependencies

The code below goes in **`pom.xml`** located in the root folder of your project.

``` xml
<!-- SLF4J Dependency -->
<dependency>
  <groupId>org.slf4j</groupId>
  <artifactId>slf4j-api</artifactId>
  <version>2.0.9</version> <!-- check for the latest version -->
</dependency>

<!-- Logback Core Dependency -->
<dependency>
  <groupId>ch.qos.logback</groupId>
  <artifactId>logback-classic</artifactId>
  <version>1.4.11</version> <!-- check for the latest version -->
</dependency>

<!-- Logback Classic Dependency -->
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.2.6</version> <!-- check for the latest version -->
</dependency>

```

---
# Example Logback Configuration

The code below goes in **`logback.xml`** located in **`src/main/resources`**.

---

``` xml
<configuration>
  <!-- Console Configuration -->
  <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
    <encoder>        
      <pattern>[%date] [%thread] [%level] [%logger{36}] [%file:%line] - %msg%n%ex</pattern>
      <charset>UTF-8</charset>
    </encoder>
  </appender>

  <!-- File Configuration -->
  <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
    <file>logs/app.log</file>
    <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
      <fileNamePattern>logs/app.%d{yyyy-MM-dd}.log</fileNamePattern>
      <maxHistory>30</maxHistory>
      <cleanHistoryOnStart>true</cleanHistoryOnStart>
    </rollingPolicy>
    <encoder>
      <pattern>[%date] [%thread] [%level] [%logger{36}] [%file:%line] - %msg%n%ex</pattern>
      <charset>UTF-8</charset>
    </encoder>
  </appender>

  <!-- Root Configuration -->
  <root level="debug">
    <appender-ref ref="CONSOLE" />
    <appender-ref ref="FILE" />
  </root>
</configuration>
```

---
# Log Levels

- TRACE
- DEBUG
- INFO
- WARN
- ERROR

---
## Log Level Usage

**`TRACE`** - for when you need full visibility f what's happening in your application

**`DEBUG`** - for information that may be needed for diagnosing issues or for the test environment to ensure everything is working correctly

**`INFO`** - to indicate that something normal happened

**`WARN`** - to indicate that something unexpected occurred or that something happened that may cause issues in the future, but nothing that would prevent your application from running at the moment.

**`ERROR`** - to indicate that an error occurred in your application, preventing certain aspects or the entirety of your application from functioning properly.

---
