# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtGui

# set bold text
def set_bold(status):
    myFont = QtGui.QFont()
    myFont.setBold(status)
    return myFont


