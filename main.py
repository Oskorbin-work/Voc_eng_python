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
from database.old_data_to_database import old_data
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
        #old_data()
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
        self.setMinimumWidth(510)
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
                # Timer from start                          # Words start program
                ((0, 0),                                    (0, 1),),
                # Count words are for learning              # Count words that can change
                ((1, 0),                                    (1, 1),),
                # None place
                ((2, 0),                                    (2, 1),),
                # Word is checking                          # Words where life => 1
                ((3, 0),                                    (3, 1),),
                #  Count words are for learning             # Words where life = 3
                ((4, 0),                                    (4, 1),),
                # Part of speech                            # Words where life = 2
                ((5, 0),                                    (5, 1),),
                # Transcription                             # Words where life = 1
                ((6, 0),                                    (6, 1),),
                # Chapter                                   # Words where life = 0
                ((7, 0),                                    (7, 1),),
                # Start/pause                               # info_transcription
                ((8, 0),                                    (8, 1),),
                # Field for word                            # Buttons for check word
                ((9, 0),                                    (9, 1),),
                # Place for true answer                     # Place for enter answer
                ((10, 0),                                   (10, 1),),
                # Place for transcription
                ((11, 0),                                   (11, 1),),
        )
        # -----------------------------------------------------------
        # add main labels
        # Information about words
        # -----------------------------------------------------------
        # Line 0
        # Timer from start
        grid.addWidget(self.information_labels["timer learn"], grid_map[0][0][0], grid_map[0][0][1])
        # words start program
        grid.addWidget(self.information_labels["words start program"], grid_map[0][1][0], grid_map[0][1][1])

        # Line 1
        # Count words are for learning
        grid.addWidget(self.information_labels["sum words learn"], grid_map[1][0][0], grid_map[0][0][1])
        # Count words that can change
        grid.addWidget(self.information_labels["change words learn"], grid_map[1][1][0], grid_map[1][1][1])

        # Line 2
        # None place
        grid.addWidget(self.information_labels["none place"], grid_map[2][1][0], grid_map[2][1][1])

        # Line 3
        # Word is checking
        grid.addWidget(self.information_labels["word now"], grid_map[3][0][0], grid_map[3][0][1])
        # Words where life => 1
        grid.addWidget(self.information_labels["words with more 1"], grid_map[3][1][0], grid_map[3][1][1])

        # Line 4
        # Count words are for learning
        grid.addWidget(self.information_labels["count word now"], grid_map[4][0][0], grid_map[4][0][1])
        # Words where life = 3
        grid.addWidget(self.information_labels["words with 3"], grid_map[4][1][0], grid_map[4][1][1])

        # Line 5
        # Part of speech
        grid.addWidget(self.information_labels["parts of speech word now"], grid_map[5][0][0], grid_map[5][0][1])
        # Words where life = 2
        grid.addWidget(self.information_labels["words with 2"], grid_map[5][1][0], grid_map[5][1][1])

        # Line 6
        # Transcription
        grid.addWidget(self.information_labels["transcription word now"], grid_map[6][0][0], grid_map[6][0][1])
        # Words where life = 1
        grid.addWidget(self.information_labels["words with 1"], grid_map[6][1][0], grid_map[6][1][1])

        # Line 7
        # Chapter
        grid.addWidget(self.information_labels["chapter word now"], grid_map[7][0][0], grid_map[7][0][1])
        # Words where life = 0
        grid.addWidget(self.information_labels["words with 0"], grid_map[7][1][0], grid_map[7][1][1])

        # Line 8
        # Start/pause
        grid.addWidget(self.btn_start_pause, grid_map[8][1][0], grid_map[8][1][1])
        # info_transcription
        grid.addWidget(self.btn_info_transcription, grid_map[8][0][0], grid_map[8][0][1])

        # Line 9
        # Field for word
        grid.addWidget(self.textEdit, grid_map[9][0][0], grid_map[9][0][1])
        # Buttons for check word
        grid.addWidget(self.btn, grid_map[9][1][0], grid_map[9][1][1])

        # -----------------------------------------------------------
        # Wrong section
        # -----------------------------------------------------------

        # Line 10
        # Place for true answer
        grid.addWidget(self.information_labels["right one"], grid_map[10][0][0], grid_map[10][0][1])
        # Place for enter answer
        grid.addWidget(self.information_labels["wrong one"], grid_map[10][1][0], grid_map[10][1][1])

        # Line 11
        # Place for transcription
        grid.addWidget(self.information_labels["transcription word previous"], grid_map[11][1][0], grid_map[11][1][1])
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
