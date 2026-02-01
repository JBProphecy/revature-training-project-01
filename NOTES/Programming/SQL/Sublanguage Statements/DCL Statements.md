
---
# GRANT

**General Formula**

``` sql
GRANT PRIVILEGES ON object TO user;
```

## Examples

``` sql
GRANT SELECT ON my_table TO 'jack.user';

GRANT SELECT, INSERT, UPDATE, DELETE ON my_table TO 'jack.user';
```

---
# REVOKE

**General Formula**

``` sql
REVOKE PRIVILEGES ON object FROM user;
```

## Examples

``` sql
REVOKE SELECT ON my_table FROM 'jack.user';

REVOKE SELECT, INSERT, UPDATE, DELETE ON my_table FROM 'jack.user';
```

---
