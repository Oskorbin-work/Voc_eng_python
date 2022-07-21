
from PyQt5.QtWidgets import QPushButton,QGridLayout,QDialog


class WrongWordInterface(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)

        modalgrid = QGridLayout(self)

        self.btn_unpack = QPushButton("Принять", self)
        self.btn_unpack.setFixedSize(150, 30)
        self.btn_unpack.clicked.connect(self.modalWinHide)
        modalgrid.addWidget(self.btn_unpack, 2, 0)

        self.btn_close = QPushButton("Отмена", self)
        self.btn_close.setFixedSize(150, 30)
        self.btn_close.clicked.connect(self.modalWinHide)
        modalgrid.addWidget(self.btn_close, 2, 1)

    def modalWinHide(self):
        self.close()