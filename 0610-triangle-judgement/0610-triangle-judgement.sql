# Write your MySQL query statement below
SELECT X,Y,Z, (CASE WHEN (X+Y > Z and Y+Z > X AND Z+X > Y) THEN 'Yes' ELSE 'No' END) TRIANGLE
FROM TRIANGLE


# x+y
# y+z
# z+x