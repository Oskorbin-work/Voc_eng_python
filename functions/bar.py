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
        self.statusbar = self.statusBar()

        self.statusbar.showMessage("F1 - вызов помощи")

    # create structure bar
    # is not use
    def bar_category_file_menu(self):
        file_menu = self.menubar.addMenu('File')
        file_menu.addAction(QAction('', self))
        work_with_bd = self.menubar.addMenu('Data Base')
        work_with_bd.addAction(QAction('', self))
