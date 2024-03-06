# Write your MySQL query statement below
select e.employee_id, e.name, (case when e1.employee_id is not null then count(e1.employee_id) else null end) reports_count, (case when e1.age is not null then (round(avg(e1.age))) else null end) average_age
from employees e
join employees e1
on e.employee_id = e1.reports_to
group by e.employee_id, e.name
having reports_count is not null and average_age is not null
order by employee_id