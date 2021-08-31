# -----------------------------------------------------------
# PyQt 5.Initiate structure Main window and GUI
# -----------------------------------------------------------
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel,QAction,QMessageBox,QMainWindow
# -----------------------------------------------------------
# Few libraries
# -----------------------------------------------------------
import os  # To files Address


#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.wcLabel = QLabel(f"Error")
        self.menubar = self.menuBar()

    def bar_category_fileMenu(self):
        fileMenu = self.menubar.addMenu('File')
        Work_with_bd = self.menubar.addMenu('Data Base')

