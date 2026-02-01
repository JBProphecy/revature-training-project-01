
---

A comment in SQL starts with the `--` symbol.

``` sql
-- This is a comment in SQL.

--This is another comment.

-- It's recommended to put a space between -- and the following text for readability.
```

---

A string literal must be defined using single quotes rather than double quotes.

``` sql
SELECT name FROM my_table WHERE name = 'Jack'; -- this is correct

SELECT name FROM my_table WHERE name = "Jack"; -- this is incorrect
```

---

It's best to use joins rather than subqueries when possible, as joins have better performance.

---

An SQL transaction is a series of one or more SQL operations that are treated as a single unit of work.

---
