# -- create table categories (
# -- category_id integer primary key,
# -- catergory_name varchar not null,
# -- description text,
# -- picture bytea
# -- );
# -- create table products (
# -- product_id integer primary key,
# -- product_name varchar(50) not null,
# -- supplier_id integer,
# -- category_id integer,
# -- quantity_per_unit varchar(50) not null,
# -- unit_price numeric(10,4),
# -- unit_in_stock smallint,
# -- unit_in_order smallint,
# -- reorder_level smallint,
# -- discontinued boolean null default False,
# -- foreign key(supplier_id) references suppliers(supplier_id),
# -- foreign key(category_id) references categories(category_id)
# -- );
# -- create table suppliers(
# -- supplier_id integer primary key,
# -- company_name varchar(50) not null,
# -- contact_name varchar(50) not null,
# -- contact_title varchar(50) not null,
# -- address varchar(50) not null,
# -- city varchar(50) not null,
# -- region varchar(50) not null,
# -- postal_code varchar(50) not null,
# -- country varchar(50) not null,
# -- phone varchar(20) not null,
# -- fax varchar(50) not null,
# -- homepage text
# -- );
# -- create table orders(
# -- order_id integer primary key,
# -- order_date date,
# -- required_date date,
# -- shipped_date date,
# -- ship_name varchar(50) not null,
# -- ship_adress varchar(50) not null,
# -- ship_city varchar(50) not null,
# -- ship_region varchar(50) not null,
# -- ship_country varchar(50) not null
# -- );
# -- create table order_date(
# -- order_id integer primary key,
# -- product_id integer,
# -- unit_price numeric(10,4),
# -- quantity varchar(50),
# -- discount varchar(50),
# -- foreign key(order_id) references orders(order_id),
# -- foreign key(product_id) references products(product_id)
# -- );
#
# 1-misol
# -- select * from products
# -- where category_id=3 and unit_price=(select min(unit_price) from products where category_id=3)
#
# 2-misol
# -- select * from orders
# -- where to_char(order_date,'YYYY-MM')='1996-07' and shipped_date>required_date
#
# 3-misol
# -- SELECT *
# -- FROM categories
# -- WHERE EXISTS (
# --     SELECT *
# --     FROM products
# --     WHERE products.category_id = categories.category_id
# -- );
#
# 4-misol
# -- select *
# -- from categories
# -- where category_id between 2 and 6
# --  and unit_pr
# -- select to_char(order_date,'YYYY-MM'),count(distinct o.order_id) from orders o
# -- join order_details od on o.order_id=od.order_id
# -- join products p on p.product_id=od.product_id
# -- where p.category_id=1 and od.unit_price>10 and to_char(o.order_date,'YYYY')='1996'
# -- group by to_char(order_date,'YYYY-MM')
#
# -- select p.product_name,e.first_name,o.shipped_date from products p
# -- join order_details od on p.product_id=od.product_id
# -- join orders o on od.order_id=o.order_id
# -- join employees e on o.employee_id=e.employee_id
# -- where p.category_id=3 and p.unit_price=(select min(unit_price) from products where category_id=3) and to_char(shipped_date,'YYYY-MM')='1997-08';
#
# -- select e.first_name,count(o.order_id) from orders o
# -- join employees e on e.employee_id= o.employee_id
# -- where to_char(shipped_date,'YYYY-MM')='1998-03'
# -- group by e.first_name
#
# -- select product_name,category_id,od.unit_price,count(o.order_id) from products p
# -- join order_details od on p.product_id=od.product_id
# -- join orders o on od.order_id=o.order_id
# -- where p.unit_price=(select max(unit_price) from products) and to_char(order_date,'YYYY')='1996'
# -- group by p.product_name,p.category_id,od.unit_price;
#
# -- select e.first_name,count(o.order_id) from orders o
# -- join employees e on e.employee_id=o.employee_id
# -- join customers c on o.customer_id=c.customer_id
# -- where e.country in('USA') and c.country in('USA')
# -- group by e.first_name
#
# -- select e.first_name,count(o.order_id) from products p
# -- join order_details od on p.product_id=od.product_id
# -- join orders o on o.order_id=od.order_id
# -- join employees e on o.employee_id=e.employee_id
# -- where to_char(order_date,'YYYY')='1997' and p.category_id=5
# -- group by e.first_name
#
# -- select c.contact_name,count(o.order_id) from customers c
# -- join orders o on c.customer_id=o.customer_id
# -- where to_char(order_date,'YYYY')='1997'
# -- group by c.contact_name