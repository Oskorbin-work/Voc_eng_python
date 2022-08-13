# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QAction
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from elements.Vline import VLine
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
from emoji import emojize
from functions.menubar.menu_bar import MenuMain


#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.elements_status_bar = dict()
        self.elements_for_status_bar()
        self.status_bar_structure()
        #self.bar_category_file_menu()

    def elements_for_status_bar(self):
        # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.elements_status_bar['Help'] = [QLabel(XML.get_attr_XML("bar/label_help")), VLine()]
        # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.elements_status_bar['All_word'] = [QLabel(emojize(':books:')), QLabel("0")]
        self.elements_status_bar['Activity'] = [QLabel(emojize(':bullseye:')), QLabel("0")]

        self.elements_status_bar['Not_Activity'] = [QLabel(emojize(':military_medal:')), QLabel("0"), VLine()]
        # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        self.elements_status_bar['Last_word'] = [QLabel(XML.get_attr_XML("bar/last_words")), QLabel("0")]
        self.elements_status_bar['0_hp'] = [QLabel(emojize(':check_mark_button:')), QLabel("0")]
        self.elements_status_bar['1_hp'] = [QLabel(emojize(':keycap_1:')), QLabel("0")]
        self.elements_status_bar['1_hp'][0].setFont(QFont("Apple Color Emoji"))
        self.elements_status_bar['2_hp'] = [QLabel(emojize(':keycap_2:')), QLabel("0")]
        self.elements_status_bar['2_hp'][0].setFont(QFont("Apple Color Emoji"))
        self.elements_status_bar['3_hp'] = [QLabel(emojize(':keycap_3:')), QLabel("0"),VLine()]
        self.elements_status_bar['3_hp'][0].setFont(QFont("Apple Color Emoji"))
        # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    # create structure statusbar
    def status_bar_structure(self):
        for list_widgets in self.elements_status_bar:
            for widget in self.elements_status_bar[list_widgets]:
                self.statusbar.addWidget(widget)

    def data_status_bar_static_words(self, *args):
        self.elements_status_bar['All_word'][1].setText(args[0])
        self.elements_status_bar['Activity'][1].setText(args[1])
        self.elements_status_bar['Not_Activity'][1].setText(args[2])

    def data_status_bar_hp(self, *args):
        self.elements_status_bar['Last_word'][1].setText(args[0])
        self.elements_status_bar['0_hp'][1].setText(args[1])
        self.elements_status_bar['1_hp'][1].setText(args[2])
        self.elements_status_bar['2_hp'][1].setText(args[3])
        self.elements_status_bar['3_hp'][1].setText(args[4])
    #create structure menubar
    # is not use
    def bar_category_file_menu(self):
        file_menu = self.menubar.addMenu('File')
        exitAction = QAction('Exit', self)
        file_menu.addAction(exitAction)
        exitAction.setMenuRole(QAction.NoRole)
        work_with_bd = self.menubar.addMenu('Data Base')
        work_with_bd.addAction(QAction('', self))
