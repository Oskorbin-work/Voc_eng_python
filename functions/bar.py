# -----------------------------------------------------------
# PyQt 5.Initiate structure Main window and GUI
# -----------------------------------------------------------
from PyQt5.QtWidgets import QLabel, QAction, QFrame
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from elements.Vline import VLine

#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.wcLabel = QLabel('Error')
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.elements_status_bar = dict()
        self.elements_for_status_bar()
        self.status_bar_structure()

    def elements_for_status_bar(self):
        self.elements_status_bar['Help'] = QLabel("F1 - Допомога")

    # create structure statusbar
    def status_bar_structure(self):
        for i in self.elements_status_bar:
            self.statusbar.addWidget(self.elements_status_bar[i])
            self.statusbar.addWidget(VLine())

    #create structure menubar
    # is not use
    def bar_category_file_menu(self):
        file_menu = self.menubar.addMenu('File')
        file_menu.addAction(QAction('', self))
        work_with_bd = self.menubar.addMenu('Data Base')
        work_with_bd.addAction(QAction('', self))
