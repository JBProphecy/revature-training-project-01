
---


## **Environment Variables**

| Name         | Purpose               |
| ------------ | --------------------- |
| `PGHOST`     | the default host      |
| `PGPORT`     | the default port      |
| `PGDATABASE` | the default dbname    |
| `PGUSER`     | the default username  |
| `PGPASSFILE` | path of `pgpass.conf` |

---

## PGPASSFILE / `pgpass.conf`

On `Windows`, you can use a file called `pgpass.conf` to configure passwords based on the combination of `host`, `port`, `dbname`, and `username`.

You can tell `psql` where that file is located by assigning its path to an environment variable called `PGPASSFILE`.

Each line in `pgpass.conf` is a definition, which should match the following structure.

`host:port:dbname:username:password`

When you run `psql`, if the current `host`, `port`, `dbname`, and `username` all match a definition in `pgpass.conf`, the `password` from that file will be used to authenticate the current user and you will not be prompted to enter a password. The file is searched from top to bottom, so only the first definition will be used if the current environment would match multiple definitions.

You can use an asterisk `*` as a wildcard to match anything. For example, if you only care about matching a username, you could write a definition in `pgpass.conf` as `*:*:*:username:password`.

---
