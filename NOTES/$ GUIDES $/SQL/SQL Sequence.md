
---

## **Creating a Sequence**

**Default Values for `SQL`**

| Name         | Value                             |
| ------------ | --------------------------------- |
| `START WITH` | implementation-dependent          |
| `MINVALUE`   | `1` (ascending)                   |
| `MAXVALUE`   | the highest representable integer |
| `CYCLE`      | `NO CYCLE`                        |
| `CACHE`      | implementation-dependent          |

**Default Values for `PostgresSQL`

| Name        | Value      |
| ----------- | ---------- |
| `INCREMENT` | `1`        |
| `START`     | `MINVALUE` |
| `MINVALUE`  | `1`        |
| `MAXVALUE`  | `2^63 - 1` |
| `CYCLE`     | `NO`       |
| `CACHE`     | `1`        |

---

``` sql
CREATE SEQUENCE my_sequence
  START WITH 1
  INCREMENT BY 1
  MINVALUE 1
  MAXVALUE 100
  NO CYCLE
  CACHE 20
```

``` postgresql
ALTER SEQUENCE my_sequence RESTART WITH 1;
```

``` postgresql
ALTER SEQUENCE my_sequence OWNED BY 1 my_table.my_column;
```

---
