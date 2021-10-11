# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import os
from sys import platform
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------

# setting address
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'
ROOT_MAIN_DB = ROOT_DIR + "database" + '/' + 'data_word.sqlite'

# Setting language
LANGUAGE = ("ru", "en")
KEYBOARD_ENGLISH = '67699721'
KEYBOARD_RUSSIAN = '00000419'

# Setting timer
TIMER_INTERVAL = 1

# setting status learn words
PROGRAM_STATUS = True

# setting random for old words
RANDOM_OLD_WORD = 0.05

# os platform
if platform == "linux" or platform == "linux2":
    PLATFORM = "Linux"
elif platform == "darwin":
    PLATFORM = "Apple"
elif platform == "win32":
    PLATFORM = "Windows"
else:
    PLATFORM = "Not found"
