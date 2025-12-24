# -- 1 - masala
# -- 1996 - yilning iyul oyida zakaz qilingan mahsulotlar va qaysi kompaniya tomonidan yetkazib berilganligi haqida ma`lumot(Order Details, Orders, Products, Supplier)
# -- select o.order_id, o.order_date, p.product_name, s.company_name as supplier from orders o
# -- join order_details od on o.order_id = od.order_id
# -- join products p on od.product_id = p.product_id
# -- join suppliers s on p.supplier_id = s.supplier_id
# -- where o.order_date between '1996-07-01' and '1996-07-31'

# -- 2 - misol
# -- Bitta shaharda yashovchi ham haridori ham ishchisi mavjud shaharlar ro`yxatini topuvchi so`rov yozing(Employees va Customers)
# -- select distinct e.city from employees e
# -- inner join customers c on e.city = c.city
# -- group by e.city

# -- 3-misol
# -- Qaysi yilda eng ko`p zakaz qilingan mahsulot va sakaz qilgan kompaniya haqida ma’lumot.
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
# 5-misol
# -- Eng ko`p zakaz qilingan mahsulot turi bo`yicha hisobot shakllantiring
# -- select c.category_name as mahsulot_turi, sum(od.quantity) as jami_zakaz from categories c
# -- inner join products p on c.category_id = p.category_id
# -- inner join order_details od on p.product_id = od.product_id
# -- group by c.category_name
# -- order by jami_zakaz

# -- 6-misol
# -- Amerikada yashovchi eng faol hodimlar haqida ma`lumot shakllantiring
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
# -- select e.country, count(order_id) from employees as e
# -- inner join orders o on o.employee_id=e.employee_id
# -- group by e.country
# -- having count (o.order_id)=(select count(o.order_id) from employees as e
# -- inner join orders o on o.employee_id=e.emloyee_id
# -- group by e.country order by e.count desc limit 1)
#
# -- 8-misol
# -- 1997-yilda eng ko`p summada buyurtma qilgan haridorlar haqida m`lumot
# -- select c.customer_id,c.company_name,sum(od.quantity*od.unit_price*(1-od.discount)) as jami_summa from customers c
# -- join orders o on c.customer_id=o.customer_id
# -- join order_details od on o.order_id=od.order_id
# -- where to_char(order_date,'yyyy')='1997'
# -- group by c.customer_id, c.company_name
# -- order by jami_summa desc
#
# -- 9-misol
# -- Eng kam buyurtma qilingan mahsulotlar
# -- select p.product_id,p.product_name, sum(od.quantity) from products p
# -- join order_details od on od.product_id=od.product_id
# -- group by p.product_id,p.product_name
# -- order by product_id
#
# -- 10-misol
# -- 1-kategoriyadagi eng qimmat sotilgan 10ta mahsulot kim tomonidan zakaz qilinganligi va qaysi
# -- kompaniya tomonidan yetkazib berilganligi haqida ma`lumot
# -- select p.product_name, od.unit_price,c.company_name, s.company_name from products p
# -- join categories cat on p.category_id = cat.category_id
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- join customers c on o.customer_id = c.customer_id
# -- join suppliers s on p.supplier_id = s.supplier_id
# -- where p.category_id = 1
# -- order by od.unit_price desc

# -- 11-misol
# -- Ko`p zakaz qilingan ammo narxi arzon mahsulotlar ro`yxatini shakllantiring
# -- select p.unit_price, p.product_name,p.product_id, sum(od.quantity) as jami_zakaz from products p
# -- join order_details od on p.product_id = od.product_id
# -- group by p.product_id,p.product_name,p.unit_price
# -- having sum(od.quantity) > 500 and p.unit_price < 20
# -- order by jami_zakaz desc

# -- 12-misol
# -- Londonda yashovchi va zakazlar soni kam bo`lgan kompaniyalar soni chiqarilsin
# -- select s.company_name, count(o.order_id) from suppliers s
# -- inner join products p on s.supplier_id=p.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- where s.city='London'
# -- group by s.company_name
# -- having count (o.order_id)=(select count(o.order_id) from suppliers s
# -- inner join products p on s.supplier_id=p.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- where s.city='London'
# -- group by s.company_name
# -- order by count(o.order_id) desc limit 1)

# -- 13-misol
# -- Har bir kategoriya bo`yicha eng qimmat maxsulotni chop etuvchi so`rov yozing (products va
# -- categories)
# -- select c.category_name,p.product_name,p.unit_price from products p
# -- join categories c on p.category_id = c.category_id
# -- where p.unit_price = (select max(p2.unit_price)from products p2
# -- where p2.category_id = p.category_id)
# -- order by c.category_name
#
# -- 14-misol
# -- Eng ko`p buyurtma qilgan 10ta haridorni chop etuvchi so`rov yozing (Customers va Orders)
# -- select c.customer_id,c.company_name,count(o.order_id) as jami_zakaz from customers c
# -- join orders o on c.customer_id = o.customer_id
# -- group by c.customer_id,c.company_name
# -- order by jami_zakaz desc

