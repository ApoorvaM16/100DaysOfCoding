# Write your MySQL query statement below
Select a.name as Employee from employee a
left join employee b
on a.managerid = b.id where a.salary > b.salary