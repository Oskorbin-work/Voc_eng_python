from PyQt5 import QtWidgets, QtCore # Импортируем необходимые библиотеки;
import sys



def show_modal_window(): # Создаем фунцкию;
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.Window)
    modalWindow.setWindowTitle('Модальное окно')
    modalWindow.resize(200, 50)
    modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center() - modalWindow.rect()
                     .center() - QtCore.QPoint(40, 30))
    modalWindow.show()

app = QtWidgets.QApplication(sys.argv)
window1 = QtWidgets.QWidget() # Создает окно;
window1.setWindowTitle('Обычное окно')
window1.resize(300, 100)
btn = QtWidgets.QPushButton('Открыть модальное окно')
btn.clicked.connect(show_modal_window)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(btn)
window1.setLayout(vbox)
window1.show()


window2 = QtWidgets.QWidget()
window2.setWindowTitle('БЛОКИРОВАНО') # Это окно не будет блокировано при WindowModal;
window2.resize(500, 100)
window2.show()
sys.exit(app.exec_())