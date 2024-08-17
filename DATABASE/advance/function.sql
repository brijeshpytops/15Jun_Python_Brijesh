-- function basic syntax:
CREATE FUNCTION function_name(parameter_name datatype, ...)
RETURNS return_datatype
DETERMINISTIC
BEGIN
    -- Declare variables (if needed)
    
    -- Function logic
    
    RETURN value;  -- Return a value
END;


-- function_name: The name of the function.
-- parameter_name datatype: Input parameters with their respective data types.
-- RETURNS return_datatype: Specifies the data type of the value the function will return.
-- DETERMINISTIC: Indicates that the function always returns the same result given the same input parameters. (Use NOT DETERMINISTIC if this is not the case.)
-- BEGIN ... END: Defines the body of the function where you can include SQL statements.
-- RETURN value: The value that will be returned when the function is called.

-- create function
use functions;

DELIMITER //

CREATE FUNCTION add_numbers(x INT, y INT)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN x + y;
END//

DELIMITER ;

-- call function
SELECT add_numbers(5, 20) AS result;  -- This will return 15

-- drop function
DROP FUNCTION function_name;
DROP FUNCTION IF EXISTS calculate_discount;



