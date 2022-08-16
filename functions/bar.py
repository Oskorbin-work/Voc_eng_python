# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QAction
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from elements.Vline import VLine
from functions.notifications import exit_program
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# -----------------------------------------------------------
# Import other modules
# -----------------------------------------------------------
from emoji import emojize


#  In class "Bar" -- menuBar in main program
class Bar:
    def __init__(self):  # Initiate menuBar
        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()
        self.control_menu_bar()
        self.elements_status_bar = dict()
        self.elements_for_status_bar()
        self.status_bar_structure()

    # label for status bar
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
        self.elements_status_bar['3_hp'] = [QLabel(emojize(':keycap_3:')), QLabel("0"), VLine()]
        self.elements_status_bar['3_hp'][0].setFont(QFont("Apple Color Emoji"))
        # ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

    # create structure statusbar
    def status_bar_structure(self):
        for list_widgets in self.elements_status_bar:
            for widget in self.elements_status_bar[list_widgets]:
                self.statusbar.addWidget(widget)

    # update a label status bar sector "words"
    def data_status_bar_static_words(self, *args):
        self.elements_status_bar['All_word'][1].setText(args[0])
        self.elements_status_bar['Activity'][1].setText(args[1])
        self.elements_status_bar['Not_Activity'][1].setText(args[2])

    # update a label status bar sector "hp words"
    def data_status_bar_hp(self, *args):
        self.elements_status_bar['Last_word'][1].setText(args[0])
        self.elements_status_bar['0_hp'][1].setText(args[1])
        self.elements_status_bar['1_hp'][1].setText(args[2])
        self.elements_status_bar['2_hp'][1].setText(args[3])
        self.elements_status_bar['3_hp'][1].setText(args[4])

    # ------------------------------------------------------------------------
    # sector menu bar

    # main table
    def control_menu_bar(self):
        self.tab_main_menu()

    # first tab in menu bar
    def tab_main_menu(self):
        # name tab
        name_main_menu = XML.get_attr_XML("menu_bar/tab_main_menu/name_tab")
        self.main_menu = self.menubar.addMenu(name_main_menu)
        # row that exit program
        self.main_row_exit()

    # row that exit program
    def main_row_exit(self):
        name_exit_action = XML.get_attr_XML("menu_bar/tab_main_menu/rows_tab/row_exit_program")
        self.exitAction = QAction(name_exit_action, self)
        self.exitAction.setMenuRole(QAction.NoRole)
        self.main_menu.addAction(self.exitAction)
        self.exitAction.triggered.connect(self.func_main_row_exit)

    # add function to "row that exit program"
    def func_main_row_exit(self):
        name = XML.get_attr_XML("notifications/exit_program/name")
        question = XML.get_attr_XML("notifications/exit_program/question")
        yes = XML.get_attr_XML("notifications/exit_program/choice/yes")
        no = XML.get_attr_XML("notifications/exit_program/choice/no")
        test = exit_program(name, question, yes, no)
        if test == yes:
            self.close()

    # ------------------------------------------------------------------------
