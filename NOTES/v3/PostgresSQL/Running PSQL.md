
---

## **Running PSQL**

You must have the `postgres` process running.

---

Run the following command.

``` powershell
psql
```

| Flag | Value      | Purpose                     | Default      |
| ---- | ---------- | --------------------------- | ------------ |
| `-h` | `host`     | to set the current host     | `PGHOST`     |
| `-p` | `port`     | to set the current port     | `PGPORT`     |
| `-d` | `dbname`   | to set the current dbname   | `PGDATABASE` |
| `-U` | `username` | to set the current username | `PGUSER`     |
| `-w` |            | never prompt for password   |              |
| `-W` |            | always prompt for password  |              |

---

You may be prompted to enter the password for current username.

In `PowerShell`, you can press `Ctrl + C` to escape the password prompt.

Once you enter the correct password, you should be authenticated into `psql`.

---

If the current username matches a definition in `pgpass.conf`, the password from that file will be used to authenticate the current user and you will not be prompted to enter a password, unless you run `psql` with the flag `-W`, which will always prompt you to enter a password.

---
