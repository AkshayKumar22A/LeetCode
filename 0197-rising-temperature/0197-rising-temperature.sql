# Write your MySQL query statement below
Select a.id AS ID
From Weather AS a, Weather AS b
Where DATEDIFF(a.recordDate, b.recordDate) = 1 AND a.temperature > b.temperature;;