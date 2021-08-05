from s_p_utkazish.postgresga_yozish import Magazin_Postgras as MP
from s_p_utkazish.sql_select import Magazin_SQL as MS

ms = MS()
mp = MP()

class Fors:
    def for_product(self):
        mss = ms.select_products()
        for item in mss:
            mp.insert_products(item[0],item[1],item[2],item[3],item[4])

    def for_costomer(self):
        mss = ms.select_costumers_data()
        for item in mss:
            mp.insert_customers(item[0],item[1],item[2],item[3])

    def for_catigories(self):
        mss = ms.select_catigories()
        for item in mss:
            mp.insert_catigories(item[0],item[1])

    def sqlite_s(self):
        mss = ms.select_sqlite_s()
        for item in mss:
            mp.insert_sqlite_s(item[0],item[1])

    def buy_list(self):
        mss = ms.select_buy_list()
        for i in mss:
            mp.insert_buy_list(i[0],i[1],i[2],i[3])