# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QPushButton
import random
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from database.work_with_bd import WorkWithBd


# Class to describe  main buttons
class MainButtons(WorkWithBd):

    # def to create main_button
    def create_main_button(self):
        self.btn = QPushButton('Проверить', self)
        self.btn.setStyleSheet("QPushButton"
                               "{"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    # def to create button start pause
    def create_button_start_pause(self):
        self.btn_start_pause = QPushButton('Старт', self)
        self.btn_start_pause .setStyleSheet("QPushButton"
                               "{"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    # When a word is selected for checking, then you need to select a language for it
    def choice_ru_or_en_word(self):
        return random.choice(settings.LANGUAGE)

    # chek language now word
    def check_language_word(self, language, reverse="reverse_off"):
        if reverse == "reverse_off":
            if language == "ru":
                return 2
            elif language == "en":
                return 1
        elif reverse == "reverse_on":
            if language == "ru":
                return 1
            elif language == "en":
                return 2

    # Check entered word with selected word
    def check_enter_word(self, id_now_word, language, text_check):
        row_now_word = self.get_row(id_now_word)
        lang_now = self.check_language_word(language, "reverse_on")
        if row_now_word[lang_now].lower() == text_check.lower():
            return True
        else:
            return False
