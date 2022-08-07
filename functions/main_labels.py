# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore
# -----------------------------------------------------------
# Import classes
# -----------------------------------------------------------
import another_windows.wrong_void_word.wrong_word_interface as WrondWindow
# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
from emoji import emojize

# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from database.work_data_bd import WorkDataBd
from functions.main_buttons import MainButtons
import settings
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# Class to describe  main labels
class MainLabels(WorkDataBd):

    # create labels
    def name_labels(self):
        self.time = QtCore.QTime(0, 0, 0)
        self.timer()
        self.text_labels = [
            emojize(':purple_heart:', variant="emoji_type"),
            XML.get_attr_XML("main_window/label/help_for_word"),
            emojize(':black_heart:', variant="emoji_type"),
        ]
        self.information_labels = {
            "timer learn": QLabel(),
            "sum words learn": QLabel(),
            "count word now": QLabel(),
            "parts of speech word now": QLabel(),
            "word now": QLabel(),
            "transcription word now": QLabel(),
            "chapter word now": QLabel(),
        }

    # describe font and size labels text
    def label_set_font_and_size(self):
        size_label_font = 14
        name_label_font = 'JetBrains Mono'
        for element in self.information_labels:
            self.information_labels[element].setFont(QFont(name_label_font, size_label_font))
        self.information_labels["timer learn"].setFont(QFont('JetBrains Mono', 13))
        self.information_labels["word now"].setFont(QFont('JetBrains Mono', 24))
        self.information_labels["parts of speech word now"].setFont(QFont('JetBrains Mono', 13))
        self.information_labels["transcription word now"].setFont(QFont('JetBrains Mono', 13))

    # change word
    def label_set_text(self, random_id=1, language="ru"):
        lang_now = MainButtons.check_language_word(MainButtons, language)
        if random_id != -1:
            self.list_now_word = self.get_row(random_id)
        else:
            self.list_now_word = ["", "", "", "", "", "", "", "", ""]

        self.information_labels["count word now"]. \
            setText(self.text_labels[0] + str(self.list_now_word[8]) +
                    " " +
                    self.text_labels[2] + str(self.list_now_word[10]))
        self.information_labels["parts of speech word now"]. \
            setText(self.list_now_word[3])

        self.information_labels["word now"]. \
            setText(self.list_now_word[lang_now])
        self.information_labels["chapter word now"]. \
            setText(self.text_labels[1] + " " + self.list_now_word[7])
        self.information_labels["word now"].setText(
            self.information_labels["word now"].text()
        )
        if language == "en":
            self.information_labels["transcription word now"]. \
                setText(f"[{str(self.list_now_word[4])}]")
        elif language == "ru":
            self.information_labels["transcription word now"]. \
                setText("")

    # functional where create wrong word window
    def create_wrong_window(self, list_wrong_word, random_language_now, text_check):
        self.wrong_window = None
        if self.wrong_window is None:
            self.wrong_window = WrondWindow.WrongWordInterface(list_wrong_word, random_language_now, text_check)
        self.wrong_window.exec()

    # check enter word
    def wrong_enter_word(self, random_id_now, status_word="True", text_check="", random_language_now=""):
        list_now_word = self.get_row(random_id_now)
        # if enter word is false
        if not status_word:
            self.create_wrong_window(list_now_word, random_language_now, text_check)

            # add 1 life to now word
            if list_now_word[8] < 3:
                self.edit_work_count_life(random_id_now, 3)

            # if user wrong then word can`t got point for "count_true_attempt"
            # and "count_true_attempt" = 0
            if self.get_status_word(random_id_now)[0] == "is_activate":
                self.edit_count_true_attempt(random_id_now, 0)

            # if word get status "temp_activate" then
            # it got status "is_activate"
            if self.get_status_word(random_id_now)[0] == "temp_activate":
                self.edit_status_word(random_id_now, "is_activate")
                self.edit_count_life(random_id_now, 3)

        # if enter word is true
        else:
            # add 1 life to now word
            if list_now_word[8] > 0:
                self.edit_work_count_life(random_id_now, list_now_word[8] - 1)

            if list_now_word[8] == 1:
                if self.get_status_word(random_id_now)[0] == "is_activate":
                    self.edit_count_true_attempt(random_id_now, 1)

                    if self.get_count_true_attempt(random_id_now)[0] == 3:
                        self.edit_count_true_attempt(random_id_now, 0)
                        self.edit_count_life(random_id_now, -1)
                        self.edit_status_word(random_id_now, "not_activate")

    # Create timer
    def timer(self):
        self.timer_learn_1 = QtCore.QTimer(self)
        self.timer_learn_1.setInterval(1000)
        self.timer_learn_1.timeout.connect(self.timer_text)
        self.timer_learn_1.start()
        settings.TIMER_INTERVAL = 0

    # Change time to timer
    def timer_text(self):
        self.time = self.time.addSecs(settings.TIMER_INTERVAL)
        self.information_labels["timer learn"].setText(self.time.toString(XML.get_attr_XML("main_window/label/timer"),))
        self.information_labels["timer learn"].setAlignment(QtCore.Qt.AlignRight)

    # Main label def
    def main_label_def(self):
        self.start_set_up()
        self.order_main_table()
        self.check_life_word()
        self.random_language_now = MainButtons.choice_ru_or_en_word(MainButtons)
        self.name_labels()
        self.label_set_font_and_size()
        self.label_set_text(self.random_id_now, self.random_language_now)
