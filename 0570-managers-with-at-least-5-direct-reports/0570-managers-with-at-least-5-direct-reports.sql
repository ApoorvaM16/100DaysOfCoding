# Write your MySQL query statement below
SELECT NAME FROM EMPLOYEE E WHERE ID IN(
SELECT managerid FROM EMPLOYEE 
GROUP BY managerID
having count(managerid) >= 5)
