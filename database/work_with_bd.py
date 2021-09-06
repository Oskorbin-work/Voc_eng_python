import sqlite3

from settings import ROOT_DIR


def request_bd(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        cur.execute(func(*args, **kwargs))
        value = (cur.fetchall())[0]
        conn.close()
        return value
    return wrapper


# Class to work with bd
class Work_with_bd:

    # get row from database
    @request_bd
    def get_row(self, random_id):
        return f'select * from Main_table where id_main = {random_id};'

    # get count row from database
    @request_bd
    def get_count_all_word(self):
        return "select COUNT(*) from Main_table"

    # get count row " Проверенные" from database
    @request_bd
    def get_count_true_world(self):
        return "select COUNT(*) from Main_table where count_life =0"

    # get count row " Непроверенные" from database
    @request_bd
    def get_count_false_world(self):
        return "select COUNT(*) from Main_table where count_life =3"

    # get count row " Проверенные но с шансом на проверку" from database
    @request_bd
    def get_count_change_world(self):
        return "select COUNT(*) from Main_table where count_life =-1"
