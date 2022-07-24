# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget, QLineEdit,QLabel,QGroupBox,
)
from PyQt5.QtGui import QPalette, QColor
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
#work with exit program
from exit_file import Exit_program


# Class to describe structure main window
class MainWindow(QMainWindow, Bar, MainLabels, MainButtons, ):

    def __init__(self):
        super().__init__()
        # Set main setting "view window"
        self.main_window_parameter()
        # ------------------------------
        # Initiate bar menu
        # is not use
        # self.bar_category_file_menu()  # Initiate Bar category fileMenu
        # ------------------------------

        # Initiate main buttons
        self.create_main_button()
        self.create_button_start_pause()
        self.create_info_transcription()
        self.create_transcription_button()
        # Initiate main text edit
        self.textEdit = QLineEdit()
        # Initiate grid
        self.main_grid()

        self.view_data_status_bar_static_words()
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
        self.button_connect()
        grid_map = (
                # Timer from start                          # Words start program
                ((0, 0),                                    (0, 1),),
                # Count words are for learning              # Count words that can change
                ((1, 0),                                    (1, 1),),
                # Empty place                                # Empty place
                ((2, 0),                                    (2, 1),),
                # Word is checking                          # Empty place
                ((3, 0),                                    (3, 1),),
                #  Count words are for learning             # Empty place
                ((4, 0),                                    (4, 1),),
                # Part of speech                            # Empty place
                ((5, 0),                                    (5, 1),),
                # Transcription                             # Empty place
                ((6, 0),                                    (6, 1),),
                # Chapter                                   # Empty place
                ((7, 0),                                    (7, 1),),
                # Start/pause                               # info_transcription
                ((8, 0),                                    (8, 1),),
                # Field for word                            # Buttons for check word
                ((9, 0),                                    (9, 1),),
                # Place for transcription                   # Button for voice transcription
                ((10, 0),                                   (10, 1),),
        )
        # -----------------------------------------------------------
        # add main labels
        # Information about words
        # -----------------------------------------------------------
        # Line 0
        # Timer from start
        grid.addWidget(self.information_labels["timer learn"], grid_map[0][1][0], grid_map[0][0][1])
        # Line 1
        # Word is checking
        groupbox_word_now = QGroupBox()
        groupbox_word_now.setStyleSheet(
            "     background-color: lightgreen;"
        )
        #set color
        grid.addWidget(groupbox_word_now, grid_map[1][0][0], grid_map[1][0][1])
        grid.addWidget(self.information_labels["word now"], grid_map[1][0][0], grid_map[1][0][1])
        # Line 2
        # Field for word
        grid.addWidget(self.textEdit, grid_map[2][0][0], grid_map[2][0][1])

        # Line 3
        # Count words are for learning
        grid.addWidget(self.information_labels["count word now"], grid_map[3][0][0], grid_map[3][0][1])
        # Line 4
        # Part of speech
        grid.addWidget(self.information_labels["parts of speech word now"], grid_map[4][0][0], grid_map[4][0][1])

        # Line 5
        # Transcription
        grid.addWidget(self.information_labels["transcription word now"], grid_map[5][0][0], grid_map[5][0][1])

        # Line 6
        # Chapter
        grid.addWidget(self.information_labels["chapter word now"], grid_map[6][0][0], grid_map[6][0][1])

        # Line 7
        # Start/pause
        grid.addWidget(self.btn_start_pause, grid_map[7][0][0], grid_map[7][0][1])

        # Line 8
        # info_transcription
        grid.addWidget(self.btn_info_transcription, grid_map[8][0][0], grid_map[8][0][1])

        # Line 9
        # Buttons for check word
        grid.addWidget(self.btn, grid_map[9][0][0], grid_map[9][0][1])
        # Line 10
        # Buttons for voice word
        grid.addWidget(self.btn_voice_transcription, grid_map[10][0][0], grid_map[10][0][1])
    # -----------------------------------------------------------
        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def view_data_status_bar_static_words(self):
        self.data_status_bar_static_words(
            str(self.get_count_all_word()[0]),
            str(self.get_count_false_world_time()[0]),
            str(self.get_count_change_world()[0]),
        )

    def view_data_status_bar_hp(self):
        self.data_status_bar_hp(
            str(self.get_count_false_world()[0]),
            str(self.get_work_count_words(0)[0]),
            str(self.get_work_count_words(1)[0]),
            str(self.get_work_count_words(2)[0]),
            str(self.get_work_count_words(3)[0]),
        )

    # Place for connect buttons!
    def button_connect(self):
        self.btn.setDisabled(1)
        self.btn_voice_transcription.setDisabled(1)
        self.btn.clicked.connect(lambda: self.clicked_main_button())
        self.btn_start_pause.clicked.connect(lambda: self.clicked_button_start_pause())
        self.btn_info_transcription.clicked.connect(lambda: self.clicked_button_info_transcription())
        self.btn_voice_transcription.clicked.connect(lambda: self.clicked_button_voice_transcription())

    # This is GOD def keyboards!
    def keyPressEvent(self, event):
        # Qt.Key.Key_*Button* working but it have bug
        # 16777220 is Enter.
        if event.key() == 16777220: #and settings.TIMER_INTERVAL != 0:
            self.clicked_main_button()
        # 16777222 is F2
        elif event.key() == 16777265:
            self.clicked_button_start_pause()
        # 16777251 is Option
        elif event.key() == 16777251:
            self.clicked_button_info_transcription()
        # 16777248 is Command
        elif event.key() == 16777249:
            self.clicked_button_voice_transcription()
        # 16777264 is F1
        elif event.key() == 16777264:
            view_help()

    # Functional button "Проверить"
    def clicked_main_button(self):
        status_word = (self.check_enter_word(self.random_id_now, self.random_language_now, self.textEdit.text()))
        self.wrong_enter_word(self.random_id_now, status_word, self.textEdit.text(),self.random_language_now)
        self.random_language_now = self.choice_ru_or_en_word()
        self.language_control()
        # -----------------------------------------------
        # section functional
        self.check_life_word()
        # -----------------------------------------------
        self.label_set_text(self.random_id_now, self.random_language_now)
        # -----------------------------------------------
        self.textEdit.setFocus()
        self.textEdit.clear()
        # -----------------------------------------------
        # status_bar
        self.view_data_status_bar_hp()
        # if all word was checked
        try:
            self.get_first_id_count_life_3()[0]
        except:
            self.game_over()

    # Button "Старт/Стоп"
    def clicked_button_start_pause(self):
        self.language_control()
        # stop and start program
        if settings.TIMER_INTERVAL == 0:
            settings.TIMER_INTERVAL = 1

            self.view_data_status_bar_hp()
            self.btn_start_pause.setText("Пауза")
            self.btn.setEnabled(1)
        else:
            self.btn.setDisabled(1)
            settings.TIMER_INTERVAL = 0
            self.btn_start_pause.setText("Старт")

        self.textEdit.setFocus()

    # view info_transcription
    def clicked_button_info_transcription(self):
        self.get_info_transcription(self.random_id_now)
        #notifications.view_info_transcription(self.random_id_now)

    # voice word
    def clicked_button_voice_transcription(self):
        if self.random_language_now == "en":
            voice(self.get_english_word(self.random_id_now)[0][0])

    # Place for funk language
    def language_control(self):
        if self.random_language_now == "ru":
            self.btn_voice_transcription.setDisabled(1)
        else:
            self.btn_voice_transcription.setEnabled(1)

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
    exit = Exit_program()
    try:
        sys.exit(app.exec_())
    finally:
        exit.bd_to_default_state()
