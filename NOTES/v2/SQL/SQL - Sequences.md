
---

# Formula of a Sequence in SQL

```
CREATE SEQUENCE sequence_name
    [ START WITH start ]
	[ INCREMENT BY increment ]
    [ MINVALUE min_value | NO MINVALUE ]
    [ MAXVALUE max_value | NO MAXVALUE ]
    [ CYCLE | NO CYCLE ]
;
```

---

# Example of a Sequence In SQL

```
CREATE SEQUENCE example_sequence_01
	START WITH 0
	INCREMENT BY 5
	MINVALUE 0
	MAXVALUE 200
	NO CYCLE
;
```

---
