
---

**Delete Methods**

- **`ON DELETE CASCADE`**: Automatically deletes related rows in the child table.
- **`ON DELETE SET NULL`**: Sets the foreign key column(s) to `NULL`.
- **`ON DELETE SET DEFAULT`**: Sets the foreign key column(s) to a default value.
- **`ON DELETE RESTRICT`**: Prevents the deletion of the parent row if there are related child rows.
- **`ON DELETE NO ACTION`**: Similar to `RESTRICT`, but the constraint check is deferred until the end of the transaction.

---

**Update Methods**

- **`ON UPDATE CASCADE`**: Automatically updates related rows in the child table.
- **`ON UPDATE SET NULL`**: Sets foreign key column(s) to `NULL`.
- **`ON UPDATE SET DEFAULT`**: Sets foreign key column(s) to a default value when the parent row is deleted.
- **`ON UPDATE RESTRICT`**: Prevents the updating of the parent row if there are related child rows.
- **`ON UPDATE NO ACTION`**: Similar to `RESTRICT`, but the constraint check is deferred until the end of the transaction.

---
