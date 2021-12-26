# -----------------------------------------------------------
# PyQt 5.Initiate structure Main window and GUI
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QAction
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from elements.Vline import VLine
from emoji import emojize
#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.wcLabel = QLabel('Error')
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.statusbar_1 = self.statusBar()
        self.elements_status_bar = dict()
        self.elements_for_status_bar()
        self.status_bar_structure()

    def elements_for_status_bar(self):
        self.elements_status_bar['Help'] = QLabel("F1 - Помощь")
        self.elements_status_bar['Help_vline'] = VLine()
        self.elements_status_bar['Last_word'] = QLabel("Осталось: 6")
        self.elements_status_bar['0_hp'] = QLabel("\u2705 0")
        self.elements_status_bar['1_hp_emoji'] = QLabel(emojize(':keycap_1:'))
        self.elements_status_bar['1_hp_emoji'].setFont(QFont("Apple Color Emoji"))
        self.elements_status_bar['1_hp_text'] = QLabel("1")
        self.elements_status_bar['2_hp_emoji'] = QLabel(emojize(':keycap_2:'))
        self.elements_status_bar['2_hp_emoji'].setFont(QFont("Apple Color Emoji"))
        self.elements_status_bar['2_hp_text'] = QLabel("2")
        self.elements_status_bar['3_hp_emoji'] = QLabel(emojize(':keycap_3:'))
        self.elements_status_bar['3_hp_emoji'].setFont(QFont("Apple Color Emoji"))
        self.elements_status_bar['3_hp_text'] = QLabel("3")
        self.elements_status_bar['hp_vline'] = VLine()

    # create structure statusbar
    def status_bar_structure(self):
        for i in self.elements_status_bar:
            self.statusbar.addWidget(self.elements_status_bar[i])

    #create structure menubar
    # is not use
    def bar_category_file_menu(self):
        file_menu = self.menubar.addMenu('File')
        file_menu.addAction(QAction('', self))
        work_with_bd = self.menubar.addMenu('Data Base')
        work_with_bd.addAction(QAction('', self))
