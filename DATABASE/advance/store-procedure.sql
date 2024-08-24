syntax: 

CREATE PROCEDURE procedure_name ([parameter_list])
BEGIN
  -- Procedure body with SQL statements
END;



CREATE TABLE employees (
    ->   employee_id INT AUTO_INCREMENT PRIMARY KEY,
    ->   employee_name VARCHAR(255) NOT NULL,
    ->   salary DECIMAL(10, 2) NOT NULL
    -> );

DELIMITER //
CREATE PROCEDURE insert_employee(IN emp_name VARCHAR(255), IN emp_salary DECIMAL(10, 2))
BEGIN
   INSERT INTO employees (employee_name, salary) VALUES (emp_name, emp_salary);
END;
//
DELIMITER ;


--  get all procedure from specific database
SELECT ROUTINE_NAME 
FROM INFORMATION_SCHEMA.ROUTINES 
WHERE ROUTINE_TYPE = 'PROCEDURE' 
AND ROUTINE_SCHEMA = 'firm';


-- call procedure
CALL insert_employee('John Doe', 50000.00);


Example - 2

DELIMITER //

CREATE PROCEDURE CalculateSum(IN num1 INT, IN num2 INT, OUT result INT)
BEGIN
    SET result = num1 + num2;
END //

DELIMITER ;

CALL CalculateSum(5, 10, result);


-- Step 1: Declare the result variable
SET @result = 0;

-- Step 2: Call the stored procedure
CALL CalculateSum(5, 10, @result);

-- Step 3: Retrieve the result
SELECT @result;
