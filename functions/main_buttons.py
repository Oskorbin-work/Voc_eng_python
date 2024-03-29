# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QPushButton
import random
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from database.sql_query_bd import WorkWithBd
from api.functions_for_all_systems import FuncForAllSystems
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# Class to describe  main buttons
class MainButtons(WorkWithBd):

    # def to create main_button
    def create_main_button(self):
        self.btn = QPushButton(XML.get_attr_XML("main_window/label_button_window/button_check"), self)
        self.btn.setStyleSheet("QPushButton"
                               "{"
                               "margin:0"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    # def to create button start pause
    def create_button_start_pause(self):
        self.btn_start_pause = QPushButton(XML.get_attr_XML("main_window/label_button_window/button_start"), self)
        self.btn_start_pause .setStyleSheet("QPushButton"
                               "{"
                                "margin:0"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    def create_info_transcription(self):
        self.btn_info_transcription = QPushButton(XML.get_attr_XML("main_window/label_button_window/button_definition"), self)
        self.btn_info_transcription.setStyleSheet("QPushButton"
                               "{"
                                "margin:0"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                               )

    def create_transcription_button(self):
        self.btn_voice_transcription = QPushButton(XML.get_attr_XML("main_window/label_button_window/button_voice"), self)
        #self.btn_transcription.setFixedSize(40, 40)
        self.btn_voice_transcription.setStyleSheet("QPushButton"
                                "{"
                                "margin:0"
                               "background-color : gray;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : gray;"
                               "}"
                                                   )

    # When a word is selected for checking, then you need to select a language for it
    def choice_ru_or_en_word(self):
        language = random.choice(settings.LANGUAGE)
        # change language
        FuncForAllSystems.change_language(FuncForAllSystems, language)
        return language

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

    # get current word
    def get_current_word(self, id_now_word, language):
        row_now_word = self.get_row(id_now_word)
        lang_now = self.check_language_word(language, "reverse_on")
        return row_now_word[lang_now]
