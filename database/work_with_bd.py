# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.functions_for_bd import (
    request_bd_update, request_bd_select
)


# Class to work with bd
class Work_with_bd:
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
