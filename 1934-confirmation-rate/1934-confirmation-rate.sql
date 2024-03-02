# Write your MySQL query statement below
# select round(/),2) from confirmations 


select s.user_id, coalesce(round(c1.confirmed / c.total,2),0.00) confirmation_rate
from signups s left join
(select user_id,count(*) total from confirmations group by user_id) c on s.user_id = c.user_id 
left join 
(
    select user_id,count(*) confirmed from confirmations where action = 'confirmed' group by user_id
) c1 on s.user_id = c1.user_id


