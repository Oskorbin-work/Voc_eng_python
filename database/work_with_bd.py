import sqlite3

from settings import ROOT_DIR

# Class to work with bd
class Work_with_bd:

    # get row from database
    def get_row(self, random_id):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute("select * from Main_table where id_main  = %d;"% random_id)
        value = (cur.fetchall())[0]
        conn.close()
        return value

    # get count row from database
    def get_count_all_word(self):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute("select COUNT(*) from Main_table")
        value = ((cur.fetchall())[0])[0]
        conn.close()
        return value

    # get count row " Проверенные" from database
    def get_count_true_world(self):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute("select COUNT(*) from Main_table where count_life =0")
        value = ((cur.fetchall())[0])[0]
        conn.close()
        return value

    # get count row " Непроверенные" from database
    def get_count_false_world(self):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute("select COUNT(*) from Main_table where count_life =3")
        value = ((cur.fetchall())[0])[0]
        conn.close()
        return value

    # get count row " Проверенные но с шансом на проверку" from database
    def get_count_change_world(self):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute("select COUNT(*) from Main_table where count_life =-1")
        value = ((cur.fetchall())[0])[0]
        conn.close()
        return value
