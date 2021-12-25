# -----------------------------------------------------------
# PyQt 5.Initiate structure Main window and GUI
# -----------------------------------------------------------
from PyQt5.QtWidgets import QFrame

# Separates for status bar
class VLine(QFrame):
    # a simple VLine, like the one you get from designer
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine|self.Sunken)