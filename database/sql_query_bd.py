# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import random
import sqlite3
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.functions_for_bd import (
    request_bd_update, request_bd_select, request_bd_insert, request_bd_select_all
)
from functions.notifications import view_error_critical
from settings import (
    ROOT_MAIN_DB, NAME_ACTIVE_TABLE,MAX_OLD_WORD
)
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# Class to work with bd
class WorkWithBd:

    def __init__(self):
        self.count_temp_activate = int(self.get_temp_activate()[0])


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
                        "work_count_life, "  
                        "status_word, "  
                        "count_true_attempt "
                        f"FROM {NAME_ACTIVE_TABLE} "
                        "Order by "
                        "work_count_life ,"
                        "english_word ")
            # Get all rows
            all_row = [[str(j) for j in i] for i in cur.fetchall()]
            # Clear table main_table
            cur.execute(f"DELETE FROM {NAME_ACTIVE_TABLE};")
            # Add ordering rows in main_table
            for i in range(len(all_row)):
                # '1', 'Abandon', 'Покидать', 'verb', 'əˈbændə', 'to leave someone or something somewhere,
                # sometimes not returning to get them', '-1', 'LEAVE', '-1'
                string = f"'{i+1}', '" + "', '".join(all_row[i]) + "'"
                cur.execute(f"INSERT INTO {NAME_ACTIVE_TABLE} VALUES ({string});")
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical(XML.get_attr_XML("error_sector/database/label_not_working_sql"), self.order_main_table().__name__)

    # place for start set up bd data
    def start_set_up(self):
        # Get count all word
        count_row = self.get_count_all_word()[0]
        ls_temp_words = self.get_list_temp_activate()
        # Copy column count life in column work count life
        for i in range(1, count_row+1):
            count_life = self.get_row(i)[6]

            if count_life == -1:
                self.edit_status_word(i, "not_activate")
                # if word is old then his life is "-1". It is mean what word was learned
                if i in ls_temp_words:
                    count_life = 1
                    self.edit_status_word(i, "temp_activate")
            if count_life == 3:
                self.edit_status_word(i, "is_activate")
            # add count life.
            self.edit_work_count_life(i, str(count_life))

    # Forming a list of temporary words
    def get_list_temp_activate(self):
        count_words = int(self.get_count_words(-1)[0])
        ls = list()

        # if setting have error
        count = count_words+1 if MAX_OLD_WORD > count_words else MAX_OLD_WORD

        for i in range(0, count):
            value = random.randint(0, count_words)
            while value in ls:
                value = random.randint(0, count_words)
            ls.append(value)
        return ls

    # all word with status "temp_activate" get
    # status "is_activate" or "not_activate"(Depends on count life).
    def clear_temp_activate(self):
        count_row = self.get_count_all_word()[0]
        for i in range(1, count_row+1):
            count_life = self.get_row(i)[6]
            if count_life == -1:
                self.edit_status_word(i, "not_activate")
            elif count_life == 3:
                self.edit_status_word(i, "is_activate")

    # edit work_count_life.
    # uses for copy values from count_life in work_count_life
    # uses for update value work_count_life while user has doing wrong
    @request_bd_update
    def edit_work_count_life(self, id_row, count_life):
        return f'update {NAME_ACTIVE_TABLE} set work_count_life = {count_life} where id_main = {id_row};'

    # edit count_true_attempt
    @request_bd_update
    def edit_count_true_attempt(self, id_row, count_life):
        # if user wrong translate word
        if count_life == 0:
            return f'update {NAME_ACTIVE_TABLE} set count_true_attempt = 0 where id_main = {id_row};'
        # if user translate word x3 contract
        else:
            return f'update {NAME_ACTIVE_TABLE} set count_true_attempt = count_true_attempt+{count_life} where id_main = {id_row};'

    # edit status_word
    @request_bd_update
    def edit_status_word(self, id_row, status):
        return f'update {NAME_ACTIVE_TABLE} set status_word = "{status}" where id_main = {id_row};'

    # edit count_life
    @request_bd_update
    def edit_count_life(self, id_row, count_life):
        return f'update {NAME_ACTIVE_TABLE} set count_life = {count_life} where id_main = {id_row};'

    # get rows from database
    @request_bd_select
    def get_row(self, random_id):
        return f'select * from {NAME_ACTIVE_TABLE} where id_main = {random_id};'

    # get count rows from database
    @request_bd_select
    def get_count_all_word(self):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE}"

    # get work count row  anyway hp from database
    @request_bd_select
    def get_work_count_words(self, count):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where work_count_life ={count}"

    # get work count row  anyway hp from database
    @request_bd_select
    def get_count_words(self, count):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where count_life ={count}"

    # get count row " Непроверенные" from database
    @request_bd_select
    def get_count_false_world_time(self):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where work_count_life >0  and status_word ='is_activate'"

    # get count row "temp_activate" from database
    @request_bd_select
    def get_temp_activate(self):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where status_word ='temp_activate'"
    # get count row " Непроверенные" from database
    @request_bd_select
    def get_count_false_world(self):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where work_count_life >0"

    # get first id word where default count life == 3
    @request_bd_select
    def get_first_id_count_life_3(self):
        return f"select id_main from {NAME_ACTIVE_TABLE} where work_count_life >0"

    # get count row " Старые слова" from database
    @request_bd_select
    def get_count_change_world(self):
        return f"select COUNT(*) from {NAME_ACTIVE_TABLE} where work_count_life =-1"

    # get first id word where default count life == 3
    @request_bd_select
    def get_work_count_life(self, now_id):
        return f"select work_count_life from {NAME_ACTIVE_TABLE} where id_main = {now_id}"

    # get first id word where default count life == 3
    @request_bd_select
    def get_english_word(self, now_id):
        return f"select english_word from {NAME_ACTIVE_TABLE} where id_main = {now_id}"

    # get status_word
    @request_bd_select
    def get_status_word(self, random_id):
        return f'select status_word from {NAME_ACTIVE_TABLE} where id_main = {random_id};'


    # get count_true_attempt
    @request_bd_select
    def get_count_true_attempt(self, random_id):
        return f'select count_true_attempt from {NAME_ACTIVE_TABLE} where id_main = {random_id};'

    # get status_word
    @request_bd_select_all
    def get_english_word(self, random_id):
        return f'select english_word from {NAME_ACTIVE_TABLE} where id_main = {random_id};'

    # get  all english word
    @request_bd_select_all
    def get_all_english_word(self):
        return f"select english_word from {NAME_ACTIVE_TABLE}"
    # insert row  to database
    @request_bd_insert
    def insert_row(self, list):
        if int(list[5]) == -1:
            status_word = "not_activate"
        else:
            status_word = "is_activate"

        return "INSERT INTO {NAME_ACTIVE_TABLE} (english_word, russian_word, parts_of_speech," \
               " transcription, definition, count_life, " \
               "other_information, work_count_life,status_word,count_true_attempt)" \
               f"VALUES ('{list[0]}', '{list[6]}', '{list[1]}'," \
               f" '{list[2]}', '{list[4]}', '{ int(list[5])}'," \
               f" '{list[3]}', null, '{status_word}', '0');"

