# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QAction
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------


class MenuMain:

    def __init__(self):
        self.menubar = self.menuBar()
        file_menu = self.menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        file_menu.addAction(exitAction)
        exitAction.setMenuRole(QAction.NoRole)
        work_with_bd = self.menubar.addMenu('Data Base')
        work_with_bd.addAction(QAction('', self))
