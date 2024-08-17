-- create view
CREATE VIEW customer_orders AS
SELECT 
    customers.customer_id,
    customers.name,
    orders.order_id,
    orders.product
FROM 
    customers
LEFT JOIN 
    orders 
ON 
    customers.customer_id = orders.customer_id;

-- show all views in db
SHOW FULL TABLES WHERE TABLE_TYPE = 'VIEW';

-- update view
CREATE OR REPLACE VIEW customer_orders AS
SELECT 
    customers.customer_id,
    customers.name,
    orders.order_id,
    orders.product
FROM 
    customers
RIGHT JOIN 
    orders 
ON 
    customers.customer_id = orders.customer_id;


-- drop your view
DROP VIEW customer_orders;
