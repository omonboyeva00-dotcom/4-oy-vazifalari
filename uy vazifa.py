# oxirgi 6ta misol

# -- 1-misol
# -- 5 tadan ko’p buyurtmani o’z vaqtida yetkazib bermagan hodimlar ro’yxatini chop eting
#
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id)from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where o.shipped_date > o.required_date
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) > 5
#
# -- 2-misol
# -- 10 tadan ko’p sotilgan mahsulotlar va hodimlar haqida ma’lumot
#
# -- select p.product_id,p.product_name,e.employee_id,e.first_name,e.last_name,sum(od.quantity)from products p
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- join employees e on o.employee_id = e.employee_id
# -- group by p.product_id,p.product_name,e.employee_id,e.first_name, e.last_name
# -- having sum(od.quantity) > 10
#
# -- 3-misol
# -- 20 tadan ortiq mijozga (customer) ega bo’lgan davlatlar ro’yxatini chiqarib beruvchi so’rov
# -- shakllantiring
#
# -- select country,count(customer_id)from customers
# -- group by country
# -- having count(customer_id) > 20
#
# -- 4-misol
# -- Eng ko’p zakazni amalga oshirgan hodimlar haqida ma’lumot shakllantiring
#
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) = (select max(soni)from (select count(order_id) as soni from orders
# -- group by employee_id))
#
# -- 5-misol
# -- 3 tadan ko’p buyurtmani o’z vaqtida yetkazib bermagan hodimlar ro’yhatini shakllantiring
#
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where o.shipped_date > o.required_date
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) > 3
#
# -- 6-misol
# -- Amerikada yashovchi eng faol xodimlar haqida ma'lumot shakllantiring
#
# -- select e.employee_id,e.first_name,e.last_name,e.country,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country = 'usa'
# -- group by e.employee_id, e.first_name, e.last_name, e.country
# -- having count(o.order_id) = (select max(soni)from (select count(o.order_id)as soni from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country = 'usa'
# -- group by e.employee_id))