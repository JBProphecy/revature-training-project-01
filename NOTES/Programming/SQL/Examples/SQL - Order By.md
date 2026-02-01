
---
# ORDER BY

This clause is used to order the results of a query. By default, `ORDER BY` is `ASC`.

**Ascending Order**

``` sql
SELECT columns FROM my_talbe ORDER BY column_name;

SELECT columns FROM my_table ORDER BY column_name ASC;
```

**Descending Order**

``` sql
SELECT columns FROM my_table ORDER BY column_name DESC;
```

**Multiple Columns**

``` sql
SELECT columns
FROM my_talbe
ORDER BY column_name_01 DESC, column_name_02, column_name_03 DESC;
```

---
