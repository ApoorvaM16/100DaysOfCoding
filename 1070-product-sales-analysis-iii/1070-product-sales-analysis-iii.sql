# Write your MySQL query statement below
-- SELECT S.PRODUCT_ID, YEAR AS FIRST_YEAR, QUANTITY, PRICE
-- FROM SALES S 
-- JOIN ( SELECT PRODUCT_ID,MIN(YEAR) FIRSTYEAR FROM SALES              
--     GROUP BY PRODUCT_ID) P
-- ON YEAR = P.FIRSTYEAR AND S.PRODUCT_ID = P.PRODUCT_ID





SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
SELECT product_id, MIN(year) as year
FROM Sales
GROUP BY product_id) ;


