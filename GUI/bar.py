# -----------------------------------------------------------
# PyQt 5.Initiate structure Main window and GUI
# -----------------------------------------------------------
from PyQt5.QtWidgets import QLabel, QAction
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings

#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.wcLabel = QLabel('Error')
        self.menubar = self.menuBar()

    # create structure bar
    def bar_category_fileMenu(self):
        fileMenu = self.menubar.addMenu('File')
        fileMenu.addAction(QAction('', self))
        Work_with_bd = self.menubar.addMenu('Data Base')
        Work_with_bd.addAction(QAction('', self))
