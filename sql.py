# import psycopg2
# conn = psycopg2.connect(
#     dbname="n75",
#     user="nargiza75",
#     password="123",
#     host="localhost", #127.0.0.1
#     port="5432"
# )
# cur = conn.cursor()
# sql1 = '''
# select * from teacher
# '''
#
# s2 = '''
# CREATE TABLE teacher (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     phone VARCHAR(20),
#     email VARCHAR(100) UNIQUE
# );
#
# '''
# s3='''
# INSERT INTO teacher (name, phone, email)
# VALUES
# ('Ali Karimov', '+998901234567', 'ali.karimov@example.com'),
# ('Dilnoza Rahimova', '+998933334455', 'dilnoza.rahimova@example.com'),
# ('Jasur Tursunov', '+998907778899', 'jasur.tursunov@example.com'),
# ('Malika Xudoyberdiyeva', '+998935551122', 'malika.xudoyberdiyeva@example.com');
#
# '''
# # Malumot qo‘shish
#
# cur.execute(sql1)
# s = cur.fetchall()
# print(s)
# for item in s:
#     print(item[0],item[1])
#
# conn.commit()
# cur.close()
# conn.close()