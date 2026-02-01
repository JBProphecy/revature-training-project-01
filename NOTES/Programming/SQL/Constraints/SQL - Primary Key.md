
---
# Notes

There are three types of primary keys: surrogate keys, natural keys, and composite keys.

---
# Examples

``` sql
CREATE TABLE my_table (
	id INT PRIMARY KEY
);
```

``` sql
CREATE TABLE my_table (
	id INT,
	PRIMARY KEY (id)
);
```

``` sql
CREATE TABLE my_table (
	id INT
	CONSTRAINT my_table_pkey PRIMARY KEY (id);
);
```

``` sql
CREATE TABLE my_table (
	id INT
);

ALTER TABLE my_table
	ADD CONSTRAINT my_table_pkey
		PRIMARY KEY (id);

ALTER TABLE my_table
	DROP CONSTRAINT my_table_pkey;
```

``` sql
CREATE TABLE my_table (
	id_01 INT,
	id_02 INT,
	PRIMARY KEY (id_01, id_02)
);
```

---
