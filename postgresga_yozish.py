from psycopg2 import connect
HOST = "localhost"
PASS = "akbar2000"
USER = "postgres"
DATABASE = "baza1"


class Magazin_Postgras:
    def creat_table_products(self):
        """bu funksiya orqali products nomli tablitsa yaratamiz"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"CREATE TABLE products(id INTEGER,cat_id INTEGER, name VARCHAR(255), narxlari VARCHAR(255),soni INTEGER)")
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz iltimos yana bir tekshirib ko'ring {e}")

    def creat_table_costomer(self):
        """bu funksiya orqali costomer nomli tablitsa yaratishimiz mumkin """
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"CREATE TABLE costomer (id INTEGER, fname VARCHAR(255), card_num VARCHAR(255),money INTEGER)")
        except Exception as e:
            print(f"Siz adashdingiz {e}")
    def creat_table_catigories(self):
        """bu funksiya orqali catigories nomli tablitsa yaratishimiz mumkin """
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"CREATE TABLE catigories(id INTEGER, name VARCHAR(255))")
        except Exception as e:
            print(f"Siz adashdingiz {e}")
    def creat_table_buy_list(self):
        """bu funksiya orqali buy_list nomli tablitsa yaratishimiz mumkin """
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"CREATE TABLE buy_list(id INTEGER, p_id INTEGER, c_id INTEGER, quantity INTEGER,buy_money INTEGER,data VARCHAR(255))")
        except Exception as e:
            print(f"Siz adashdingiz {e}")
    def creat_table_sqlite_s(self):
        """bu funksiya orqali sqlite_s nomli tablitsa yaratishimiz mumkin """
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"CREATE TABLE sqlite_sequence(name VARCHAR(255), seq INTEGER)")
        except Exception as e:
            print(f"Siz adashdingiz {e}")

    def insert_products(self, item0,item1,item2,item3,item4):
        """Postgresga products ga malumot qushish funksiyasi"""
        # try:
        connation = connect(
                host = HOST,
                user = USER,
                password = PASS,
                database = DATABASE
            )
        connation.autocommit = True
        cursor = connation.cursor()
        cursor.execute(f"INSERT INTO products(id, cat_id, name, narxlari,soni) VALUES({item0},{item1},'{item2}','{item3}',{item4})")
        # except Exception as e:
        #     print(f"Siz qayerdadir adashdingiz ! {e}")
    def insert_buy_list(self, item1,item2,item3,item4,item5):
        """Postgresga buy_listga malumotni qushadigan funksiya"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO buy_list(id,p_id,c_id,quantity,buy_money) VALUES({item1},{item2},{item3},{item4},{item5})")
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz !{e}")
    def insert_catigories(self, item1,item2):
        """Postgresga catigoriesga malumot qushadigan funksiya"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO catigories(id,name) VALUES({item1},'{item2}')")
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz !{e}")
    def insert_customers(self, item0,item1,item3,item4):
        """Postgresga customersga malumotni qushadigan funksiya"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO costomer(id,fname,card_num,money) VALUES({item0},'{item1}',{item3},{item4})")
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz !{e}")
    def insert_sqlite_s(self, item0,item1):
        """Postgresga sqlite_sga malumotni qushadigan funksiya"""
        try:
            connation = connect(
                host=HOST,
                user=USER,
                password=PASS,
                database=DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"INSERT INTO sqlite_sequence(name,seq) VALUES('{item0}',{item1})")
        except Exception as e:
            print(f"Siz qayerdadir adashdingiz !{e}")
    def del_ps(self,id):
        """Postgresdsdagi maluotni uchirish dunksiyasi"""
        try:
            connation = connect(
                host = HOST,
                user = USER,
                password = PASS,
                database = DATABASE
            )
            connation.autocommit = True
            cursor = connation.cursor()
            cursor.execute(f"DELETE FROM products WHERE id = {id}")
        except Exception as e:
            print("Bu bumagan narsa -> ",e)

if __name__ == '__main__':
    m = Magazin_Postgras()
    m.creat_table_buy_list()

