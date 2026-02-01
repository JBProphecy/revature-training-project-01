
---
## Checking Postgres Installation / Version

Open a terminal and run the following command...

``` shell
postgres --version
```

---
# Entering the Postgres Terminal

Open a terminal and run the following command...

``` shell
psql -U your_username
```

You may not need to manually change the username, but this will guarantee that you are attempting to sign in with the correct one. After running this command, you will be prompted to enter your password. When you type your password, you won't see anything appear/change, but it's still registering what you type, so just type your password and press Enter. If your password is correct, you will be entered into the psql terminal.

---
# Quick Commands

`\q` - exit the special terminal / return to the normal terminal
`\l` - display all databases
`\c your_database_name` - connect to a database
`\dt` - display all tables
`\! cls` - clear screen