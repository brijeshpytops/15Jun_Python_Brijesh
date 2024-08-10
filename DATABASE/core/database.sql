-- Create database
>>> create database [database-name];

-- Show all databases
>>> show databases;

-- Use specific database
>>> use [database-name];

-- update database [Import/Export]
>>> [Export] mysqldump -u [username] -p [database_name] > [filename].sql
>>> [Import] mysql -u root -p my_database < backup.sql

-- Delete database
>>> drop database [database-name];