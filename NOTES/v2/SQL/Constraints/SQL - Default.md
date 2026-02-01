
---
# Examples

``` sql
CREATE TABLE my_table (
	id INT PRIMARY KEY,
	description TEXT DEFAULT 'no description'
);

ALTER TABLE my_table ALTER COLUMN description
SET DEFAULT 'this will replace any existing default value';

ALTER TABLE my_table ALTER COLUMN description
DROP DEFAULT;
```

---
