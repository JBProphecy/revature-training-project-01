
---

# Formula for a Custom Function

```
parameter = parameter_name parameter_datatype
parameters = parameter, parameter, ...
```

```
DELIMITER $$
CREATE FUNCTION function_name(parameters)
RETURNS return_datatype
BEGIN
	function_body
END $$
DELIMITER ;
```

```
DROP FUNCTION [IF EXISTS] function_name;
```

---

# Example for a Custom Function

```
DELIMITER $$
CREATE FUNCTION example_function_01(account_number integer)
RETURNS integer
BEGIN
	DECLARE account_balance;

	SELECT balance INTO account_balance
	FROM accounts
	WHERE id = account_number
	LIMIT 1;

	RETURN account_balance
END $$
DELIMITER ;
```

---
