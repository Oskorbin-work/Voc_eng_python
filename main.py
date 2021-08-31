# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from GUI.bar import *  # Initiate bar-structure
import sys

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
        self.timer_learn = QLabel('Часов: 0 Минут: 0 Секунд: 0')
        self.sum_words_learn = QLabel('Всего слов: ')
        self.false_words = QLabel('Непроверенные слова: ')
        self.true_words = QLabel('Непроверенные слова: ')
        self.change_words_learn = QLabel('Слова с некотором шансом на проверку: ')
        # initiate functions
        self.main_structure()
        self.mains_label()
        self.main_window_parameter()


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

        # title_1.setText("ff")

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_windows()
    sys.exit(app.exec_())