# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QFont
from PyQt5.uic.properties import QtCore

from GUI.bar import *  # Initiate bar-structure
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFrame, QLineEdit, QGridLayout, QPushButton, QWidget


class main_windows(QMainWindow, Bar):

    def __init__(self):
        super().__init__()
        # value size windows
        self.window_width = 400
        self.window_height = 400
        # initiate bar menu
        self.statusbar = self.statusBar()
        self.bar_category_fileMenu()  # Initiate Bar category fileMenu
        # initiate value
        self.time = QtCore.QTime(0, 0, 0)
        self.timer_learn = QLabel('Время: 00:00:00')
        self.timer()
        self.sum_words_learn = QLabel('Всего слов: ')
        self.false_words = QLabel('Непроверенные слова: ')
        self.true_words = QLabel('Проверенные слова: ')
        self.change_words_learn = QLabel('Слова с некотором шансом на проверку: ')
        self.count_word_now = QLabel('Количество очков слова: ')
        self.parts_of_speech_word_now = QLabel('Часть слова: ')
        self.word_now = QLabel('Перевод слова: ')
        self.transcription_word_now = QLabel('Транскрипция: ')
        self.chapter_word_now = QLabel('Тема: ')
        # initiate functions
        self.label_set_font_and_size()
        self.main_structure()
        self.mains_label()
        self.main_window_parameter()

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

    def timer(self):
        self.timer_learn_1 = QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()

    def timer_text(self):
        self.time = self.time.addSecs(1)
        self.timer_learn.setText(self.time.toString("Время: hh:mm:ss"))


    def main_window_parameter(self):  # place to main setting "view window"
        self.setWindowTitle("Vocalubary_English")
        self.setFixedWidth(self.window_width)
        #self.setFixedHeight(self.window_height)
        self.show()

    def main_structure(self): # Initiate structure
        self.form_frame = QFrame()
        self.form_frame.setFrameShape(QFrame.StyledPanel)
        self.ver_frame = QFrame()
        self.ver_frame.setFrameShape(QFrame.StyledPanel)

    def mains_label(self):
        grid = QGridLayout()
        grid.addWidget(self.timer_learn, 1, 0)
        grid.addWidget(self.sum_words_learn, 2, 0)
        grid.addWidget(self.false_words, 3, 0)
        grid.addWidget(self.true_words, 4, 0)
        grid.addWidget(self.change_words_learn, 5, 0)
        grid.addWidget(self.count_word_now, 6, 0)
        grid.addWidget(self.parts_of_speech_word_now, 7, 0)
        grid.addWidget(self.word_now, 8, 0)
        grid.addWidget(self.transcription_word_now, 9, 0)
        grid.addWidget(self.chapter_word_now, 10, 0)
        # title_1.setText("ff")

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_windows()
    sys.exit(app.exec_())