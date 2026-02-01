
---
# CREATE

**Create Database**

``` sql
CREATE DATABASE database_name;
```

**Create Table**

``` sql
CREATE TABLE table_name;

CREATE TABLE table_name (
	column_name data_type constraint,
	...
)
```

---
# ALTER

**Add Column**

``` sql
ALTER TABLE table_name ADD column_name data_type;

ALTER TABLE table_name ADD (
	column_name data_type,
	...
);
```

**Alter Column**

``` sql
ALTER TABLE table_name ALTER COLUMN column_name action;
```

**Drop Column**

``` sql
ALTER TABLE table_name DROP COLUMN column_name;
```

**Rename Table**

``` sql
ALTER TABLE table_name RENAME TO table_name;
```

**Rename Column**

``` sql
ALTER TABLE table_name RENMAME COLUMN column_name TO column_name;
```

---
# DROP

**Drop a Database**

``` sql
DROP DATABASE database_name;
```

**Drop a Table**

``` sql
DROP TABLE table_name;
```

---
# TRUNCATE

**Truncate Table**

``` sql
TRUNCATE TABLE table_name;
```

---
