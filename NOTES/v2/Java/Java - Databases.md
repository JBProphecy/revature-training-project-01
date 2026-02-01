
---
# Terms

**`DAO`** - Data Access Object
**`JDBC`** - Java Database Connectivity
**`RDBMS`** - Relational Database Management System
**`URL`** - Uniform Resource Loader

---
# Tools

| RDBMS       | JDBC Driver                                  | URL Format                                            |
| ----------- | -------------------------------------------- | ----------------------------------------------------- |
| MySQL       | com.mysql.jdbc.Driver                        | jdbc:mysql://hostname/databaseName                    |
| Oracle      | oracle.jdbc.driver.OracleDriver              | jdbc:oracle:thin:@hostname:portNumber:databaseName    |
| SQLServer   | com.microsoft.sqlserver.jdbc.SQLServerDriver | jdbc:sqlserver://serverName:portNumber;property=value |
| PostgresSQL | org.postgresql.Driver                        | jdbc:postgresql://hostname:port/databaseName          |

---
# Important Concepts

- connection object
- prepared statements

---

- A prepared statement protects against SQL injection.

---
# Example Connection (PostgreSQL)

``` xml
<dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.7.5</version> <!-- Check for latest version -->
</dependency>
```

``` java
package com.example.app;

import java.sql.*;

public class App {
	public static void main (String[] args) {
		String url = "jdbc:postgresql://localhost:3000/myDatabase";
		String username = "example-username";
		String password = "example-password";
		try {
			Connection connection = DriverManager.getConnection(url, username, password);
			System.out.println(connection.isValid(5));
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
```

``` java
package com.example.app;

import java.sql.*;

public class PSQLConnectionUtility {
	static String url = "jdbc:postgresql://localhost:3000/myDatabase";
	static String username = "example-username";
	static String password = "example-password";

	static Connection getConnection() {
	
		Connection connection = null;
		
		try {
			connection = DriverManager.getConnection(url, username, password);
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
		
		return connection;
	}
}
```

``` java
package com.example.app;

import java.sql.*;

public class App {
	public static void main (String[] args) {
		try {
			Connection connection = PSQLConnectionUtility.getConnection();
			System.out.println(connection.isValid(5));
		}
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}
```

---
# Terms

**`DriverManager`** class
**`DataSource`** interface
**`Connection`** interface
- **`createStatement()`**
- **`prepareStatement(String sql)`**
- **`prepareCall(String sql)`**
- **`setAutoCommit(boolean autoCommit)`**
- **`rollback(Savepoint savepoint)`**
- **`commit()`**
- **`setSavepoint(String name)`**
- **`close()`**
- **`isClosed()`**
**`SQLException`** class
**`Statement`** interface
**`PreparedStatement`** interface
- extends the Statement interface
**`CallableStatement`** interface
- extends the PreparedStatement interface
**`ResultSet`** interface
- **`next()`**
- **`previous()`**
- **`first()`**
- **`last()`**
- **`absolute(int row)`**
- **`isFirst()`**
- **`isLast()`**

---
