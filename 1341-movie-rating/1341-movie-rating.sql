(SELECT NAME as results FROM USERS U JOIN MOVIERATING M
ON U.USER_ID = M.USER_ID
GROUP BY M.USER_ID
order by count(m.user_id) desc,name
LIMIT 1)
union all               
(SELECT TITLE as results FROM MOVIES M1 JOIN MOVIERATING M2
ON M1.MOVIE_ID = M2.MOVIE_ID
WHERE CREATED_AT LIKE '2020-02-%'
GROUP BY M2.MOVIE_ID
order by avg(rating) desc, title
limit 1)

                           
                          