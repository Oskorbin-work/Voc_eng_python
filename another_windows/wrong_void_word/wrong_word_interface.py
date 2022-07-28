from functions.voice.voice import voice
from PyQt5.QtWidgets import QGridLayout, QDialog
from another_windows.wrong_void_word.functions.table_wrong import WrongTable
from another_windows.wrong_void_word.functions.wrong_word_buttons import WrongWordButtons


class WrongWordInterface(QDialog, WrongWordButtons):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, list_now_word, random_language_now, text_check, parent=None):
        super().__init__(parent)

        self.list_now_word = list_now_word

        self.start_create_wrong_word_button()
        self.connect_function_with_button()
        self.generate_wrong_table(text_check, list_now_word, random_language_now)
        self.wrong_interface_add_widgets()
        self.main_window_parameter()


    def connect_function_with_button(self):
        self.btn_unpack.clicked.connect(self.modal_win_hide)
        self.btn_voice_wrong.clicked.connect(self.text_to_voice)

    def main_window_parameter(self):
        self.setMinimumWidth(800)
        self.setWindowTitle("Информация по неправильному переводу")

    def generate_wrong_table(self, text_check, list_now_word, random_language_now):
        self.test_table = WrongTable(
            column_count=2,
            row_count=5,
            vertical_header_set_visible=False,
            horizontal_header_set_visible=False,
            horizontal_header_set_stretch_last_section=True,
            vertical_header_set_stretch_last_section=True,
        )
        self.test_table.fill_table_wrong(text_check, list_now_word, random_language_now)

    def modal_win_hide(self):
        self.close()

    def text_to_voice(self):
        text = self.list_now_word[1]
        return voice(text)

    def wrong_interface_add_widgets(self):
        self.modalgrid = QGridLayout(self)
        self.modalgrid.addWidget(self.test_table.table_form, 1, 0)
        self.modalgrid.addWidget(self.btn_unpack, 2, 0)
        self.modalgrid.addWidget(self.btn_voice_wrong, 3, 0)
