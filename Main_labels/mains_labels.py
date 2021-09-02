# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore

import os # Initiate project into operating system
import sqlite3 # Database to Tooltip

from setting import ROOT_DIR

# Class to describe  main labels
class Main_labels:
    # create lables
    def name_labels(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.timer_learn = QLabel('Время: 00:00:00')
        self.timer()
        self.sum_words_learn = QLabel('Всего слов: ')
        self.false_words = QLabel('Непроверенные слова: ')
        self.true_words = QLabel('Проверенные слова: ')
        self.change_words_learn = QLabel('Старые слова на проверку: ')
        self.count_word_now = QLabel('Количество очков слова: ')
        self.parts_of_speech_word_now = QLabel('Часть слова: ')
        self.word_now = QLabel('Перевод слова: ')
        self.transcription_word_now = QLabel('Транскрипция: ')
        self.chapter_word_now = QLabel('Тема: ')

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

    # change word
    def label_set_text(self):
        random_word = 1
        # Connect database
        conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
        cur = conn.cursor()
        # get all command from database
        cur.execute("select * from Main_table where id_main  = %d;"% random_word)
        conn.commit()
        ones = (cur.fetchall())[0]
        print(ones)
        self.sum_words_learn.\
            setText(self.sum_words_learn.text() + ones[1])
        self.false_words.\
            setText(self.false_words.text() + ones[1])
        self.true_words.\
            setText(self.true_words.text() + ones[1])
        self.change_words_learn.\
            setText(self.change_words_learn.text() + ones[1])
        self.count_word_now.\
            setText(self.count_word_now.text() + str(ones[6]))
        self.parts_of_speech_word_now.\
            setText(self.parts_of_speech_word_now.text() + ones[1])
        self.word_now.\
            setText(self.word_now.text() + ones[3])
        self.transcription_word_now.\
            setText(self.transcription_word_now.text() + str(ones[4]))
        self.chapter_word_now.\
            setText(self.chapter_word_now.text() + ones[7])


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
