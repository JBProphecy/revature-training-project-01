
---

# Formula for a Trigger in SQL

```
CREATE TRIGGER trigger_name
	[BEFORE | AFTER] [INSERT | UPDATE | DELETE]
    ON table_name
    [FOR EACH ROW]
    [trigger_body]
;
```

```
DROP TRIGGER [IF EXISTS] trigger_name;
```

---
