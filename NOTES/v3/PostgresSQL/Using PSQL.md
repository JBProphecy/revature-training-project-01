
---

## **Quick Commands**

| Command     | Purpose                           | Parameters |
| ----------- | --------------------------------- | ---------- |
| `\q`        | to exit `psql`                    |            |
| `\! cls`    | to clear the screen               |            |
| `\c`        | to display the current connection |            |
| `\l`        | to display a list of database     |            |
| `\c dbname` | to connect to a database          | `dbname`   |

---

**`Command`**

``` psql
\q
```

This command will exit `psql`.

---

**`Command`**

``` psql
\! cls
```

This command will clear the screen.

---

**`Command`**

``` psql
\c
```

This command will display the current connection.

---

**`Command`**

``` psql
\l
```

This command will display a list of database.

You can use `\c dbname`, with `dbname` as any of the listed databases to connect to it.

---

**`Command`**

``` psql
\c dbname
```

This command will connect you to a database.
- `dbname` should be the name of a database
- you can display a list of databases with `\l`

---