# -- 15-misol
# -- Eng kam sotilgan 10ta maxsulotni topuvchi so`rov yozing (Products va Order Details)
# -- select p.product_id,od.unit_price,p.product_name from products p
# -- join order_details od on p.product_id=od.product_id
# -- where od.unit_price = (select min(unit_price)from products)
# -- group by p.product_id,od.unit_price,p.product_name
#
# -- 16-misol
# -- 1996-yilda buyurtma qilingan maxsulotlarning umumiy summasini topuvchi so`rov yozing
# -- (Orders va Order Details)
# -- select o.order_id,od.unit_price,sum(od.unit_price * od.quantity * (1 - od.discount)) from order_details od
# -- join orders o on od.order_id=o.order_id
# -- where to_char(order_date,'yyyy')='1996'
# -- group by o.order_id,od.unit_price
#
# -- 17-misol
# -- Eng ko`p summadagi buyurtma qilgan 5ta haridorni topuvchi so`rov yozing (Customers, Orders
# -- va Order Details)
# -- select c.customer_id,o.order_id,sum(od.unit_price * od.quantity * (1 - od.discount)) from order_details od
# -- join orders o on od.order_id=o.order_id
# -- join customers c on o.customer_id=c.customer_id
# -- group by c.customer_id,o.order_id
# -- order by sum desc limit 5
#
# -- 18-misol
# -- Buyurtmalar soni 50tadan kam bo`lgan ishchilar haqida ma`lumotni topuvchi so`rov yozing
# -- (Employees va Orders)
# -- select e.first_name, e.last_name, count(o.order_id) from employees e
# -- inner join orders o on e.employee_id=o.employee_id
# -- group by e.first_name, e.last_name
# -- having 50>count(o.order_id)
# -- order by count(o.order_id)
#
# -- 19-misol
# -- Har bir yil bo`yicha buyurtmalar sonini chop eting (Oraliq nazoratdan)
# -- select  to_char(order_date,'yyyy'), count(order_id) from orders
# -- group by to_char(order_date,'yyyy')
#
# -- 20-misol
# -- 1997-yil may oyida eng ko`p buyurtma qabul qilingan beshta kunni chop eting (Oraliq
# -- nazoratdan)
# -- select to_char(order_date,'dd'),count(order_id) from orders
# -- where to_char(order_date,'yyyy-mm')='1997-05'
# -- group by to_char(order_date,'dd')
# -- order by count(order_date) desc limit 5
#
# -- 21-misol
# -- 1996-yili qaysi oyida eng ko’p mahsulot zakaz qilinganligini aniqlab beruvchi so’rov
# -- shakllantiring
# -- select to_char(order_date,'yyyy-mm'),count(order_id) from orders
# -- where to_char(order_date,'yyyy')='1996'
# -- group by to_char(order_date,'yyyy-mm')
# -- order by count(order_id) desc
#
# -- 22-misol
# -- Eng ko’p buyurtma qabul qilingan 10ta kunni chop etish
# -- select order_date,count(order_id) as buyurtmalar_soni
# -- from orders
# -- group by order_date
# -- order by buyurtmalar_soni desc
# -- limit 10

# -- 23-misol
# -- Vaqtida yetkazib berilgan mahsulotlarni qancha muddatda yetkazilganligi va kim tomonidan
# -- yetkazilganligi haqida ma’lumotni shakllantiring
# -- select p.product_name, s.company_name, (o.shipped_date-o.order_date) from suppliers s
# -- inner join products p on p.supplier_id=s.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on od.order_id=o.order_id
# -- where o.shipped_date<=o.required_date
#
# -- 24-misol
# -- Ikki va undan ortiq buyurtma bergan haridorlar soni top 50tasini chiqarish
# -- select c.company_name, count(o.order_id) from customers c
# -- inner join orders o on o.customer_id=c.customer_id
# -- group by c.company_name
# -- having count>=2
# -- order by count(o.order_id) desc limit 50
#
# -- 25-misol
# -- Har bir davlatdan nechta hodim borligini aniqlash so`rovini tuzish
# -- select country, count(employee_id) from employees
# -- group by country

# -- 26-misol
# -- 5 tadan ko’p buyurtmani o’z vaqtida yetkazib bermagan hodimlar ro’yxatini chop eting
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id)from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where o.shipped_date > o.required_date
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) > 5
#
# -- 27-misol
# -- 10 tadan ko’p sotilgan mahsulotlar va hodimlar haqida ma’lumot
# -- select p.product_id,p.product_name,e.employee_id,e.first_name,e.last_name,sum(od.quantity)from products p
# -- join order_details od on p.product_id = od.product_id
# -- join orders o on od.order_id = o.order_id
# -- join employees e on o.employee_id = e.employee_id
# -- group by p.product_id,p.product_name,e.employee_id,e.first_name, e.last_name
# -- having sum(od.quantity) > 10
#
# -- 28-misol
# -- 20 tadan ortiq mijozga (customer) ega bo’lgan davlatlar ro’yxatini chiqarib beruvchi so’rov
# -- shakllantiring
# -- select country,count(customer_id)from customers
# -- group by country
# -- having count(customer_id) > 20
#
# -- 29-misol
# -- Eng ko’p zakazni amalga oshirgan hodimlar haqida ma’lumot shakllantiring
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) = (select max(soni)from (select count(order_id) as soni from orders
# -- group by employee_id))
#
# -- 30-misol
# -- 3 tadan ko’p buyurtmani o’z vaqtida yetkazib bermagan hodimlar ro’yhatini shakllantiring
# -- select e.employee_id,e.first_name,e.last_name,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where o.shipped_date > o.required_date
# -- group by e.employee_id, e.first_name, e.last_name
# -- having count(o.order_id) > 3
#
# -- 31-misol
# -- Amerikada yashovchi eng faol xodimlar haqida ma'lumot shakllantiring
# -- select e.employee_id,e.first_name,e.last_name,e.country,count(o.order_id) from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country = 'usa'
# -- group by e.employee_id, e.first_name, e.last_name, e.country
# -- having count(o.order_id) = (select max(soni)from (select count(o.order_id)as soni from employees e
# -- join orders o on e.employee_id = o.employee_id
# -- where e.country = 'usa'
# -- group by e.employee_id))