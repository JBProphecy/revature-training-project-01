
---

## **Installation & Configuration**

**`Link to Downloads`**
https://www.enterprisedb.com/download-postgresql-binaries

---

**`Create the Following File Structure`**
- `pgsql`
	- `clusters`
	- `versions`
	- `pgpass.conf`

---

**`Set Environment Variables`**
- `PGHOST` = `localhost`
- `PGPORT` = `5432`
- `PGDATABASE` = `postgres`
- `PGUSER` = `postgres`
- `PGPASSFILE` = path to `pgsql/pgpass.conf`

---

The rest of this guide is for `PostgresSQL 18.1` specifically.

---

**`Install Binary for PostgresSQL 18.1`**
- Download the zip folder for version `18.1`.
- Extract the zip folder.
- Delete the zip folder.
- Rename the real folder to `18.1`.
- Move `18.1` into `pgsql/versions`.

---

**`Define Cluster for Postgres 18.1`**
- Create a folder called `18` (the major version) in `pgsql/clusters`.

---

**`Current Snapshot of File System`**
- `pgsql`
	- `clusters`
		- `18`
	- `versions`
		- `18.1`
	- `pgpass.conf`

---

**`Set Environment Variables`**
- `PGDATA` = path to `pgsql/clusters/18`

---

**`Add to Environment Path`**
- path to `pgsql/versions/18.1/bin`

---

**`Create Cluster`**

``` powershell
initdb --auth "scram-sha-256" --username "postgres" --pwprompt
```

It's conventional to use `postgres` as the default superuser. I have aligned this value with `PGUSER`.

You may want to change encoding, it will use your system encoding by default. I changed my system encoding to `UTF-8` so I don't have to set it.

You don't need to set `--pgdata` when `PGDATA` is set.

This command should only be ran once.

You will be prompted to enter a password.

---

**`Update Password Configuration`**

In `pgpass.conf`, add line `*:*:*:postgres:password` (where `password` is what you entered)

---

## **Server Flow - Manual**

**`Start Cluster`**

``` powershell
pg_ctl start --wait --log "C:\software\pgsql\clusters\18\logfile.log"
```

You don't need to set `--pgdata` if the environment variable `PGDATA` exists.

---

**`Restart Cluster`**

``` powershell
pg_ctl restart --wait --log "C:\software\pgsql\clusters\18\logfile.log"
```

You don't need to set `--pgdata` if the environment variable `PGDATA` exists.

---

**`Stop Cluster`**

``` powershell
pg_ctl stop --wait --log "C:\software\pgsql\clusters\18\logfile.log"
```

You don't need to set `--pgdata` if the environment variable `PGDATA` exists.

---

## **Server Flow - Manual**

**`Register Service`**

``` powershell
pg_ctl register -N "PostgresSQL Cluster 18" -D "C:\software\pgsql\clusters\18" -U "NT AUTHORITY\NetworkService" -S auto
```

This command should register the service and the service should start automatically on boot.

You'll need to start the service manually when you create it, unless you reboot your system.

``` powershell
Start-Service "PostgresSQL Cluster 18"
```

---
