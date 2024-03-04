# Write your MySQL query statement below
SELECT ACTIVITY_DATE AS DAY, COUNT(DISTINCT USER_ID) ACTIVE_USERS
FROM ACTIVITY
WHERE ACTIVITY_DATE > '2019-06-27' AND ACTIVITY_DATE <= '2019-07-27'
GROUP BY ACTIVITY_DATE


# SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
# FROM Activity
# WHERE (activity_date > "2019-06-27" AND activity_date <= "2019-07-27")
# GROUP BY activity_date;