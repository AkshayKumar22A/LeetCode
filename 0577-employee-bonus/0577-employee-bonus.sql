# Write your MySQL query statement below
Select e.name,b.bonus
from Employee e
LEFT JOIN  Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus IS NULL