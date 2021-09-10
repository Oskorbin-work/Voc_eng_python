# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
from database.work_with_bd import Work_with_bd

import random


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
            'Старые слова на проверку: ',
            'Количество очков слова: ',
            'Часть слова: ',
            'Перевод слова: ',
            'Транскрипция: ',
            'Тема: ',
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

    # describe font and size labels text
    def label_set_font_and_size(self):
        size_label_font = 10
        name_label_font = 'Arial'
        self.timer_learn.\
            setFont(QFont(name_label_font, size_label_font))
        self.sum_words_learn.\
            setFont(QFont(name_label_font, size_label_font))
        self.false_words.\
            setFont(QFont(name_label_font, size_label_font))
        self.true_words.\
            setFont(QFont(name_label_font, size_label_font))
        self.change_words_learn.\
            setFont(QFont(name_label_font, size_label_font))
        self.count_word_now.\
            setFont(QFont(name_label_font, size_label_font))
        self.parts_of_speech_word_now.\
            setFont(QFont(name_label_font, size_label_font))
        self.word_now.\
            setFont(QFont(name_label_font, size_label_font))
        self.transcription_word_now.\
            setFont(QFont(name_label_font, size_label_font))
        self.chapter_word_now.\
            setFont(QFont(name_label_font, size_label_font))

    # def for get random row
    def random_row_bd(self):
        return random.randint(1, self.get_count_all_word()[0])

    # change word
    def label_set_text(self, random_id=1):
        list_now_word = self.get_row(random_id)
        self.sum_words_learn.\
            setText(self.text_labels[1] + str(self.get_count_all_word()[0]))
        self.false_words.\
            setText(self.text_labels[2] + str(self.get_count_false_world()[0]))
        self.true_words.\
            setText(self.text_labels[3] + str(self.get_count_true_world()[0]))
        self.change_words_learn.\
            setText(self.text_labels[4] + str(self.get_count_change_world()[0]))
        self.count_word_now.\
            setText(self.text_labels[5] + str(list_now_word[6]))
        self.parts_of_speech_word_now.\
            setText(self.text_labels[6] + list_now_word[3])
        self.word_now.\
            setText(self.text_labels[7] + list_now_word[1])
        self.transcription_word_now.\
            setText(self.text_labels[8] + str(list_now_word[4]))
        self.chapter_word_now.\
            setText(self.text_labels[9] + list_now_word[7])

    # create timer
    def timer(self):
        self.timer_learn_1 = QtCore.QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()

    # change time to timer
    def timer_text(self):
        self.time = self.time.addSecs(1)
        self.timer_learn.setText(self.time.toString("Время: hh:mm:ss"))

    # main label def
    def main_label_def(self):
        self.name_labels()
        self.label_set_font_and_size()
        self.label_set_text()
        self.add_work_count_life()
