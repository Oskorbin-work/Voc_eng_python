# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QGridLayout, QDialog, QLabel, QLineEdit,QComboBox
from PyQt5 import QtCore
import re
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
# Structure wrong buttons
from another_windows.setting.functions.wrong_word_buttons import WrongWordButtons
# set labels
import elements.label as label
# settings programm
from settings import LANGUAGE_INTERFACE_LIST, STATUS_LANGUAGE_INTERFACE
from another_windows.setting.functions.save_setting import save_all

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
        self.btn_save_setting.clicked.connect(save_all)


    # funk that close current window
    def modal_win_hide(self):
        self.close()

    # create and setting grid
    def grid_settings(self):
        self.grid = QGridLayout(self)

    # check name
    # status title -- it name category
    def check_name_widget(self, text, range):
        if text[1] == "title":
            widget = QLabel(text[0])
            widget.setFont(label.set_bold(True))
            self.grid.addWidget(widget, range, 0, 1, 2, QtCore.Qt.AlignCenter)
        else:
            widget = QLabel(text[0])
            self.grid.addWidget(widget, range, 0)

    def check_place_widget(self,text, range):
        if text[1] == "title":
            pass
        elif text[1] == "text_area":
            widget = QLineEdit(text[1])
            self.grid.addWidget(widget, range, 1)
        elif text[1] == "choice_area":
            widget = QComboBox()
            widget.addItems(LANGUAGE_INTERFACE_LIST.keys())
            widget.setCurrentText(STATUS_LANGUAGE_INTERFACE)
            self.grid.addWidget(widget, range, 1)

    # add label to grid
    def label_add_to_grid(self):
        list_widgets = self.label_create_list()
        range = 0
        for i in list_widgets:
            self.check_name_widget(i, range)
            self.check_place_widget(i, range)
            #self.grid.addWidget(list_widgets[range][1], range, 1)
            range += 1
        # add button "Exit" to window
        self.grid.addWidget(self.btn_unpack, range, 0)
        self.grid.addWidget(self.btn_save_setting, range, 1)

    # create list path (in XML_language) label name help
    def label_list_path_widgets_name(self):
        list_path_widgets = [
            "setting_window/title_column/general_settings/name",
            "setting_window/elements_setting/language_interface/name",
        ]
        return list_path_widgets

    def label_list_path_widgets_place(self):
        title_column = [
            "setting_window/title_column/general_settings/type_change",
            "setting_window/elements_setting/language_interface/type_change",
                        ]
        return title_column

    # create list with name and place for change
    def label_create_list(self):
        list_title_column = self.label_list_path_widgets_place()
        list_path_widgets = self.label_list_path_widgets_name()
        list_qlabel_widgets = list()

        for one_column, two_column in zip(list_path_widgets,list_title_column):
            name_text = XML.get_attr_XML(one_column)
            type_change = XML.get_attr_XML(two_column)
            finale_type_column = type_change
            list_qlabel_widgets.append(
                [
                    name_text,
                    finale_type_column,
                ])
        return list_qlabel_widgets



