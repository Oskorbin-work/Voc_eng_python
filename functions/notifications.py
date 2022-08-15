# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
from emoji import emojize
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

import another_windows.help_for_users.helper as Helper

# View QMessageBox about error
# (Example about failed sql request)
def view_error_critical(title, text=""):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

# view info_transcription
def view_info_transcription(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(XML.get_attr_XML("notifications/view_info_transcription/title"))
    msg.setText(XML.get_attr_XML("notifications/view_info_transcription/name_transcription") + ":\n" + str(text))
    msg.exec_()


# Button -- # exit program
def exit_program(name, question, yes, no):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    # https://stackoverflow.com/questions/35887523/qmessagebox-change-text-of-standard-button
    status = msg.question(msg, name, question, msg.Yes,
                                  msg.No)
    if status == QMessageBox.Yes:
        return yes
    else:
        return no

# view help
def view_help():
    wrong_window = None
    if wrong_window is None:
        wrong_window = Helper.HelperNotifications()
    wrong_window.exec()

def test():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setFont(QFont("Apple Color Emoji"))
    msg.setText(
        XML.get_attr_XML("notifications/help/enter") + "\n" +
        XML.get_attr_XML("notifications/help/status_program") + "\n" +
        XML.get_attr_XML("notifications/help/transcription") + "\n" +
        XML.get_attr_XML("notifications/help/voice") + "\n" +
        emojize(':purple_heart:', variant="emoji_type")+ "\n" +
        emojize(':black_heart:', variant="emoji_type") + "\n" +
        emojize(':books:') + "\n" +
        emojize(':bullseye:') + "\n" +
        emojize(':military_medal:') + "\n" +
        "\u2705" + "\n" +
        emojize(':keycap_1:') + "\n" +
        emojize(':keycap_2:') + "\n" +
        emojize(':keycap_3:')

    )
    msg.exec_()