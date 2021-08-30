import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFrame


class main_windows(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_window_parameter()
        self.main_structure()

    def main_window_parameter(self):  # place to main setting "view window"
        self.showMaximized()

    def main_structure(self): # Initiate structure
        self.form_frame = QFrame()
        self.form_frame.setFrameShape(QFrame.StyledPanel)
        self.ver_frame = QFrame()
        self.ver_frame.setFrameShape(QFrame.StyledPanel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main_windows()
    sys.exit(app.exec_())