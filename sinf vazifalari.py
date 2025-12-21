# # # -- create table categories (
# # # -- category_id integer primary key,
# # # -- catergory_name varchar not null,
# # # -- description text,
# # # -- picture bytea
# # # -- );
# # # -- create table products (
# # # -- product_id integer primary key,
# # # -- product_name varchar(50) not null,
# # # -- supplier_id integer,
# # # -- category_id integer,
# # # -- quantity_per_unit varchar(50) not null,
# # # -- unit_price numeric(10,4),
# # # -- unit_in_stock smallint,
# # # -- unit_in_order smallint,
# # # -- reorder_level smallint,
# # # -- discontinued boolean null default False,
# # # -- foreign key(supplier_id) references suppliers(supplier_id),
# # # -- foreign key(category_id) references categories(category_id)
# # # -- );
# # # -- create table suppliers(
# # # -- supplier_id integer primary key,
# # # -- company_name varchar(50) not null,
# # # -- contact_name varchar(50) not null,
# # # -- contact_title varchar(50) not null,
# # # -- address varchar(50) not null,
# # # -- city varchar(50) not null,
# # # -- region varchar(50) not null,
# # # -- postal_code varchar(50) not null,
# # # -- country varchar(50) not null,
# # # -- phone varchar(20) not null,
# # # -- fax varchar(50) not null,
# # # -- homepage text
# # # -- );
# # # -- create table orders(
# # # -- order_id integer primary key,
# # # -- order_date date,
# # # -- required_date date,
# # # -- shipped_date date,
# # # -- ship_name varchar(50) not null,
# # # -- ship_adress varchar(50) not null,
# # # -- ship_city varchar(50) not null,
# # # -- ship_region varchar(50) not null,
# # # -- ship_country varchar(50) not null
# # # -- );
# # # -- create table order_date(
# # # -- order_id integer primary key,
# # # -- product_id integer,
# # # -- unit_price numeric(10,4),
# # # -- quantity varchar(50),
# # # -- discount varchar(50),
# # # -- foreign key(order_id) references orders(order_id),
# # # -- foreign key(product_id) references products(product_id)
# # # -- );
# # #
# # # 1-misol
# # # -- select * from products
# # # -- where category_id=3 and unit_price=(select min(unit_price) from products where category_id=3)
# # #
# # # 2-misol
# # # -- select * from orders
# # # -- where to_char(order_date,'YYYY-MM')='1996-07' and shipped_date>required_date
# # #
# # # 3-misol
# # # -- SELECT *
# # # -- FROM categories
# # # -- WHERE EXISTS (
# # # --     SELECT *
# # # --     FROM products
# # # --     WHERE products.category_id = categories.category_id
# # # -- );
# # #
# # # 4-misol
# # # -- select *
# # # -- from categories
# # # -- where category_id between 2 and 6
# # # --  and unit_pr
# # # -- select to_char(order_date,'YYYY-MM'),count(distinct o.order_id) from orders o
# # # -- join order_details od on o.order_id=od.order_id
# # # -- join products p on p.product_id=od.product_id
# # # -- where p.category_id=1 and od.unit_price>10 and to_char(o.order_date,'YYYY')='1996'
# # # -- group by to_char(order_date,'YYYY-MM')
# # #
# # # -- select p.product_name,e.first_name,o.shipped_date from products p
# # # -- join order_details od on p.product_id=od.product_id
# # # -- join orders o on od.order_id=o.order_id
# # # -- join employees e on o.employee_id=e.employee_id
# # # -- where p.category_id=3 and p.unit_price=(select min(unit_price) from products where category_id=3) and to_char(shipped_date,'YYYY-MM')='1997-08';
# # #
# # # -- select e.first_name,count(o.order_id) from orders o
# # # -- join employees e on e.employee_id= o.employee_id
# # # -- where to_char(shipped_date,'YYYY-MM')='1998-03'
# # # -- group by e.first_name
# # #
# # # -- select product_name,category_id,od.unit_price,count(o.order_id) from products p
# # # -- join order_details od on p.product_id=od.product_id
# # # -- join orders o on od.order_id=o.order_id
# # # -- where p.unit_price=(select max(unit_price) from products) and to_char(order_date,'YYYY')='1996'
# # # -- group by p.product_name,p.category_id,od.unit_price;
# # #
# # # -- select e.first_name,count(o.order_id) from orders o
# # # -- join employees e on e.employee_id=o.employee_id
# # # -- join customers c on o.customer_id=c.customer_id
# # # -- where e.country in('USA') and c.country in('USA')
# # # -- group by e.first_name
# # #
# # # -- select e.first_name,count(o.order_id) from products p
# # # -- join order_details od on p.product_id=od.product_id
# # # -- join orders o on o.order_id=od.order_id
# # # -- join employees e on o.employee_id=e.employee_id
# # # -- where to_char(order_date,'YYYY')='1997' and p.category_id=5
# # # -- group by e.first_name
# # #
# # # -- select c.contact_name,count(o.order_id) from customers c
# # # -- join orders o on c.customer_id=o.customer_id
# # # -- where to_char(order_date,'YYYY')='1997'
# # # -- group by c.contact_name
# #
# # -- SELECT
# # --     to_char(o.order_date, 'MM') AS oy,
# # --     COUNT(DISTINCT o.order_id) AS zakas_soni
# # -- FROM orders o
# # -- JOIN order_details od ON o.order_id = od.order_id
# # -- JOIN products p ON od.product_id = p.product_id
# # -- WHERE
# # --     p.category_id = 1
# # --     AND p.unit_price > 10
# # --     AND to_char(o.order_date, 'YYYY') = '1996'
# # -- GROUP BY oy
# # -- ORDER BY oy;
# #
# # -- SELECT
# # --     s.company_name
# # -- FROM suppliers s
# # -- JOIN products p ON s.supplier_id = p.supplier_id
# # -- JOIN order_details od ON p.product_id = od.product_id
# # -- JOIN orders o ON od.order_id = o.order_id
# # -- WHERE
# # --     p.category_id = 3
# # --     AND p.unit_price = (
# #--         SELECT MIN(unit_price)
# #- -         FROM products WHERE category_id = 3
# #               - -     )
# # --     AND to_char(o.order_date, 'YYYY-MM') = '1997-07'
# # -- GROUP BY s.company_name;
# #
# # -- SELECT
# # --     e.first_name,
# # --     e.last_name
# # -- FROM employees e
# # -- JOIN orders o ON e.employee_id = o.employee_id
# # -- WHERE to_char(o.order_date, 'YYYY-MM') = '1998-03'
# # -- GROUP BY e.first_name, e.last_name;
# #
# # -- SELECT
# # --     c.category_name,
# # --     p.product_name,
# # --     SUM(od.quantity) AS sotilgan_soni
# # -- FROM categories c
# # -- JOIN products p ON c.category_id = p.category_id
# # -- JOIN order_details od ON p.product_id = od.product_id
# # -- JOIN orders o ON od.order_id = o.order_id
# # -- WHERE
# # --     to_char(o.order_date, 'YYYY') = '1996'
# # --     AND p.unit_price = (
# # --         SELECT MAX(p2.unit_price)
# #- -         FROM products p2
# # - -         WHERE p2.category_id = p.category_id
# #                  - -     )
# # -- GROUP BY c.category_name, p.product_name;
# #
# # -- SELECT
# # --     s.company_name
# # -- FROM suppliers s
# # -- JOIN products p ON s.supplier_id = p.supplier_id
# # -- JOIN order_details od ON p.product_id = od.product_id
# # -- JOIN orders o ON od.order_id = o.order_id
# # -- JOIN customers c ON o.customer_id = c.customer_id
# # -- WHERE
# # --     s.country = 'USA'
# # --     AND c.country = 'USA'
# # --     AND to_char(o.order_date, 'YYYY') = '1997'
# # -- GROUP BY s.company_name;
# #
# # -- SELECT
# # --     e.first_name,
# # --     e.last_name
# # -- FROM employees e
# # -- JOIN orders o ON e.employee_id = o.employee_id
# # -- JOIN order_details od ON o.order_id = od.order_id
# # -- JOIN products p ON od.product_id = p.product_id
# # -- WHERE
# # --     p.category_id = 5
# # --     AND to_char(o.order_date, 'YYYY') = '1997'
# # -- GROUP BY e.first_name, e.last_name;
# #
# # -- SELECT
# # --     c.city,
# # --     to_char(o.order_date, 'MM')AS oy,
# # --     COUNT(o.order_id)AS zakas_soni
# # -- FROM customers c
# # -- JOIN orders o ON c.customer_id = o.customer_id
# # -- WHERE
# # --     c.country = 'USA'
# # --     AND to_char(o.order_date, 'YYYY') = '1997'
# # -- GROUP BY c.city, oy
# # -- ORDER BY c.city, oy;
# #
#
#
#
#
#
#
# # -- select c.category_name, count(p.product_name)from products p
# # -- right join categories c on p.category_id = c.category_id
# # -- group by c.category_name
# #
# # -- 1 - misol
# # -- amerikaning har bir citysi har bir yilga qanchadan zakaz olgan
# #
# # -- select c.city, to_char(o.order_date, 'yyyy'), count(o.order_id)from orders o
# # -- inner join customers c on c.customer_id = o.customer_id
# # -- where c.country = 'USA'
# # -- group by c.city, to_char(o.order_date, 'yyyy')
# # -- order by c.city
# #
# # -- 2 - misol
# # -- 8chi categoriyadagi mahsulotlar amerikaga qancha zakaz tushgan
# #
# # -- select to_char(order_date, 'YYYY-MM'), count(*) from products p
# # -- inner join order_details od on od.product_id = p.product_id
# # -- inner join categories c on c.category_id = p.category_id
# # -- inner join suppliers s on s.supplier_id = p.supplier_id
# # -- inner join orders o on o.order_id = od.order_id
# # -- where to_char(order_date, 'YYYY') = '1996' and s.country = 'USA'
# # -- group by to_char(order_date, 'YYYY-MM')
# #
# # -- 3 - misol
# # -- har bir xodim har bir oyda nechta zakaz taxlagan
# #
# # -- select e.last_name, to_char(order_date, 'yyyy-mm'), count(o.order_id) from orders o
# # -- inner join employees e on e.employee_id = o.employee_id
# # -- where to_char(order_date, 'yyyy') = '1996'
# # -- group by to_char(order_date, 'yyyy-mm'), e.last_name
# # -- select name, salary from employees
# # -- where salary = any(5000, 6000, 7000)
# # -- select max(unit_price)from products p
# # -- group by category_id
# #
# # -- select * from products
# # -- where unit_price = any(select max(unit_price) from products p
# # -- group by category_id)
# #
# # -- select * from products
# # -- where unit_price < all(select max(unit_price) from products p
# # -- group by category_id)
# #
# # -- select c.company_name, s.company_name, p.unit_price from products p
# # -- inner join suppliers s on s.supplier_id = p.supplier_id
# # -- inner join order_details od on od.product_id = p.product_id
# # -- inner join orders o on od.order_id = o.order_id
# # -- inner join customers c on c.customer_id = o.customer_id
# # -- where p.unit_price = any(select max(unit_price) from products
# # -- group by category_id, c.company_name, s.company_name)
# #
# # -- 1 - vazifa
# # -- 1996 - yilning iyul oyida zakaz qilingan mahsulotlar va qaysi kompaniya tomonidan yetkazib berilganligi haqida ma`lumot(Order Details, Orders, Products, Supplier)
# #
# # -- select o.order_id, o.order_date, p.product_name, s.company_name as supplier from orders o
# # -- join order_details od on o.order_id = od.order_id
# # -- join products p on od.product_id = p.product_id
# # -- join suppliers s on p.supplier_id = s.supplier_id
# # -- where o.order_date between '1996-07-01' and '1996-07-31'
# #
# # -- 2 - misol
# # -- Bitta shaharda yashovchi ham haridori ham ishchisi mavjud shaharlar ro`yxatini topuvchi so`rov yozing(Employees va Customers)
# # -- select distinct e.city from employees e
# # -- inner join customers c on e.city = c.city
# # -- group by e.city
# #
# # -- 3 - misol
# # -- Qaysi yilda eng ko`p zakaz qilingan mahsulot va sakaz qilgan kompaniya haqida ma’lumot
# #
# # select c.company_name, p.product_name, count(o.order_id) as orders from orders o
# # inner join customers c on o.customer_id = c.customer_id
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# -- 12-misol
# -- Londonda yashovchi va zakazlar soni kam bo`lgan kompaniyalar soni chiqarilsin
#
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
#
#
# -- 18-misol
# -- Buyurtmalar soni 50tadan kam bo`lgan ishchilar haqida ma`lumotni topuvchi so`rov yozing
# -- (Employees va Orders)
#
# -- select e.first_name, e.last_name, count(o.order_id) from employees e
# -- inner join orders o on e.employee_id=o.employee_id
# -- group by e.first_name, e.last_name
# -- having 50>count(o.order_id)
# -- order by count(o.order_id)
#
# -- 19-misol
# -- Har bir yil bo`yicha buyurtmalar sonini chop eting (Oraliq nazoratdan)
#
# -- select  to_char(order_date,'yyyy'), count(order_id) from orders
# -- group by to_char(order_date,'yyyy')
#
# -- 20-misol
# -- 1997-yil may oyida eng ko`p buyurtma qabul qilingan beshta kunni chop eting (Oraliq
# -- nazoratdan)
#
# -- select to_char(order_date,'dd'),count(order_id) from orders
# -- where to_char(order_date,'yyyy-mm')='1997-05'
# -- group by to_char(order_date,'dd')
# -- order by count(order_date) desc limit 5
#
# -- 21-misol
# -- 1996-yili qaysi oyida eng ko’p mahsulot zakaz qilinganligini aniqlab beruvchi so’rov
# -- shakllantiring
#
# -- select to_char(order_date,'yyyy-mm'),count(order_id) from orders
# -- where to_char(order_date,'yyyy')='1996'
# -- group by to_char(order_date,'yyyy-mm')
# -- order by count(order_id) desc
#
# -- 23-misol
# -- Vaqtida yetkazib berilgan mahsulotlarni qancha muddatda yetkazilganligi va kim tomonidan
# -- yetkazilganligi haqida ma’lumotni shakllantiring
#
# -- select p.product_name, s.company_name, (o.shipped_date-o.order_date) from suppliers s
# -- inner join products p on p.supplier_id=s.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on od.order_id=o.order_id
# -- where o.shipped_date<=o.required_date
#
# -- 24-misol
# -- Ikki va undan ortiq buyurtma bergan haridorlar soni top 50tasini chiqarish
#
# -- select c.company_name, count(o.order_id) from customers c
# -- inner join orders o on o.customer_id=c.customer_id
# -- group by c.company_name
# -- having count>=2
# -- order by count(o.order_id) desc limit 50
#
# -- 25-misol
# -- Har bir davlatdan nechta hodim borligini aniqlash so`rovini tuzish
#
# -- select country, count(employee_id) from employees
# -- group by country
#
# -- 26-misol
# -- 5 tadan ko’p buyurtmani o’z vaqtida yetkazib bermagan hodimlar ro’yxatini chop eting
#
#
#
#
#
#
# -- select company_name from suppliers
# -- union
# -- select customer_id from customers
#
# -- select c1 ,cast(c2 as varchar) from t1
# -- union
# -- select c1,c2 from t2
#
# -- select country from customers
# -- intersect
# -- select country from employees