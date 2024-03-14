# Write your MySQL query statement below
SELECT ROW_NUMBER() OVER(ORDER BY IF (MOD(ID,2) = 0, ID-1, ID+1)) ID,
        STUDENT FROM SEAT