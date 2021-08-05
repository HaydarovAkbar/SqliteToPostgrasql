import sqlite3

DATABASE = "categories.db"


class Magazin_SQL:
    def select_products(self):
        """ SQL dagi products tableni barcha malumotlarini olishda foydalanamiz"""
        try:
            connation = sqlite3.connect(DATABASE)
            cursor = connation.cursor()
            cursor.execute(f"SELECT * FROM products")
            return cursor.fetchall()  # Natija list ko'rinishida qaytadi
        except Exception as e:
            return f"siz nimadadir xatoga yo'l quydingiz -> {e}"

    def select_costumers_data(self):
        """SQL dagi costomersni ruyxatini qayataradigan funksiya"""
        connation = sqlite3.connect(DATABASE)
        cursor = connation.cursor()
        cursor.execute("SELECT * FROM customers")
        return cursor.fetchall()  ## Natija list ko'rinishda qaytadi

    def select_catigories(self):
        """SQL dagi barcha categoriesni olishda foydalanamiz"""
        connation = sqlite3.connect(DATABASE)
        cursor = connation.cursor()
        cursor.execute("SELECT * FROM catigories")
        ## shu listga narxlarni kiritib olamiz
        return cursor.fetchall()

    def select_buy_list(self):
        """SQL dagi barcha buy_listdagi malumotlarni chiqarishda foydalanamiz """
        connation = sqlite3.connect(DATABASE)
        cursor = connation.cursor()
        cursor.execute("SELECT * FROM buy_list")
        ## barcha mahsulotlarni for bilan listga kiritib boramiz
        return cursor.fetchall()

    def select_sqlite_s(self):
        """SQL dagi barcha buy_listdagi malumotlarni chiqarishda foydalanamiz """
        connation = sqlite3.connect(DATABASE)
        cursor = connation.cursor()
        cursor.execute("SELECT name,seq FROM sqlite_sequence")
        ## barcha mahsulotlarni for bilan listga kiritib boramiz
        return cursor.fetchall()

    def del_data(self):
        """SQL dagi buy_listni ruyxatini uchrishda foydalanamiz """
        connation = sqlite3.connect(DATABASE)
        cursor = connation.cursor()
        cursor.execute("DELETE FROM buy_list")
        connation.commit()
        connation.close()
if __name__ == '__main__':
    m = Magazin_SQL()
    print(m.select_buy_list())