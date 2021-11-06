# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QMessageBox

# View QMessageBox about error
# (Example about failed sql request)
def view_error_critical(title, text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.exec_()

# view info_transcription
def view_info_transcription(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Дефиниция")
    msg.setText("Дефиниция:\n" + str(text))
    msg.exec_()

# view help
def view_help():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Enter - Проверить слово\n"
                "F2 - Старт/Пауза\n"
                "⌥ - Вывод транскрипции\n"
                "⌘ - Озвучка слова \n")
    msg.exec_()