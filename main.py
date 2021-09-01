# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from Main_labels.mains_labels import Main_labels  # Initiate Labels from main window
from GUI.bar import Bar  # Initiate bar-structure
# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QGridLayout, QWidget


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

        # add main labels
        # Information about words
        grid.addWidget(self.timer_learn, 1, 1)  # timer from start
        grid.addWidget(self.sum_words_learn, 2, 0)  # count words are for learning
        grid.addWidget(self.false_words, 3, 0)  # count words to without verification
        grid.addWidget(self.true_words, 4, 0)  # count words to with verification
        grid.addWidget(self.change_words_learn, 5, 0)  # count words that can change
        # Word that is checking
        grid.addWidget(self.word_now, 6, 0)  # Word is checking.
        grid.addWidget(self.count_word_now, 7, 0)  # count words are for learning
        grid.addWidget(self.parts_of_speech_word_now, 8, 0)  # Part of speech
        grid.addWidget(self.transcription_word_now, 9, 0)  # Transcription
        grid.addWidget(self.chapter_word_now, 10, 0) # Chapter

        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_windows()
    sys.exit(app.exec_())