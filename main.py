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
from database.old_data_to_database import test
# settings
import settings
# Initiate labels from main window
from functions.main_labels import MainLabels
# Initiate buttons from main window
from functions.main_buttons import MainButtons
# Initiate bar-structure
from GUI.bar import Bar
# Notifications


# Class to describe structure main window
class MainWindow(QMainWindow, Bar, MainLabels, MainButtons, ):

    def __init__(self):
        super().__init__()
        #test()
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

        grid_map = (
                # sum words learn                           #timer learn -- 0
                ((0, 0),                                    (0, 1),),
                # count words to without verification
                ((1, 0),                                    (1, 1),),
                # count words to with verification
                ((2, 0),                                    (2, 1),),
                # sum words learn   #timer learn
                ((3, 0), (3, 1),),
                # sum words learn   #timer learn
                ((4, 0), (4, 1),),
                # sum words learn   #timer learn
                ((5, 0), (5, 1),),
                # sum words learn   #timer learn
                ((6, 0), (6, 1),),
                # sum words learn   #timer learn
                ((7, 0), (7, 1),),
                # sum words learn   #timer learn
                ((8, 0), (8, 1),),
                # sum words learn   #timer learn
                ((9, 0), (9, 1),),
                # sum words learn   #timer learn
                ((10, 0), (10, 1),),
                # sum words learn   #timer learn
                ((11, 0), (11, 1),),
                # sum words learn   #timer learn
                ((12, 0), (12, 1),),
                # sum words learn   #timer learn
                ((13, 0), (13, 1),),
                # sum words learn   #timer learn
                ((14, 0), (14, 1),),
        )
        # -----------------------------------------------------------
        # add main labels
        # Information about words
        # -----------------------------------------------------------
        # count words are for learning
        grid.addWidget(self.information_labels["sum words learn"], grid_map[0][0][0], grid_map[0][0][1])
        # timer from start
        grid.addWidget(self.information_labels["timer learn"], grid_map[0][1][0], grid_map[0][1][1])
        # count words to without verification
        grid.addWidget(self.information_labels["false words"], grid_map[1][0][0], grid_map[1][0][1])
        # count words to with verification
        grid.addWidget(self.information_labels["true words"], grid_map[2][0][0], grid_map[2][0][1])
        # count words that can change
        grid.addWidget(self.information_labels["change words learn"], 3, 0)
        # Line
        grid.addWidget(self.information_labels["line between bd and word"], 4, 0)
        # -----------------------------------------------------------
        # Word that is checking
        # -----------------------------------------------------------

        # Word is checking.
        grid.addWidget(self.information_labels["word now"], 5, 0)
        # count words are for learning
        grid.addWidget(self.information_labels["count word now"], 6, 0)

        # Part of speech
        grid.addWidget(self.information_labels["parts of speech word now"], 7, 0)
        # Transcription
        grid.addWidget(self.information_labels["transcription word now"], 8, 0)
        # Chapter
        grid.addWidget(self.information_labels["chapter word now"], 9, 0)

        # info_transcription
        grid.addWidget(self.btn_info_transcription, 9, 1)

        # Field for word
        grid.addWidget(self.textEdit, 10, 0)
        # Buttons for check word
        grid.addWidget(self.btn, 10, 1)
        # start/pause
        grid.addWidget(self.btn_start_pause, 11, 1)
        # -----------------------------------------------------------
        # Wrong section
        # -----------------------------------------------------------
        # Place for information about now word
        grid.addWidget(self.information_labels["status word"], 11, 0)
        grid.addWidget(self.information_labels["wrong one"], 12, 0)
        grid.addWidget(self.information_labels["right one"], 13, 0)
        grid.addWidget(self.information_labels["transcription word previous"], 14, 0)
        # -----------------------------------------------------------

        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    # This is GOD def keyboards!
    def keyPressEvent(self, event):
        # Qt.Key.Key_*Button* working but it have bug
        # 16777220 is Enter.
        if event.key() == 16777220 and settings.TIMER_INTERVAL != 0:
            self.clicked_main_button()
        # 16777222 in Shift
        elif event.key() == 16777249:
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
        self.check_life_word()
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
            self.btn_start_pause.setText("Пауза")
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
