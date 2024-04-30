# Write your MySQL query statement below
Select product_name,year,price
from sales JOIN Product
ON sales.product_id = Product.product_id;