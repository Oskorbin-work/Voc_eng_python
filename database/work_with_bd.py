# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import random
import sqlite3
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from database.functions_for_bd import (
    request_bd_update, request_bd_select
)
from settings import ROOT_MAIN_DB


# Class to work with bd
class Work_with_bd:
    # Sorting rows in the database
    def order_main_table(self):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()
            # Order rows
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
                        "work_count_life ,"
                        "english_word ")
            # Get all rows
            all_row = [[str(j) for j in i] for i in cur.fetchall()]
            # Clear table main_table
            cur.execute(f"DELETE FROM main_table;")
            # Add ordering rows in main_table
            for i in range(len(all_row)):
                string = f"'{i+1}', '" + "', '".join(all_row[i]) + "'"
                cur.execute( f"INSERT INTO main_table VALUES ({string});")
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical("Not working sql:", self.order_main_table().__name__)

    # Add work count life
    def add_work_count_life(self):
        # Get count all word
        count_row = self.get_count_all_word()[0]
        # Copy column count life in column work count life
        for i in range(1, count_row+1):
            count_life = self.get_row(i)[6]
            # if word is old then his life is "-1". It is mean what word was learned
            if count_life == -1 and random.random() <= settings.RANDOM_OLD_WORD:
                count_life = 1
            # add count life.
            self.edit_work_count_life(i, str(count_life))

    # edit work_count_life.
    # Uses for copy values from count_life in work_count_life
    # Uses for update value work_count_life while user has doing wrong
    @request_bd_update
    def edit_work_count_life(self, id_row, count_life):
        return f'update Main_table set work_count_life = {count_life} where id_main = {id_row};'

    # get rows from database
    @request_bd_select
    def get_row(self, random_id):
        return f'select * from Main_table where id_main = {random_id};'

    # get count rows from database
    @request_bd_select
    def get_count_all_word(self):
        return "select COUNT(*) from Main_table"

    # get count row " Проверенные" from database
    @request_bd_select
    def get_count_true_world(self):
        return "select COUNT(*) from Main_table where work_count_life =0"

    # get count row " Непроверенные" from database
    @request_bd_select
    def get_count_false_world(self):
        return "select COUNT(*) from Main_table where work_count_life >0"

    # get first id word where default count life == 3
    @request_bd_select
    def get_first_id_count_life_3(self):
        return "select id_main from Main_table where work_count_life >0"

    # get count row " Старые слова" from database
    @request_bd_select
    def get_count_change_world(self):
        return "select COUNT(*) from Main_table where work_count_life =-1"
