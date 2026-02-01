
---

```
pytest
```

This command will run all tests.

---

```
pytest file_name
```

This command will run all tests in a specific file.

---

```
pytest --cov
```

This command will show a coverage report after tests run.

---

```
pytest -s
```

This command is useful for showing `print` statements in the console during tests.

I don't see any reason to use `print` when I can use a `logger`.

---

```
pytest -o log_cli=true -o log_cli_level=INFO
```

```
pytest -o log_cli=true -o log_cli_level=DEBUG
```

These commands are useful for showing logs in the console during tests.

I use these in my library where I don't have any handlers configured.

```
-o log_cli=true -o log_cli_level=DEBUG
```

---
