# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sqlite3
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.functions_for_bd import (
    request_bd_update, request_bd_select
)
from settings import ROOT_MAIN_DB


# Class to work with bd
class Work_with_bd:
    def order_main_table(self):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()

            cur.execute("SELECT "
                        "english_word," 
                        "russian_word,"  
                        "parts_of_speech," 
                        "transcription,"    
                        "definition,"       
                        "count_life,"  
                        "other_information," 
                        "work_count_life "    
                        "FROM Main_table "
                        "Order by "
                        "count_life ,"
                        "english_word ")
            all_row = [[str(j) for j in i] for i in cur.fetchall()]
            for i in range(len(all_row)):
                print(", ".join(all_row[i]))
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical("Not working sql:", self.order_main_table().__name__)

    def add_work_count_life(self):
        count_row = self.get_count_all_word()[0]
        for i in range(1, count_row+1):
            self.edit_work_count_life(i, str(self.get_row(i)[6]))

    # get row from database
    @request_bd_update
    def edit_work_count_life(self, id_row, count_life):
        return f'update Main_table set work_count_life = {count_life} where id_main = {id_row};'

    # get row from database
    @request_bd_select
    def get_row(self, random_id):
        return f'select * from Main_table where id_main = {random_id};'

    # get count row from database
    @request_bd_select
    def get_count_all_word(self):
        return "select COUNT(*) from Main_table"

    # get count row " Проверенные" from database
    @request_bd_select
    def get_count_true_world(self):
        return "select COUNT(*) from Main_table where count_life =0"

    # get count row " Непроверенные" from database
    @request_bd_select
    def get_count_false_world(self):
        return "select COUNT(*) from Main_table where count_life =3"

    # get count row " Проверенные но с шансом на проверку" from database
    @request_bd_select
    def get_count_change_world(self):
        return "select COUNT(*) from Main_table where count_life =-1"
