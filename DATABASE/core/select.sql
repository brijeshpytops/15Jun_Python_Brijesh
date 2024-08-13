-- Select all data from the table
>>> select * from posts;

-- filtyer specific data
>>> select * from posts where user_id = 3;

-- set limit
>>> select * from posts limit 5;

-- filter using operator
>>> select * from posts where post_id >= 2 and post_id <= 16;
>>> select * from posts where post_id  between 2 and 16;
>>> SELECT * FROM users WHERE username IN ('alice', 'bob', 'carol');

-- using LIKE
>>>  SELECT * FROM users WHERE username LIKE 'a%';

-- aggrigate function
>>> select sum(post_id) AS sum_of_post_id from posts where post_id < 4;
>>> select AVG(post_id) AS sum_of_post_id from posts where post_id < 4;
>>> select MIN(post_id) AS sum_of_post_id from posts where post_id < 4;
>>> select MAX(post_id) AS sum_of_post_id from posts where post_id < 4;

-- order by
>>> select * from posts order by post_id DESC;