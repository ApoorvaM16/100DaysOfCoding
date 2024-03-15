# Write your MySQL query statement below
SELECT MAX(P.NUM) NUM FROM MYNUMBERS M 
JOIN (SELECT NUM FROM MYNUMBERS
GROUP BY NUM
HAVING COUNT(NUM) = 1) P ON P.NUM = M.NUM