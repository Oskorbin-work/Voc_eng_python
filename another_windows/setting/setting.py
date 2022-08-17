# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QGridLayout, QDialog, QLabel
from PyQt5.QtGui import QFont
import re
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
# Structure wrong buttons
from another_windows.setting.functions.wrong_word_buttons import WrongWordButtons


# class for setting window
class SettingInterface(QDialog, WrongWordButtons):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window_parameter()
        # Create buttons
        # ------------------------------------
        self.start_create_wrong_word_button()
        self.connect_function_with_button()

        self.grid_settings()
        self.label_add_to_grid()


    # set window parameter
    def main_window_parameter(self):
        # self.setMinimumWidth(300)
        self.set_window_title()

    # set text for title window
    def set_window_title(self):
        self.setWindowTitle(XML.get_attr_XML("setting_window/title"))
        self.setMinimumWidth(400)

    # add method to button`s
    def connect_function_with_button(self):
        self.btn_unpack.clicked.connect(self.modal_win_hide)

    # funk that close current window
    def modal_win_hide(self):
        self.close()

    # create and setting grid
    def grid_settings(self):
        self.grid = QGridLayout(self)

    def label_add_to_grid(self):
        list_widgets = self.label_create_list()
        range = 0
        for i in list_widgets:
            self.grid.addWidget(list_widgets[range][0], range, 0)
            self.grid.addWidget(list_widgets[range][1], range, 1)
            range += 1
        # add button "Exit" to window
        self.grid.addWidget(self.btn_unpack, range, 0)
        self.grid.addWidget(self.btn_save_setting, range, 1)

    # create list path (in XML_language) label name help
    def label_list_path_widgets (self):
        list_path_widgets = [
            "notifications/help/enter/name",
            "notifications/help/status_program/name",
            "notifications/help/transcription/name",
            "notifications/help/voice/name",
            "notifications/help/purple_heart/name",
            "notifications/help/black_heart/name",
            "notifications/help/books/name",
            "notifications/help/bullseye/name",
            "notifications/help/military_medal/name",
            "notifications/help/check_mark_button/name",
            "notifications/help/keycap_1/name",
            "notifications/help/keycap_2/name",
            "notifications/help/keycap_3/name",
        ]
        return list_path_widgets
    # create list with name and place for change
    def label_create_list(self):
        list_path_widgets = self.label_list_path_widgets()
        list_qlabel_widgets = list()
        for i  in list_path_widgets:
            name_text = XML.get_attr_XML(i)
            list_qlabel_widgets.append(
                [
                    QLabel(name_text),
                    QLabel("f")
                ])
        return list_qlabel_widgets



