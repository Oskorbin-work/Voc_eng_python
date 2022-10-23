# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QGridLayout, QDialog
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Voice
from functions.voice.voice import voice
# Structure wrong table
from another_windows.wrong_void_word.functions.table_wrong import WrongTable
# Structure wrong buttons
from another_windows.wrong_void_word.functions.wrong_word_buttons import WrongWordButtons
#Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
# Сервер
from server.controller import ControllerServer


# clas create window to wrong word
class WrongWordInterface(QDialog, WrongWordButtons):

    def __init__(self, list_wrong_word, random_language_now, text_check, parent=None):
        super().__init__(parent)
        # list with information about wrong word
        self.list_wrong_word = list_wrong_word
        # Create buttons
        # ------------------------------------
        self.start_create_wrong_word_button()
        self.connect_function_with_button()
        # ------------------------------------
        # create wrong table inside window
        self.generate_wrong_table(text_check, random_language_now)
        self.wrong_interface_add_widgets()
        # ------------------------------------
        # set window parameter
        self.main_window_parameter()

    # add method to button`s
    def connect_function_with_button(self):
        self.btn_unpack.clicked.connect(self.modal_win_hide)
        self.btn_voice_wrong.clicked.connect(self.text_to_voice)

    # set window parameter
    def main_window_parameter(self):
        self.setMinimumWidth(800)
        self.set_window_title()

    # set text for title window
    def set_window_title(self):
        word_for_title = self.test_table.determine_status_lang_word(True)
        self.setWindowTitle(XML.get_attr_XML("wrong_window/title_window") + " ' " + word_for_title + " '")

    # create wrong table inside window
    def generate_wrong_table(self, text_check, random_language_now):
        # create and set parameter to table
        self.test_table = WrongTable(
            column_count=2,
            row_count=6,
            vertical_header_set_visible=False,
            horizontal_header_set_visible=False,
            horizontal_header_set_stretch_last_section=True,
            vertical_header_set_stretch_last_section=True,
        )
        # add text to table
        self.test_table.fill_table_wrong(text_check, self.list_wrong_word, random_language_now)

    # funk that close current window
    def modal_win_hide(self):
        self.close()

    # create voice word (only english)
    def text_to_voice(self):
        text = self.list_wrong_word[1]
        return voice(text)

    # set window parameter
    def wrong_interface_add_widgets(self):
        # used grid table
        self.modalgrid = QGridLayout(self)
        # add table to window
        self.modalgrid.addWidget(self.test_table.table_form, 1, 0)
        # add button "Exit" to window
        self.modalgrid.addWidget(self.btn_unpack, 2, 0)
        # add button "Voice text" to window
        self.modalgrid.addWidget(self.btn_voice_wrong, 3, 0)
