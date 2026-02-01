
---
# Examples

``` sql
CREATE TABLE parent_table (
	id INT PRIMARY KEY
);

CREATE TABLE child_table (
	id INT PRIMARY KEY,
	parent_id INT REFERENCES parent_table(id)
);
```

``` sql
CREATE TABLE parent_table (
	id INT PRIMARY KEY
);

CREATE TABLE child_table (
	id INT PRIMARY KEY,
	parent_id INT,
	FOREIGN KEY (parent_id) REFERENCES parent_table(id)
);
```

``` sql
CREATE TABLE parent_table (
	id INT PRIMARY KEY
);

CREATE TABLE child_table (
	id INT PRIMARY KEY,
	parent_id INT
	CONSTRAINT parent_table_id_fkey
		FOREIGN KEY (parent_id)
		REFERENCES parent_table(id)
);
```

``` sql
CREATE TABLE parent_table (
	id INT PRIMARY KEY
);

CREATE TABLE child_table (
	id INT PRIMARY KEY,
	parent_id INT
);

ALTER TABLE child_table
	ADD CONSTRAINT parent_table_id_fkey
		FOREIGN KEY (parent_id)
		REFERENCES parent_table(id);
```

---
