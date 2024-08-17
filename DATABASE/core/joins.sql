CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


INSERT INTO customers (customer_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO orders (order_id, customer_id, product) VALUES
(1, 1, 'Laptop'),
(2, 1, 'Mouse'),
(3, 2, 'Keyboard');

SELECT customers.customer_id, customers.name, orders.order_id, orders.product
    -> FROM customers
    -> LEFT JOIN orders ON customers.customer_id = orders.customer_id;
+-------------+---------+----------+----------+
| customer_id | name    | order_id | product  |
+-------------+---------+----------+----------+
|           1 | Alice   |        1 | Laptop   |
|           1 | Alice   |        2 | Mouse    |
|           2 | Bob     |        3 | Keyboard |
|           3 | Charlie |     NULL | NULL     |
+-------------+---------+----------+----------+

SELECT customers.customer_id, customers.name, orders.order_id, orders.product
    -> FROM customers
    -> RIGHT JOIN orders ON customers.customer_id = orders.customer_id;
+-------------+-------+----------+----------+
| customer_id | name  | order_id | product  |
+-------------+-------+----------+----------+
|           1 | Alice |        1 | Laptop   |
|           1 | Alice |        2 | Mouse    |
|           2 | Bob   |        3 | Keyboard |
+-------------+-------+----------+----------+

SELECT customers.customer_id, customers.name, orders.order_id, orders.product
    -> FROM customers
    -> CROSS JOIN orders;
+-------------+---------+----------+----------+
| customer_id | name    | order_id | product  |
+-------------+---------+----------+----------+
|           3 | Charlie |        1 | Laptop   |
|           2 | Bob     |        1 | Laptop   |
|           1 | Alice   |        1 | Laptop   |
|           3 | Charlie |        2 | Mouse    |
|           2 | Bob     |        2 | Mouse    |
|           1 | Alice   |        2 | Mouse    |
|           3 | Charlie |        3 | Keyboard |
|           2 | Bob     |        3 | Keyboard |
|           1 | Alice   |        3 | Keyboard |
+-------------+---------+----------+----------+