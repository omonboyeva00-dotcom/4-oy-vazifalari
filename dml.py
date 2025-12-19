# 1-misol
# -- select
# --     to_char(o.order_date, 'MM') as oy,
# --     count(distinct o.order_id) as zakas_soni
# -- from orders o
# -- join order_details od on o.order_id = od.order_id
# -- join products p on od.product_id = p.product_id
# -- where
# --     p.category_id = 1
# --     and p.unit_price > 10
# --     and to_char(o.order_date, 'YYYY') = '1996'
# -- group by oy
# -- order by oy;
#
# 2-misol
# -- select
# --     s.company_name
# -- from suppliers s
# -- join products p on s.supplier_id = p.supplier_id
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- where
# --     p.category_id = 3
# --     and p.unit_price = (
# --         select min(unit_price)
# --         from products
# --         where category_id = 3
# --     )
# --     and to_char(o.order_date, 'YYYY-MM') = '1997-07'
# -- group by s.company_name;
#
# 3-misol
# -- select
# --     e.first_name,
# --     e.last_name
# -- from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where to_char(o.order_date, 'YYYY-MM') = '1998-03'
# -- group by e.first_name, e.last_name;
#
# 4-misol
# -- select
# --     c.category_name,
# --     p.product_name,
# --     sum(od.quantity) as sotilgan_soni
# -- from categories c
# -- join products p on c.category_id = p.category_id
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- where
# --     to_char(o.order_date, 'YYYY') = '1996'
# --     and p.unit_price = (
# --         select max(p2.unit_price)
# --         from products p2
# --         where p2.category_id = p.category_id
# --     )
# -- group by c.category_name, p.product_name;
#
# 5-misol
# -- select
# --     s.company_name
# -- from suppliers s
# -- join products p on s.supplier_id = p.supplier_id
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- join customers c on o.customer_id = c.customer_id
# -- where
# --     s.country = 'USA'
# --     and c.country = 'USA'
# --     and to_char(o.order_date, 'YYYY') = '1997'
# -- group by s.company_name;
#
# 6-misol
# -- select
# --     e.first_name,
# --     e.last_name
# -- from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- join order_details od on o.order_id = od.order_id
# -- join products p on od.product_id = p.product_id
# -- where
# --     p.category_id = 5
# --     and to_char(o.order_date, 'YYYY') = '1997'
# -- group by e.first_name, e.last_name;
#
# 7-misol
# -- select
# --     c.city,
# --     to_char(o.order_date, 'MM') as oy,
# --     count(o.order_id) as zakas_soni
# -- from customers c
# -- join orders o on c.customer_id = o.customer_id
# -- where
# --     c.country = 'USA'
# --     and to_char(o.order_date, 'YYYY') = '1997'
# -- group by c.city, oy
# -- order by c.city, oy;

