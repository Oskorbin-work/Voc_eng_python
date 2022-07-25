# Voice
import PyQt5

from functions.voice.voice import voice
from PyQt5.QtWidgets import QPushButton, QGridLayout, QDialog, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
class WrongWordInterface(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, list_now_word, random_language_now, text_check, parent=None):
        super().__init__(parent)
        self.list_now_word = list_now_word
        self.random_language_now = random_language_now
        self.modalgrid = QGridLayout(self)
        self.text_check = text_check
        self.content_wrong_table = dict()
        self.btn_unpack = QPushButton("В главное меню", self)
        self.btn_voice_wrong = QPushButton("Озвучить текст", self)
        self.default_name_label_wrong()
        self.btn_unpack.clicked.connect(self.modal_win_hide)
        self.btn_voice_wrong.clicked.connect(self.text_to_voice)
        self.generate_wrong_table()
        self.wrong_interface_add_widgets()
        self.main_window_parameter()

    def main_window_parameter(self):
        self.setMinimumWidth(900)
        self.setWindowTitle("Неправильный перевод!")

    def default_name_label_wrong(self):
        self.default_name_label_text_check = "Ваш перевод"
        self.default_name_label_truth_translate_word = "Правильный перевод"
        self.default_name_label_part_of_a_word = "Часть слова"
        self.default_name_label_definition = "Дефиниция"
        self.default_name_label_theme = "Тема"

    def determine_status_lang_word(self, flag_now_language=True):
        if self.random_language_now == "en":
            if flag_now_language:
                return self.list_now_word[1]
            else:
                return self.list_now_word[2]
        elif self.random_language_now == "ru":
            if flag_now_language:
                return self.list_now_word[2]
            else:
                return self.list_now_word[1]

    def modal_win_hide(self):
        self.close()

    # ----------------------------------
    def description_wrong_word(self):
        description_name_label_text_check = "Ваш перевод"
        content_name_label_text_check = self.text_check
        return {f'{description_name_label_text_check}': content_name_label_text_check}

    def description_true_word_and_translate(self):
        description_name_label_truth_translate_word = "Правильный перевод: " \
                                                      + self.determine_status_lang_word(True)
        content_name_label_truth_translate_word = self.determine_status_lang_word(False)
        return {f'{description_name_label_truth_translate_word}': content_name_label_truth_translate_word}

    def description_part_of_a_word(self):
        description_name_label_part_of_a_word = "Часть слова"
        content_name_label_part_of_a_word = self.list_now_word[3]
        return {f'{description_name_label_part_of_a_word}': content_name_label_part_of_a_word}

    def description_transcription(self):
        description_transcription = "Транскрипция"
        content_transcription = self.list_now_word[4]
        return {f'{description_transcription}': content_transcription}

    def description_definition(self):
        description_name_label_definition = "Дефиниция"
        content_name_label_definition = self.list_now_word[5]
        return {f'{description_name_label_definition}': content_name_label_definition}

    def description_theme_word(self):
        description_name_label_theme = "Тема"
        content_name_label_theme = self.list_now_word[7]
        return {f'{description_name_label_theme}': content_name_label_theme}

    def description_all_row(self):
        self.update_wrong_table(self.description_wrong_word())
        self.update_wrong_table(self.description_true_word_and_translate())
        self.update_wrong_table(self.description_part_of_a_word())
        self.update_wrong_table(self.description_transcription())
        self.update_wrong_table(self.description_definition())
        self.update_wrong_table(self.description_theme_word())

    # ----------------------------------
    # table to view information about wrong table
    # ----------------------------------

    def check_content_empty(self,dict_add):
        return ("".join(f"{v}" for k, v in dict_add.items())) == "-"

    def update_wrong_table(self,dict_add):
        if not self.check_content_empty(dict_add):
            self.content_wrong_table.update(dict_add)

    def settings_wrong_table(self):
        self.wrong_table = QTableWidget(self)
        self.wrong_table.setColumnCount(2)
        self.wrong_table.setRowCount(5)
        self.wrong_table.verticalHeader().setVisible(False)
        self.wrong_table.horizontalHeader().setVisible(False)
        self.wrong_table.horizontalHeader().setStretchLastSection(True)
        self.wrong_table.verticalHeader().setStretchLastSection(True)
        self.wrong_table.setWordWrap(True)

    def generate_wrong_table(self):
        self.settings_wrong_table()
        self.description_all_row()
        num = 0
        for j, k in self.content_wrong_table.items():
            description_column = QTableWidgetItem(j)
            description_column.setFlags(Qt.ItemIsEnabled)
            self.wrong_table.setItem(num, 0, description_column)
            content_column = QTableWidgetItem(k)
            content_column.setFlags(Qt.ItemIsEnabled)
            self.wrong_table.setItem(num, 1, content_column)
            num += 1
        self.wrong_table.resizeColumnsToContents()
    # ----------------------------------

    def text_to_voice(self):
        text = self.list_now_word[1]
        return voice(text)

    def wrong_interface_add_widgets(self):
        self.modalgrid.addWidget(self.wrong_table, 1, 0)
        self.modalgrid.addWidget(self.btn_unpack, 2, 0)
        self.modalgrid.addWidget(self.btn_voice_wrong, 3, 0)
