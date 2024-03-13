# Write your MySQL query statement below
# SELECT *FROM USERS
# WHERE MAIL LIKE '%leetcode.com'
SELECT *FROM USERS
WHERE MAIL REGEXP '^[A-Za-z][A-Za-z0-9\.\\-\_]*@leetcode[.]com$'




























# SELECT *
# FROM Users
# WHERE regexp_like(mail, '^[A-Za-z]+[A-Za-z0-9_.-]*@leetcode[.]com')