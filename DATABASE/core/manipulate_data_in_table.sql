-- insert data into the table
>>> insert into users(username, email, password)values('brijesh07', 'brijesh@gmail.com', 'test@123');

-- select all columns from the table
>>> select * from users;
+---------+-----------+-------------------+----------+
| user_id | username  | email             | password |
+---------+-----------+-------------------+----------+
|       1 | brijesh07 | brijesh@gmail.com | test@123 |
+---------+-----------+-------------------+----------+

-- select specific column
>>> select username, email from users;
+-----------+-------------------+
| username  | email             |
+-----------+-------------------+
| brijesh07 | brijesh@gmail.com |
| admin07   | admin@gmail.com   |
+-----------+-------------------+

-- update a specific data
>>> update users set password = 'test123' where user_id = 1;

-- delete a specific data
>>> delete from users where user_id < 3;