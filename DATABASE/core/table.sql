-- Create table

create table table_name (col1 data_type config, col2 data_type config....);

Example :
-- create table users(user_id int auto_increment primary key, username varchar(255), email varchar(255) not null unique, password varchar(255) not null);

-- show avaliable tables in database
>>> show tables;

-- Describe table structure
>>> describe users;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| user_id  | int          | NO   | PRI | NULL    | auto_increment |
| username | varchar(255) | YES  |     | NULL    |                |
| email    | varchar(255) | NO   | UNI | NULL    |                |
| password | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+

-- modify column config
>>> alter table users modify username varchar(255) not null unique;

-- add new column
>>> alter table users add mobile varchar(50) unique not null;

-- drop column
>>> alter table users drop column mobile;

-- Delete table data with structure
>>> drop table students;

-- To delete all data from a table in MySQL, you can use the TRUNCATE command. The TRUNCATE command is faster and more efficient than DELETE when you want to remove all rows from a table because it deallocates the data pages used by the table and resets any AUTO_INCREMENT counters.
>>> TRUNCATE TABLE table_name;


-- referance table posts
create table posts(post_id int auto_increment primary key, title varchar(155), content varchar(255), user_id int, FOREIGN KEY (user_id) REFERENCES users(user_id));