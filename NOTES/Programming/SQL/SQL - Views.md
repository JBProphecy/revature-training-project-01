
---

``` sql
CREATE VIEW view_name AS dql_statement;
```

``` sql
CREATE TABLE my_table (
	id INT PRIMARY KEY,
	first_name TEXT,
	last_name TEXT
);

CREATE VIEW first_and_last AS
SELECT first_name, last_name
FROM my_table;
```

---
