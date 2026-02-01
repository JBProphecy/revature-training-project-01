
---
# Types of Joins

- INNER JOIN
- LEFT JOIN / LEFT OUTER JOIN
- RIGHT JOIN / RIGHT OUTER JOIN
- FULL JOIN / FULL OUTER JOIN

---

When performing a join between two tables, you select which columns you want from each of the tables and define a condition that determines how the data will be joined. Every combination of records will be compared and the result of the join will depend on which type of join you use.

---
# INNER JOIN

An inner join will generate a table with the selected columns and a record for each pair of records that satisfies the joining condition. Every combination of records from the two tables will be compared.

---
# LEFT JOIN / LEFT OUTER JOIN

A left join will generate a table with the selected columns and at least one record for each row in the left table. Each record in the left table will be compared with each record in the right table. When considering one record from the left table and each record from the right table...
- If no records from the right table satisfy the joining condition with the record from the left table, one record will be generated in the resulting table with the selected columns from the left table containing the data from the associated record from the left table and the selected columns from the right table containing null values.
- If any records from the right table satisfy the joining condition with the record from the left table, one record will be generated in the resulting table for each successful case with the selected columns from the left table containing the data from the associated record from the left table and the selected columns from the right table containing the data from the associated record from the right table.

---
# RIGHT JOIN / RIGHT OUTER JOIN

A right join will generate a table with the selected columns and at least one record for each row in the right table. Each record in the right table will be compared with each record in the left table. When considering one record from the right table and each record from the left table...
- If no records from the left table satisfy the joining condition with the record from the right table, one record will be generated in the resulting table with the selected columns from the right table containing the data from the associated record from the right table and the selected columns from the left table containing null values.
- If any records from the left table satisfy the joining condition with the record from the right table, one record will be generated in the resulting table for each successful case with the selected columns from the right table containing the data from the associated record from the right table and the selected columns from the left table containing the data from the associated record from the left table.

---
# FULL JOIN / FULL OUTER JOIN

A full join will generate a table with the selected columns and a record for each pair of records that satisfies the joining condition, as well as a record for each record from the left table that doesn't satisfy the joining condition with any records from the right table, with the selected columns from the left table containing the data from the associated record from the left table and the selected columns from the right table containing null values, and a record for each record from the right table that doesn't satisfy the joining condition with any records from the left table, with the selected columns from the right table containing the data from the associated record from the right table and the selected columns from the left table containing null values. Every combination of records from the two tables will be compared.

---
# Examples

``` sql
CREATE TABLE authors (
	id INT PRIMARY KEY,
	name TEXT
);

CREATE TABLE books (
	id INT PRIMARY KEY,
	title TEXT,
	author_id INT REFERENCES authors(id)
);

INSERT INTO authors (id, name)
VALUES
	(1, 'Jack'),
	(2, 'Kyle'),
	(3, 'Mom'),
	(4, 'Dad');

INSERT INTO books (id, title, author_id)
VALUES
	(1, 'aaa', 3),
	(2, 'bbb', 2),
	(3, 'ccc', 3),
	(4, 'ddd', 3),
	(5, 'eee', 2),
	(6, 'fff', 1);

SELECT authors.id AS 'Author ID', books.id AS 'Book ID'
FROM authors INNER JOIN books
ON authors.id = books.id;

SELECT authors.name AS 'Author Name', books.title AS 'Book Title'
FROM authors LEFT JOIN books
ON authors.id = books.author_id;

SELECT authors.name AS 'Author Name', books.title AS 'Book Title'
FROM authors RIGHT JOIN books
ON authors.id = books.author_id;

SELECT authors.id AS 'Author ID', books.id AS 'Book ID'
FROM authors FULL JOIN books
ON authors.id = books.id;
```

---
