import sys

from PyQt5.QtWidgets import QApplication,QMainWindow, QTableWidget, QTableWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Test')
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(3)
        for j in range(table.rowCount()):
            for k in range(table.columnCount()):
                table.setItem(j, k, QTableWidgetItem("{}{}".format(j, k)))
        self._centralWidget = table
        self.setCentralWidget(self._centralWidget)
        self.resize(500, 200)


def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    view.setStyleSheet("QTableWidget::item {border: 0px; padding: 5px;}")
    view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()