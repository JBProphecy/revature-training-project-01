
---

## **Summary**

`PostgresSQL` is an object-relational database management system (`ORDBMS`).

---

## **Conventions**

The following conventions are used in the synopsis of a command:
- brackets `[` and `]` indicate optional elements
- braces `{` and `}` and pipes `|` indicate several elements and you must choose one
- dots `...` indicate that the preceding element can be repeated.

---

## **Architecture**

`PostgresSQL` uses a `client/server model`.

The database server program is called `postgres`.

The `client` and `server` can be on different hosts and communicate via a `TCP/IP` network connection.

The `PostgresSQL` server can handle multiple concurrent connections at once. To achieve this, it starts/forks a new process for each connection. From that point, the client and the new server process communicate without intervention by the original `postgres` process.

---

**`Command`**

``` powershell
createdb mydb
```

This command will create a database.

---

**`Command`**

``` powershell
dropdb mydb
```

This command will delete a database.

---
