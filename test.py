# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget, QLineEdit,QLabel, QPushButton,
)
import sys
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.old_data_to_database import old_data
# settings
import settings
# Initiate labels from main window
from functions.main_labels import MainLabels
# Initiate buttons from main window
from functions.main_buttons import MainButtons
# Initiate bar-structure
from functions.bar import Bar
# Voice
from functions.voice.voice import voice
#notifications
from functions.notifications import view_help

# Class to describe structure main window
class MainWindow(QMainWindow, Bar, MainLabels, MainButtons, ):

    def __init__(self):
        super().__init__()
        self.main_window_parameter()
        self.main_grid()
        # Run GUI
        self.show()

    # place for main setting "view window"
    def main_window_parameter(self):
        self.setMinimumWidth(550)
        self.setWindowTitle("Vocabulary_English")


    # place to main setting "view window"
    def main_grid(self):
        # realise main labels
        self.main_label_def()
        # create Grid
        grid = QGridLayout()
        zrada = QLabel()
        size_label_font = 15
        name_label_font = 'JetBrains Mono'

        zrada.setStyleSheet(""
                       "font-style: bold;"
                            ""
                            )
        ff = QFont(name_label_font, size_label_font)
        zrada.setFont(ff)
        zrada.setText("Ill")
        grid.addWidget(zrada, 0, 0)

        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
    # Place for connect buttons!


# It for run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
