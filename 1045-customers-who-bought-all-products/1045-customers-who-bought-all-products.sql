# Write your MySQL query statement below
SELECT CUSTOMER_ID FROM CUSTOMER C
GROUP BY CUSTOMER_ID
HAVING Count(DISTINCT C.PRODUCT_KEY) = (
                    SELECT COUNT(P.PRODUCT_KEY) FROM PRODUCT P                   
)

