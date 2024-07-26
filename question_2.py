# Task 1

# SELECT e.employee_name, SUM(p.quantity_produced) AS total_quantity
# FROM employees e
# JOIN production p ON e.employee_id = p.employee_id
# GROUP BY e.employee_name;


# Task 2

# SELECT p.product_name, SUM(o.quantity_ordered) AS total_quantity_ordered
# FROM products p
# JOIN orders o ON p.product_id = o.product_id
# GROUP BY p.product_name
# ORDER BY total_quantity_ordered DESC;


# Task 3

# SELECT c.customer_name, SUM(o.order_value) AS total_order_value
# FROM customers c
# JOIN orders o ON c.customer_id = o.customer_id
# GROUP BY c.customer_name
# HAVING SUM(o.order_value) >= 2;


# Task 4

# SELECT p.name, SUM(pr.quantity_produced) AS total_quantity_produced
# FROM products p
# JOIN production pr ON p.product_id = pr.product_id
# WHERE pr.production_date = '2024-07-25'
# GROUP BY p.product_name;