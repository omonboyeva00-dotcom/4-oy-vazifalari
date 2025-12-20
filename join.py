# -- uy-vazifa
# -- 1-misol
# -- Eng ko`p zakaz qilingan mahsulot turi bo`yicha hisobot shakllantiring
#
# -- select c.category_name as mahsulot_turi, sum(od.quantity) as jami_zakaz from categories c
# -- inner join products p on c.category_id = p.category_id
# -- inner join order_details od on p.product_id = od.product_id
# -- group by c.category_name
# -- order by jami_zakaz
#
#
# -- 2-misol
# -- Amerikada yashovchi eng faol hodimlar haqida ma`lumot shakllantiring
#
# -- select e.employee_id,e.country,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- having count(o.order_id)=(select count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id) desc
#
# -- 3-misol
# -- Qaysi davlatdagi hodimlar eng faol ishlashi haqidagi hisobot shakllantiring
#
# -- select e.country as davlat,count(o.order_id) as jami_zakaz from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- group by e.country
# -- order by jami_zakaz desc
#
#
# -- 4-misol
# -- 1997-yilda eng ko`p summada buyurtma qilgan haridorlar haqida m`lumot
#
# -- select c.customer_id,c.company_name,sum(od.quantity*od.unit_price*(1-od.discount)) as jami_summa from customers c
# -- join orders o on c.customer_id=o.customer_id
# -- join order_details od on o.order_id=od.order_id
# -- where to_char(order_date,'yyyy')='1997'
# -- group by c.customer_id, c.company_name
# -- order by jami_summa desc
#
# -- 5-misol
# -- Eng kam buyurtma qilingan mahsulotlar
#
# -- select p.product_id,p.product_name, sum(od.quantity) from products p
# -- join order_details od on od.product_id=od.product_id
# -- group by p.product_id,p.product_name
# -- order by product_id
#
# -- 6-misol
# -- 1-kategoriyadagi eng qimmat sotilgan 10ta mahsulot kim tomonidan zakaz qilinganligi va qaysi
# -- kompaniya tomonidan yetkazib berilganligi haqida ma`lumot
#
# -- select p.product_name, od.unit_price,c.company_name, s.company_name from products p
# -- join categories cat on p.category_id = cat.category_id
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- join customers c on o.customer_id = c.customer_id
# -- join suppliers s on p.supplier_id = s.supplier_id
# -- where p.category_id = 1
# -- order by od.unit_price desc
#
# -- 7-misol
# -- Ko`p zakaz qilingan ammo narxi arzon mahsulotlar ro`yxatini shakllantiring
#
# -- select p.unit_price, p.product_name,p.product_id, sum(od.quantity) as jami_zakaz from products p
# -- join order_details od on p.product_id = od.product_id
# -- group by p.product_id,p.product_name,p.unit_price
# -- having sum(od.quantity) > 500 and p.unit_price < 20
# -- order by jami_zakaz desc
#
# -- 8-misol
# -- Londonda yashovchi va zakazlar soni kam bo`lgan kompaniyalar soni chiqarilsin
#
# -- select count(*) as kompaniyalar_soni
# -- from (select c.customer_id from customers c
# -- left join orders o on c.customer_id = o.customer_id
# -- where c.city = 'London'
# -- group by c.customer_id
# -- having count(o.order_id) < 5)
#
# -- 9-misol
# -- Har bir kategoriya bo`yicha eng qimmat maxsulotni chop etuvchi so`rov yozing (products va
# -- categories)
#
# -- select c.category_name,p.product_name,p.unit_price from products p
# -- join categories c on p.category_id = c.category_id
# -- where p.unit_price = (select max(p2.unit_price)from products p2
# -- where p2.category_id = p.category_id)
# -- order by c.category_name
#
# -- 10-misol
# -- Eng ko`p buyurtma qilgan 10ta haridorni chop etuvchi so`rov yozing (Customers va Orders)
#
# -- select c.customer_id,c.company_name,count(o.order_id) as jami_zakaz from customers c
# -- join orders o on c.customer_id = o.customer_id
# -- group by c.customer_id,c.company_name
# -- order by jami_zakaz desc














# -- 3-misol
# -- Qaysi yilda eng ko`p zakaz qilingan mahsulot va sakaz qilgan kompaniya haqida ma’lumot.
#
# -- select p.product_name,to_char(order_date,'yyyy'),c.company_name,count(o.order_id) from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- inner join customers c on c.customer_id=o.customer_id
# -- group by p.product_name,to_char(o.order_date,'yyyy'),c.company_name
# -- having count(o.order_id)=(select count(o.order_id)from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- inner join customers c on c.customer_id=o.customer_id
# -- group by p.product_name, to_char(o.order_date,'yyyy'),c.company_name
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id) desc
#
# -- 4-misol
# -- Eng ko`p zakaz qilgan va eng minimal narxdagi mahsulot va zakaz qilgan kompaniya haqida
# -- ma`lumot
#
# -- select p.product_name, to_char(order_date,'yyyy'),c.company_name,count(o.order_id) from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- inner join customers c on c.customer_id=o.customer_id
# -- where p.product_id=(select product_id from products
# -- where unit_price=(select min(unit_price)from products))
# -- group by p.product_name,to_char(o.order_date,'yyyy'),c.company_name
# -- having count(o.order_id)=(select count(o.order_id) from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- inner join customers c on c.customer_id=o.customer_id
# -- where p.product_id=(select product_id from products
# -- where unit_price=(select min(unit_price)from products))
# -- group by p.product_name,to_char(o.order_date,'yyyy'),c.company_name
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id) desc
#
# -- 6-misol
# -- Amerikada yashovchi eng faol hodimlar haqida ma`lumot shakllantiring
#
# -- select e.employee_id,e.country,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- having count(o.order_id)=(select count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id,e.first_name,e.last_name,e.country
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id) desc
#
# -- 7-misol
# -- Qaysi davlatdagi hodimlar eng faol ishlashi haqidagi hisobot shakllantiring
#
# -- select e.country, count(order_id) from employees as e
# -- inner join orders o on o.employee_id=e.employee_id
# -- group by e.country
# -- having count (o.order_id)=(select count(o.order_id) from employees as e
# -- inner join orders o on o.employee_id=e.emloyee_id
# -- group by e.country order by e.count desc limit 1)
#
# -- 10-misol
# -- 1-kategoriyadagi eng qimmat sotilgan 10ta mahsulot kim tomonidan zakaz qilinganligi va qaysi
# -- kompaniya tomonidan yetkazib berilganligi haqida ma`lumot

