# -- CREATE TABLE IF NOT EXISTS users (
# --     id SERIAL PRIMARY KEY,
# --     full_name VARCHAR(100) NOT NULL,
# --     email VARCHAR(100) NOT NULL,
# --     password TEXT,
# --     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# -- )
#
#
# -- create table if not exists books (
# -- book_id SERIAL primary key,
# -- title VARCHAR(150) not null,
# -- author_id INTEGER references authors(author_id) ,
# -- description TEXT,
# -- published_year INTEGER ,
# -- genre_id INTEGER references genres(genre_id),
# -- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# -- )
#
#
# -- create table if not exists authors (
# -- author_id SERIAL primary key,
# -- full_name VARCHAR(100),
# -- country VARCHAR(100)
# -- )
#
# -- create table if not exists genres (
# -- genre_id SERIAL primary key,
# -- name VARCHAR(50)
# -- )
#
# -- create table if not exists comments(
# -- id SERIAL primary key,
# -- user_id INTEGER references users(id) ,
# -- book_id INTEGER references books(book_id),
# -- content TEXT,
# -- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# -- )
#
# -- INSERT INTO users (id,full_name,email,password,created_at) VALUES
# -- ('1', 'malika', 'malika@gmail.com','malikaa', '2026-12-31'),
# -- ('2', 'ali', 'ali@gmail.com','alii', '2027-06-30')
#
# -- INSERT INTO books (book_id,title,author_id,description,published_year,genre_id,created_at) VALUES
# -- ('1', 'ktioblar olami', 'malika','umumiy kitob haqida','komediya', '2026-12-15','2027-06-18'),
# -- ('2', 'dunyo tarixi', 'ali','dunyoning tarixi haqida','detektiv', '2027-06-12','2027-06-25')
#
# -- INSERT INTO authors (author_id,full_name,country) VALUES
# -- ('1', 'malika','uzbekistan'),
# -- ('2', 'ali', 'uzbekistan')
#
# -- INSERT INTO genres (genre_id,name) values
# -- ('1','malika'),
# -- ('2','ali')
#
# -- INSERT INTO comments (user_id,book_id,content,created_at) values
# -- ('1','1','nnnn','2026-12-31'),
# -- ('2','2','mmm','2027-06-30')
#
#
#
#
# -- a variant
# -- 1.Chiqarilgan yili bo‘yicha kitoblarni tartiblash
# -- select * from books order by created_at;
#
# -- 2. Har bir janr bo‘yicha nechta kitob borligini chiqaring
# -- select name, count(books.genre_id) from genres
# -- inner join books on books.genre_id = genres.genre_id
# -- group by books.genre_id, name;
#
# -- 3. .Comment yozilmagan kitoblarni chiqaring
# -- select books.title from books
# -- inner join comments on comments.book_id=books.book_id
# -- where comments.book_id is null
#
# -- 4.Eng ko‘p komment yozilgan 5 ta kitobni chiqaring
# -- select books.title,count(id) from books
# -- inner join comments on comments.book_id=books.book_id
# -- group by books.title,count(comment_id)
# -- having count(id)=(select count(id) from books
# -- inner join comments on comments.book_id=books.book_id
# -- group by books.title,count(id)
# -- order by count(id) desc limit 5)
