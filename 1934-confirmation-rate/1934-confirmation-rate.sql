# Write your MySQL query statement below
# select round(/),2) from confirmations 


# select s.user_id, coalesce(round(c1.confirmed / c.total,2),0.00) confirmation_rate
# from signups s left join
# (select user_id,count(*) total from confirmations group by user_id) c on s.user_id = c.user_id 
# left join 
# (
#     select user_id,count(*) confirmed from confirmations where action = 'confirmed' group by user_id
# ) c1 on s.user_id = c1.user_id


# select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
# from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;


SELECT S.USER_ID, ROUND(AVG(IF(C. ACTION = 'CONFIRMED',1,0)),2) CONFIRMATION_RATE 
FROM SIGNUPS S LEFT JOIN CONFIRMATIONS C ON S.USER_ID = C.USER_ID GROUP BY USER_ID






