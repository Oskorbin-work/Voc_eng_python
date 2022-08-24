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
def view_info(name, question, yes, no):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle(name)
    msg.setText(question)
    # -------------------------------------------
    # sector buttons
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = msg.button(QMessageBox.Yes)
    buttonY.setText(yes)
    buttonN = msg.button(QMessageBox.No)
    buttonN.setText(no)
    # -------------------------------------------
    msg.exec_()

    if msg.clickedButton() == buttonY:
        return yes
    elif msg.clickedButton() == buttonN:
        return no
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
    msg.setWindowTitle(name)
    msg.setText(question)
    # -------------------------------------------
    # sector buttons
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    buttonY = msg.button(QMessageBox.Yes)
    buttonY.setText(yes)
    buttonN = msg.button(QMessageBox.No)
    buttonN.setText(no)
    # -------------------------------------------
    msg.exec_()

    if msg.clickedButton() == buttonY:
        return yes
    elif msg.clickedButton() == buttonN:
        return no


# NO pressed

# view help
def view_help():
    wrong_window = None
    if wrong_window is None:
        wrong_window = Helper.HelperNotifications()
    wrong_window.exec()