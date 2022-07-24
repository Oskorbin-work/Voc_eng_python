# Voice
from functions.voice.voice import voice
from PyQt5.QtWidgets import QPushButton,QGridLayout,QDialog,QLabel



class WrongWordInterface(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, list_now_word, random_language_now,text_check, parent=None):
        super().__init__(parent)
        self.list_now_word = list_now_word
        self.random_language_now = random_language_now
        self.modalgrid = QGridLayout(self)
        self.text_check = text_check
        self.btn_unpack = QPushButton("Выйти", self)
        self.btn_voice_wrong = QPushButton("Озвучить текст", self)
        self.default_name_label_wrong()
        self.btn_unpack.clicked.connect(self.modal_win_hide)
        self.btn_voice_wrong.clicked.connect(self.test)
        self.wrong_word_grid()
        self.wrong_interface_add_widgets()

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

    def wrong_word_grid(self):
        self.label_text_check = QLabel(
            "<b>"
            f"{self.default_name_label_text_check} "
            " : "
            "</b>"
            f"{self.text_check}"
            "<br>"
            "<b>"
            f"{self.default_name_label_truth_translate_word}"
            "' "
            f"{self.determine_status_lang_word(True)}"
            "' : "
            "</b>"
            "<br>"
            f"{self.determine_status_lang_word(False)}"
            "<br>"
            "<b>"
            f"{self.default_name_label_part_of_a_word} "
            " : "
            "</b>"
            f"{self.list_now_word[4]}"
            "<br>"
            "<b>"
            f"{self.default_name_label_definition}"
            " : "
            "</b>"
            f"{self.list_now_word[5]}"
            "<br>"
            "<b>"
            f"{self.default_name_label_theme} "
            " : "
            "</b>"
            f"{self.list_now_word[7]}"
                                       )
        self.label_text_check.setWordWrap(True)
        self.label_text_check.setStyleSheet(open('another_windows/styles/tables.css').read())

    def test(self):
        text = self.list_now_word[1]
        return voice(text)

    def wrong_interface_add_widgets(self):
        self.modalgrid.addWidget(self.label_text_check, 0, 0)
        self.modalgrid.addWidget(self.btn_unpack, 2, 0)
        self.modalgrid.addWidget(self.btn_voice_wrong, 3, 0)