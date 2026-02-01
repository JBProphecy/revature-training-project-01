
---

# Formula for a Procedure in SQL

```
parameter = [IN | OUT | INOUT] parameter_name parameter_datatype
parameters = parameter, parameter, ...
```

```
DELIMITER $$
CREATE PROCEDURE procedure_name(parameters)
BEGIN
	formula_body
END $$
DELIMITER ;
```

```
DROP PROCEDURE [IF EXISTS] procedure_name;
```

---

# Example for a Procedure in SQL

```
DELIMITER $$
CREATE PROCEDURE UpdateEmployeeSalaries(IN PercentageIncrease DECIMAL(5,2))
BEGIN
	UPDATE employees
	SET salary = salary * (1 + PercentageIncrease / 100);
END $$
DELIMITER ;
```

---