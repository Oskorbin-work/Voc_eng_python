# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QPushButton
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML


# Button for wrong windows
class WrongWordButtons:
    def start_create_wrong_word_button(self):
        self.name_label_buttons()

    def name_label_buttons(self):
        self.btn_unpack = QPushButton(XML.get_attr_XML("setting_window/label_button_window/button_exit"), self)
        self.btn_save_setting = QPushButton(XML.get_attr_XML("setting_window/label_button_window/button_voice"), self)

