# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QWidget, QGroupBox,
)
from PyQt5 import QtCore, QtTest

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
from functions.bar import Bar
# Voice
from functions.voice.voice import voice
# Notifications
from functions.notifications import view_help
# Work with exit program
from exit_file import Exit_program
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML


# Class to describe structure main window
class MainWindow(QMainWindow, Bar, MainLabels, MainButtons, ):

    def __init__(self):
        super().__init__()
        # Set main setting "view window"
        self.main_window_parameter()
        # ------------------------------
        # Initiate bar menu
        # is not use
        # self.bar_category_file_menu()  #Initiate Bar category fileMenu
        # ------------------------------

        # Initiate main buttons
        self.create_main_button()
        self.create_button_start_pause()
        self.create_info_transcription()
        self.create_transcription_button()
        self.create_edit_text()
        self.textEdit.setFixedHeight(25)
        self.textEdit.setPlaceholderText(XML.get_attr_XML("main_window/text_edit/placeholder"))

        # Initiate grid
        self.main_grid()

        self.view_data_status_bar_static_words()
        # Run GUI
        self.show()

    # place for main setting "view window"
    def main_window_parameter(self):
        self.setMinimumWidth(700)
        self.setWindowTitle(XML.get_attr_XML("main_window/name_program"))

    # place to main setting "view window"
    def main_grid(self):
        # realise main labels
        self.main_label_def()
        # create Grid
        grid = QGridLayout()
        self.button_connect()
        self.grid_for_word_now()
        self.grid_for_information_word()
        self.grid_for_help_word()
        self.grid_for_last_letter()
        grid_map = (
                # Words start program                       # Timer from start
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
                # Chapter                                   # Empty place
                ((8, 0),                                    (8, 1),),
        )
        # -----------------------------------------------------------
        # add main labels
        # Information about words
        # -----------------------------------------------------------
        # Line 0
        # Timer from start
        grid.addLayout(self.grid_information_word, grid_map[0][0][0], grid_map[0][0][1])

        # Line 1
        # Word is checking
        groupbox_word_now = QGroupBox()
        # set color
        groupbox_word_now.setStyleSheet("background-color: lightgreen;")
        grid.addWidget(groupbox_word_now, grid_map[1][0][0], grid_map[1][0][1])
        grid.addLayout(self.grid_word_now, grid_map[1][0][0], grid_map[1][0][1])

        # Line 2
        grid.addLayout(self.grid_help_word, grid_map[2][0][0], grid_map[2][0][1])

        # Line 3
        grid.addLayout(self.grid_last_letter, grid_map[3][0][0], grid_map[3][0][1])

        # Line 4
        grid.addWidget(self.textEdit, grid_map[4][0][0], grid_map[4][0][1])

        # Line 5
        # info_transcription
        grid.addWidget(self.btn_start_pause, grid_map[5][0][0], grid_map[5][0][1])

        # Line 6
        # Buttons for check word
        grid.addWidget(self.btn_info_transcription, grid_map[6][0][0], grid_map[6][0][1])

        # Line 7
        # Buttons for voice word
        grid.addWidget(self.btn, grid_map[7][0][0], grid_map[7][0][1])

        # Line 8
        grid.addWidget(self.btn_voice_transcription, grid_map[8][0][0], grid_map[8][0][1])
    # -----------------------------------------------------------
        # This is widget!
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def grid_for_word_now(self):
        self.grid_word_now = QGridLayout()
        self.grid_word_now.setSpacing(1)
        self.grid_word_now.addWidget(self.information_labels["word now"], 0, 0, QtCore.Qt.AlignCenter)
        self.grid_word_now.addWidget(self.information_labels["parts of speech word now"], 1, 0, QtCore.Qt.AlignCenter)
        self.grid_word_now.addWidget(self.information_labels["transcription word now"], 2, 0, QtCore.Qt.AlignCenter)

    def grid_for_help_word(self):
        # create grid for help word
        self.grid_help_word = QGridLayout()
        self.grid_help_word.addWidget(self.information_labels["chapter word now"], 0, 0)

    def grid_for_last_letter(self):
        # create grid for help word
        self.grid_last_letter = QGridLayout()
        self.grid_last_letter.addWidget(self.information_labels["last letter"], 0, 0)
        self.grid_last_letter.addWidget(self.information_labels["transcription pre last word"], 0, 1)

    def grid_for_information_word(self):
        # create grid for information word
        self.grid_information_word = QGridLayout()

        self.grid_information_word.addWidget(self.information_labels["count word now"], 0, 0)
        self.grid_information_word.addWidget(self.information_labels["timer learn"], 0, 1)


    def view_data_status_bar_static_words(self):
        self.data_status_bar_static_words(
            str(self.get_count_all_unique_eng_word()[0]),
            str(self.get_count_false_world_time()[0]),
            str(self.get_count_change_eng_world()[0]),
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
        self.btn.clicked.connect(lambda: self.check_text_edit())
        self.btn_start_pause.clicked.connect(lambda: self.clicked_button_start_pause())
        self.btn_info_transcription.clicked.connect(lambda: self.clicked_button_info_transcription())
        self.btn_voice_transcription.clicked.connect(lambda: self.clicked_button_voice_transcription())

    # This is GOD def keyboards!
    def keyPressEvent(self, event):
        # Qt.Key.Key_*Button* working, but it has bug
        # 16777220 is Enter.
        if event.key() == 16777220 and settings.TIMER_INTERVAL != 0:
            self.check_text_edit()
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

    # check text.
    # if text not empty.
    def check_text_edit(self):

        if self.textEdit.text() != "":
            self.clicked_main_button()
        else:
            holder_word = self.get_current_word(self.random_id_now, self.random_language_now)
            self.textEdit.setText(holder_word[0])
            self.change_background_edit_text("red")
            QtTest.QTest.qWait(150)
            self.change_background_edit_text()


    # Functional button "Проверить"
    def clicked_main_button(self):

        status_word = (self.check_enter_word(self.random_id_now, self.random_language_now, self.textEdit.text()))

        self.wrong_enter_word(self.random_id_now, status_word, self.textEdit.text(), self.random_language_now)
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
        # default placeholder
        self.textEdit.setPlaceholderText(XML.get_attr_XML("main_window/text_edit/placeholder"))

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
            self.btn_start_pause.setText(XML.get_attr_XML("main_window/label_button_window/button_pause"))
            self.btn.setEnabled(1)
        else:
            self.btn.setDisabled(1)
            settings.TIMER_INTERVAL = 0
            self.btn_start_pause.setText(XML.get_attr_XML("main_window/label_button_window/button_start"))

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
    sys.exit(app.exec_())



