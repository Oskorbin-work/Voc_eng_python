from PyQt5.QtWidgets import QPushButton


class WrongWordButtons:
    def start_create_wrong_word_button(self):
        self.name_label_buttons()

    def name_label_buttons(self):
        self.btn_unpack = QPushButton("В главное меню", self)
        self.btn_voice_wrong = QPushButton("Озвучить текст", self)
