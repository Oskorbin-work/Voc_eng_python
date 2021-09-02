# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Initiate Labels from main window
from Main_labels.mains_labels import Main_labels
from GUI.bar import Bar  # Initiate bar-structure
# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget,
)


# Class to describe structure main window
class Main_windows(QMainWindow, Bar, Main_labels):

    def __init__(self):
        super().__init__()
        # Set main setting "view window"
        self.main_window_parameter()
        # initiate bar menu
        self.statusbar = self.statusBar()
        self.bar_category_fileMenu()  # Initiate Bar category fileMenu
        # initiate grid
        self.main_grid()
        # Run GUI
        self.show()

    # place for main setting "view window"
    def main_window_parameter(self):
        self.setWindowTitle("Vocabulary_English")

    # place to main setting "view window"
    def main_grid(self):
        # realise main labels
        self.main_label_def()

        # create Grid
        grid = QGridLayout()

        # -----------------------------------------------------------
        # add main labels
        # Information about words
        # -----------------------------------------------------------

        # timer from start
        grid.addWidget(self.timer_learn, 1, 1)
        # count words are for learning
        grid.addWidget(self.sum_words_learn, 2, 0)
        # count words to without verification
        grid.addWidget(self.false_words, 3, 0)
        # count words to with verification
        grid.addWidget(self.true_words, 4, 0)
        # count words that can change
        grid.addWidget(self.change_words_learn, 5, 0)

        # -----------------------------------------------------------
        # Word that is checking
        # -----------------------------------------------------------

        # Word is checking.
        grid.addWidget(self.word_now, 6, 0)
        # count words are for learning
        grid.addWidget(self.count_word_now, 7, 0)
        # Part of speech
        grid.addWidget(self.parts_of_speech_word_now, 8, 0)
        # Transcription
        grid.addWidget(self.transcription_word_now, 9, 0)
        # Chapter
        grid.addWidget(self.chapter_word_now, 10, 0)

        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


# It for run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_windows()
    sys.exit(app.exec_())
