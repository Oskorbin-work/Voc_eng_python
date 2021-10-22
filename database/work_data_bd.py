# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import random
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.sql_query_bd import WorkWithBd
from functions.notifications import view_info_transcription
import settings


# Work with Data Bd
class WorkDataBd(WorkWithBd):

    # def for get random row
    def get_id_row_bd(self):
        try:
            return random.randint(self.get_first_id_count_life_3()[0], self.get_count_all_word()[0])
        except:
            settings.PROGRAM_STATUS = False
            return -1

    # get transcription now word
    def get_info_transcription(self,id_now):
        view_info_transcription(self.get_row(id_now)[5])

    # check and get life word
    def check_life_word(self):
        # if all words have been passed
        if self.get_count_false_world()[0] == 0:
            view_info_transcription("Вы прошли все слова!")
            self.random_id_now = self.get_first_id_count_life_3()[0]
        else:
            # get random word
            self.random_id_now = self.get_id_row_bd()
            if self.get_work_count_life(self.random_id_now)[0] == 0:
                self.check_life_word()