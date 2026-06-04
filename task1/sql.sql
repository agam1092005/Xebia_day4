-- Q5
SELECT d.dept_name, e.name, e.salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
JOIN (
    SELECT dept_id, MAX(salary) AS max_salary
    FROM Employees
    GROUP BY dept_id
) m ON e.dept_id = m.dept_id AND e.salary = m.max_salary;

-- Q6
SELECT 
    DATE_FORMAT(order_date, '%b') AS month,
    SUM(amount) AS total_revenue,
    COUNT(order_id) AS total_orders
FROM Orders
WHERE YEAR(order_date) = 2024
GROUP BY MONTH(order_date), DATE_FORMAT(order_date, '%b')
ORDER BY total_revenue DESC;