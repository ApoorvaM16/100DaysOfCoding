# Write your MySQL query statement below
SELECT ID,MOVIE,DESCRIPTION, RATING FROM CINEMA
WHERE ID % 2 <> 0 AND DESCRIPTION != 'BORING' ORDER BY RATING DESC