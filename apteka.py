import psycopg2

class Database:
    def __init__(self):
        self.dbname = "apteka_db"
        self.user = "postgres"
        self.password = "123"
        self.host = "localhost"
        self.port = "5432"

    def get_connection(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

class AptekaManager:
    def __init__(self):
        self.db = Database()
        self.create_table()

    def create_table(self):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS mahsulotlar (
                id SERIAL PRIMARY KEY,
                nomi VARCHAR(200) NOT NULL,
                turi VARCHAR(100) NOT NULL,
                narxi DECIMAL(10,2) NOT NULL CHECK (narxi > 0),
                miqdori INTEGER NOT NULL CHECK (miqdori >= 0),
                ishlab_chiqaruvchi VARCHAR(200),
                amal_qilish_muddati DATE
            )
        ''')
        conn.commit()
        cur.close()
        conn.close()

    # Qo'shish
    def add_product(self, nomi, turi, narxi, miqdori, ishlab_chiqaruvchi, amal_muddati):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO mahsulotlar (nomi, turi, narxi, miqdori, ishlab_chiqaruvchi, amal_qilish_muddati) VALUES (%s,%s,%s,%s,%s,%s)",
            (nomi, turi, narxi, miqdori, ishlab_chiqaruvchi, amal_muddati)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("✓ Mahsulot qo'shildi")

    # Ko'rish
    def view_products(self):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mahsulotlar ORDER BY id")
        products = cur.fetchall()
        cur.close()
        conn.close()
        if not products:
            print("Hozircha mahsulotlar yo'q")
        else:
            print(f"\n{'ID':<5} {'Nomi':<25} {'Turi':<15} {'Narxi':<12} {'Miqdori':<10} {'Ishlab chiqaruvchi':<20}")
            print("=" * 100)
            for p in products:
                print(f"{p[0]:<5} {p[1]:<25} {p[2]:<15} {p[3]:<12} {p[4]:<10} {p[5]:<20}")

    # Tahrirlash
    def update_product(self, product_id, narxi, miqdori):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute(
            "UPDATE mahsulotlar SET narxi=%s, miqdori=%s WHERE id=%s",
            (narxi, miqdori, product_id)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("✓ Mahsulot tahrirlandi")

    # O'chirish
    def delete_product(self, product_id):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM mahsulotlar WHERE id=%s", (product_id,))
        conn.commit()
        cur.close()
        conn.close()
        print("✓ Mahsulot o'chirildi")

    # Qidirish
    def search_product(self, keyword):
        conn = self.db.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM mahsulotlar WHERE nomi ILIKE %s", (f"%{keyword}%",))
        results = cur.fetchall()
        cur.close()
        conn.close()
        if not results:
            print("Mahsulot topilmadi")
        else:
            print(f"\n{'ID':<5} {'Nomi':<25} {'Turi':<15} {'Narxi':<12} {'Miqdori':<10}")
            print("=" * 80)
            for p in results:
                print(f"{p[0]:<5} {p[1]:<25} {p[2]:<15} {p[3]:<12} {p[4]:<10}")

def run_apteka():
    apteka = AptekaManager()
    while True:
        print('''
========================================
        APTEKA BOSHQARUV TIZIMI
========================================
1. Mahsulot qo'shish
2. Mahsulotlarni ko'rish
3. Mahsulot tahrirlash
4. Mahsulot o'chirish
5. Mahsulot qidirish
0. Chiqish
========================================''')
        choice = input("Tanlang (0-5): ")

        if choice == "1":
            nomi = input("Mahsulot nomi: ")
            turi = input("Mahsulot turi (dori/vitamin/asbob): ")
            narxi = float(input("Narxi (so'm): "))
            miqdori = int(input("Miqdori: "))
            ishlab_chiqaruvchi = input("Ishlab chiqaruvchi: ")
            amal_muddati = input("Amal qilish muddati (YYYY-MM-DD): ")
            apteka.add_product(nomi, turi, narxi, miqdori, ishlab_chiqaruvchi, amal_muddati)

        elif choice == "2":
            apteka.view_products()

        elif choice == "3":
            p_id = int(input("Mahsulot ID: "))
            narxi = float(input("Yangi narx: "))
            miqdori = int(input("Yangi miqdor: "))
            apteka.update_product(p_id, narxi, miqdori)

        elif choice == "4":
            p_id = int(input("Mahsulot ID: "))
            tasdiqlash = input("Ishonchingiz komilmi? (ha/yo'q): ")
            if tasdiqlash.lower() == "ha":
                apteka.delete_product(p_id)
            else:
                print("Bekor qilindi")

        elif choice == "5":
            key = input("Qidiruv (mahsulot nomi): ")
            apteka.search_product(key)

        elif choice == "0":
            print("Dasturdan chiqildi. Xayr!")
            break

        else:
            print("✗ Noto'g'ri tanlov! Qaytadan urinib ko'ring.")


run_apteka()