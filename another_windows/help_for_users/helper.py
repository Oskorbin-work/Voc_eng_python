# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QGridLayout, QDialog, QLabel
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
from emoji import emojize


class HelperNotifications(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window_parameter()
        self.grid_settings()
        self.label_add_to_grid()

    # set window parameter
    def main_window_parameter(self):
        # self.setMinimumWidth(300)
        self.set_window_title()

    # set text for title window
    def set_window_title(self):
        self.setWindowTitle(XML.get_attr_XML("helper_window/title"))

    def grid_settings(self):
        self.grid = QGridLayout(self)

    def label_add_to_grid(self):
        list_widgets = self.label_create_list()
        range = 0
        for i in list_widgets:
            self.grid.addWidget(list_widgets[range], range, 0)
            range += 1

    def label_create_list(self):
        list_path_widgets = [
            "notifications/help/enter",
            "notifications/help/status_program",
            "notifications/help/transcription",
            "notifications/help/voice",
        ]
        list_qlabel_widgets = list()
        for i in list_path_widgets:
            list_qlabel_widgets.append(QLabel(XML.get_attr_XML(i)))
        return list_qlabel_widgets
