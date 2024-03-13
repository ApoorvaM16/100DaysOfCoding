# Write your MySQL query statement below
# select coalesce( (select salary
# from employee
# where salary not in (select max(salary) from employee)
# order by salary desc
# limit 1), null) SecondHighestSalary 


SELECT MAX(SALARY) SecondHighestSalary
FROM EMPLOYEE
WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)

# SELECT COALESCE(
#     (SELECT salary AS SecondHighestSalary 
#      FROM employee
#      WHERE salary NOT IN (SELECT MAX(salary) FROM employee)
#      ORDER BY salary DESC
#      LIMIT 1),
#     NULL
# ) AS SecondHighestSalary;
