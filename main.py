# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget, QLineEdit,
)
import sys
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# settings
import settings
# Initiate labels from main window
from functions.main_labels import MainLabels
# Initiate buttons from main window
from functions.main_buttons import MainButtons
# Initiate bar-structure
from GUI.bar import Bar
# Notifications
import functions.notifications as notifications


# Class to describe structure main window
class MainWindow(QMainWindow, Bar, MainLabels, MainButtons, ):

    def __init__(self):
        super().__init__()
        # Set main setting "view window"
        self.main_window_parameter()
        # Initiate bar menu
        self.statusbar = self.statusBar()
        self.bar_category_file_menu()  # Initiate Bar category fileMenu
        # Initiate main buttons
        self.create_main_button()
        self.create_button_start_pause()
        self.create_info_transcription()
        # Initiate main text edit
        self.textEdit = QLineEdit()
        # Initiate grid
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
        self.btn.clicked.connect(lambda: self.clicked_main_button())
        self.btn.setDisabled(1)
        self.btn_start_pause.clicked.connect(lambda: self.clicked_button_start_pause())
        self.btn_info_transcription.clicked.connect(lambda: self.clicked_button_info_transcription())
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
        grid.addWidget(self.line_between_bd_and_word, 6, 0)
        # -----------------------------------------------------------
        # Word that is checking
        # -----------------------------------------------------------

        # Word is checking.
        grid.addWidget(self.word_now, 7, 0)
        # count words are for learning
        grid.addWidget(self.count_word_now, 8, 0)

        # Part of speech
        grid.addWidget(self.parts_of_speech_word_now, 9, 0)
        # Transcription
        grid.addWidget(self.transcription_word_now, 10, 0)
        # Chapter
        grid.addWidget(self.chapter_word_now, 11, 0)

        # info_transcription
        grid.addWidget(self.btn_info_transcription, 11, 1)

        # Field for word
        grid.addWidget(self.textEdit, 12, 0)
        # Buttons for check word
        grid.addWidget(self.btn, 12, 1)
        # start/pause
        grid.addWidget(self.btn_start_pause, 13, 1)
        # -----------------------------------------------------------
        # Wrong section
        # -----------------------------------------------------------
        index_check_word = 13
        # Place for information about now word
        for row_check in self.list_wrong_check_word:
            grid.addWidget(row_check, index_check_word, 0)
            index_check_word += 1

        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    # This is GOD def keyboards!
    def keyPressEvent(self, event):
        # Qt.Key.Key_*Button* working but it have bug
        # 16777220 is Enter.
        print(event.key())
        if event.key() == 16777220 and settings.TIMER_INTERVAL != 0:
            self.clicked_main_button()
        # 16777222 in Shift
        elif event.key() == 16777248:
            self.clicked_button_start_pause()
        # 16777251 in Option
        elif event.key() == 16777251:
            self.clicked_button_info_transcription()

    # Functional button "Проверить"
    def clicked_main_button(self):
        status_word = (self.check_enter_word(self.random_id_now, self.random_language_now, self.textEdit.text()))
        self.wrong_enter_word(self.random_id_now, status_word, self.textEdit.text())
        self.random_language_now = self.choice_ru_or_en_word()
        # -----------------------------------------------
        # section functional
        self.random_id_now = self.get_id_row_bd()
        # -----------------------------------------------
        self.label_set_text(self.random_id_now, self.random_language_now)
        # -----------------------------------------------
        self.textEdit.setFocus()
        self.textEdit.clear()
        # -----------------------------------------------
        # if all word was checked
        try:
            self.get_first_id_count_life_3()[0]
        except:
            self.game_over()

    # Button "Старт/Стоп"
    def clicked_button_start_pause(self):
        # stop and start program
        if settings.TIMER_INTERVAL == 0:
            settings.TIMER_INTERVAL = 1
            self.btn_start_pause.setText("Стоп")
            self.btn.setEnabled(1)
        else:
            self.btn.setDisabled(1)
            settings.TIMER_INTERVAL = 0
            self.btn_start_pause.setText("Старт")

        self.textEdit.setFocus()

    def clicked_button_info_transcription(self):
        self.get_info_transcription(self.random_id_now)
        #notifications.view_info_transcription(self.random_id_now)

    # if all word was checked
    def game_over(self):
        settings.PROGRAM_STATUS = False
        self.btn.setDisabled(1)
        self.btn_start_pause.setDisabled(1)
        settings.TIMER_INTERVAL = 0


# It for run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
