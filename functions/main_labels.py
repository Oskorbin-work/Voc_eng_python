# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
import random
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.work_with_bd import Work_with_bd
from functions.main_buttons import Main_buttons
import settings
# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
import win32api


# Class to describe  main labels
class Main_labels(Work_with_bd):
    # create labels
    def name_labels(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.text_labels = [
            'Время: 00:00:00',
            'Всего слов: ',
            'Непроверенные слова: ',
            'Проверенные слова: ',
            'Старые слова: ',
            'Количество очков слова: ',
            'Часть слова: ',
            'Перевод слова: ',
            'Транскрипция: ',
            'Тема: ',
            '*********************************************',
            # id -- 11. Word "Неправильно"
            "Неправильно",
            # id -- 12. Entered word
            "Неправильный вариант: ",
            # id -- 13. True translate
            "Ответ: ",
            # id -- 14. Transcription
            "Транскрипция: ",

        ]
        self.timer_learn = QLabel()
        self.timer()
        self.sum_words_learn = QLabel()
        self.false_words = QLabel()
        self.true_words = QLabel()
        self.change_words_learn = QLabel()
        self.count_word_now = QLabel()
        self.parts_of_speech_word_now = QLabel()
        self.word_now = QLabel()
        self.transcription_word_now = QLabel()
        self.chapter_word_now = QLabel()
        self.line_between_bd_and_word = QLabel()
        self.list_wrong_check_word = [QLabel(), QLabel(), QLabel(), QLabel()]

    # describe font and size labels text
    def label_set_font_and_size(self):
        size_label_font = 10
        name_label_font = 'Arial'
        self.timer_learn. \
            setFont(QFont(name_label_font, size_label_font))
        self.sum_words_learn. \
            setFont(QFont(name_label_font, size_label_font))
        self.false_words. \
            setFont(QFont(name_label_font, size_label_font))
        self.true_words. \
            setFont(QFont(name_label_font, size_label_font))
        self.change_words_learn. \
            setFont(QFont(name_label_font, size_label_font))
        self.count_word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.parts_of_speech_word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.transcription_word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.chapter_word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.chapter_word_now. \
            setFont(QFont(name_label_font, size_label_font))
        self.line_between_bd_and_word. \
            setFont(QFont(name_label_font, size_label_font))
        for row_check in self.list_wrong_check_word:
            row_check.setFont(QFont(name_label_font, size_label_font))

    # def for get random row
    def get_id_row_bd(self):
        try:
            return random.randint(self.get_first_id_count_life_3()[0], self.get_count_all_word()[0])
        except:
            settings.PROGRAM_STATUS = False
            return -1

    # change word
    def label_set_text(self, random_id=1, language="ru"):
        lang_now = Main_buttons.check_language_word(Main_buttons, language)
        if random_id !=-1:
            self.list_now_word = self.get_row(random_id)
        else:
            self.list_now_word = ["","","","","","","","",""]
        self.sum_words_learn. \
            setText(self.text_labels[1] + str(self.get_count_all_word()[0]))
        self.false_words. \
            setText(self.text_labels[2] + str(self.get_count_false_world()[0]))
        self.true_words. \
            setText(self.text_labels[3] + str(self.get_count_true_world()[0]))
        self.change_words_learn. \
            setText(self.text_labels[4] + str(self.get_count_change_world()[0]))
        self.count_word_now. \
            setText(self.text_labels[5] + str(self.list_now_word[8]))
        self.parts_of_speech_word_now. \
            setText(self.text_labels[6] + self.list_now_word[3])

        self.word_now. \
            setText(self.text_labels[7] + self.list_now_word[lang_now])
        if language == "en":
            win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_RUSSIAN}', 1)
            self.transcription_word_now. \
                setText(self.text_labels[8] + str(self.list_now_word[4]))
        elif language == "ru":
            win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_ENGLISH}', 1)
            self.transcription_word_now. \
                setText(self.text_labels[8] + " - ")
        self.chapter_word_now. \
            setText(self.text_labels[9] + self.list_now_word[7])
        self.line_between_bd_and_word. \
            setText(self.text_labels[10])

    # check enter word
    def wrong_enter_word(self, random_id_now, status_word = "True",text_check = ""):
        list_now_word = self.get_row(random_id_now)
        # if enter word is false
        if not status_word:
            # -----------------------------------------------------------
            # Output information about true translate now word
            # -----------------------------------------------------------
            index_check_word = 11
            self.list_wrong_check_word[0].setText(
                f"{self.text_labels[index_check_word]}")
            self.list_wrong_check_word[1].setText(
                f"{self.text_labels[index_check_word+1]}"
                f" {text_check[0:1].upper()}{text_check[1:].lower()}")
            self.list_wrong_check_word[2].setText(
                f"{self.text_labels[index_check_word+2]}"
                f" {list_now_word[1]}"
                f" ="
                f" {list_now_word[2]}")
            self.list_wrong_check_word[3].setText(
                f"{self.text_labels[index_check_word + 3]}"
                f" [ {list_now_word[4]} ]")
            # -----------------------------------------------------------
            # add 1 life to now word
            if list_now_word[8] < 3:
                self.edit_work_count_life(random_id_now, list_now_word[8] + 1)

        # if enter word is true
        else:
            index_check_word = 11
            # clear information about last word
            for row_check in self.list_wrong_check_word:
                row_check.setText("")
                index_check_word += 1
            # output information that translate now word is true
            self.list_wrong_check_word[0].setText("Правильно")
            # add 1 life to now word
            if list_now_word[8] > 0:
                self.edit_work_count_life(random_id_now,list_now_word[8]-1)

    # Create timer
    def timer(self):
        self.timer_learn_1 = QtCore.QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()
        settings.TIMER_INTERVAL = 0

    # Change time to timer
    def timer_text(self):
        self.time = self.time.addSecs(settings.TIMER_INTERVAL)
        self.timer_learn.setText(self.time.toString("Время: hh:mm:ss"))

    # Main label def
    def main_label_def(self):
        self.add_work_count_life()
        self.order_main_table()
        self.random_id_now = self.get_id_row_bd()
        self.random_language_now = Main_buttons.choice_ru_or_en_word(Main_buttons)
        self.name_labels()
        self.label_set_font_and_size()
        self.label_set_text(self.random_id_now, self.random_language_now)
