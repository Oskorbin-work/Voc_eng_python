from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.uic.properties import QtCore
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore


class Main_labels:
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

    def label_set_font_and_size(self):
        size_label_font = 10
        name_label_font = 'Arial'
        self.timer_learn.setFont(QFont(name_label_font, size_label_font))
        self.sum_words_learn.setFont(QFont(name_label_font, size_label_font))
        self.false_words.setFont(QFont(name_label_font, size_label_font))
        self.true_words.setFont(QFont(name_label_font, size_label_font))
        self.change_words_learn.setFont(QFont(name_label_font, size_label_font))
        self.count_word_now.setFont(QFont(name_label_font, size_label_font))
        self.parts_of_speech_word_now.setFont(QFont(name_label_font, size_label_font))
        self.word_now.setFont(QFont(name_label_font, size_label_font))
        self.transcription_word_now.setFont(QFont(name_label_font, size_label_font))
        self.chapter_word_now.setFont(QFont(name_label_font, size_label_font))

    def label_set_text(self):
        self.sum_words_learn.setText(self.sum_words_learn.text() +"d")
        self.false_words.setText(self.false_words.text() +"d")
        self.true_words.setText(self.true_words.text() +"d")
        self.change_words_learn.setText(self.change_words_learn.text() +"d")
        self.count_word_now.setText(self.count_word_now.text() +"d")
        self.parts_of_speech_word_now.setText(self.parts_of_speech_word_now.text() +"d")
        self.word_now.setText(self.word_now.text() +"d")
        self.transcription_word_now.setText(self.transcription_word_now.text() +"d")
        self.chapter_word_now.setText(self.chapter_word_now.text() +"d")

    def timer(self):
        self.timer_learn_1 = QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()

    def timer_text(self):
        self.time = self.time.addSecs(1)
        self.timer_learn.setText(self.time.toString("Время: hh:mm:ss"))

    def main_label_def(self):
        self.name_labels()
        # initiate functions
        self.label_set_font_and_size()
        self.label_set_text()