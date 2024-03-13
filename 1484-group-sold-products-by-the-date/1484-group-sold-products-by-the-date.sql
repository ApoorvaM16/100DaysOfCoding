# Write your MySQL query statement below
SELECT SELL_DATE, COUNT(DISTINCT PRODUCT) NUM_SOLD, 
GROUP_CONCAT(DISTINCT PRODUCT ORDER BY PRODUCT) PRODUCTS
FROM ACTIVITIES
GROUP BY SELL_DATE



# SELECT 
# 	sell_date,
# 	COUNT(DISTINCT product) AS num_sold,
# 	GROUP_CONCAT(DISTINCT product ORDER BY product) AS products 
# FROM Activities
# GROUP BY sell_date