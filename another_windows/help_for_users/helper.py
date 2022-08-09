# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QGridLayout, QDialog, QLabel
from PyQt5.QtGui import QFont
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
            print(list_widgets[range][0].text())
            self.grid.addWidget(list_widgets[range][0], range, 0)
            self.grid.addWidget(list_widgets[range][1], range, 1)
            range += 1

    def label_add_emojize(self):
        list_emojize = [
            "notifications/help/enter/description",
            "notifications/help/status_program/description",
            "notifications/help/transcription/description",
            "notifications/help/voice/description",
            "notifications/help/purple_heart/description",
            "notifications/help/black_heart/description",
            "notifications/help/books/description",
            "notifications/help/bullseye/description",
            "notifications/help/military_medal/description",
            "notifications/help/check_mark_button/description",
            "notifications/help/keycap_1/description",
            "notifications/help/keycap_2/description",
            "notifications/help/keycap_3/description",
        ]
        return list_emojize

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

    def label_create_list(self):
        list_path_widgets = self.label_list_path_widgets()
        list_emojii = self.label_add_emojize()
        list_qlabel_widgets = list()
        print(XML.get_attr_XML("notifications/help"))
        for i, j in zip(list_path_widgets, list_emojii):
            name_text = XML.get_attr_XML(i)
            name_description = XML.get_attr_XML(j)
            if name_text[0] == ":" and name_text[-1] == ":":
                name_text = emojize(name_text)
                list_qlabel_widgets.append(
                    [
                        QLabel(name_text),
                        QLabel(name_description)
                    ])
                list_qlabel_widgets[-1][0].setFont(QFont("Apple Color Emoji"))
            else:
                list_qlabel_widgets.append(
                    [
                        QLabel(name_text),
                        QLabel(name_description)
                    ])
        return list_qlabel_widgets