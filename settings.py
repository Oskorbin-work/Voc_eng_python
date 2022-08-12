# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import os
from sys import platform
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------


# Setting address
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/'
ROOT_MAIN_DB = ROOT_DIR + "database" + '/' + 'data_word.sqlite'
#NAME_ACTIVE_TABLE = "Test_table"
NAME_ACTIVE_TABLE = "Main_table"

# Setting language words
LANGUAGE = ("ru", "en")
KEYBOARD_ENGLISH = '67699721'
KEYBOARD_RUSSIAN = '00000419'

# Setting language interface
LANGUAGE_INTERFACE_DIR = 'languages/'
LANGUAGE_INTERFACE_LIST = {
    "en": ROOT_DIR + LANGUAGE_INTERFACE_DIR + "language_en.xml",
    "ua": ROOT_DIR + LANGUAGE_INTERFACE_DIR + "language_ua.xml",
    "ru": ROOT_DIR + LANGUAGE_INTERFACE_DIR + "language_ru.xml",
}
STATUS_LANGUAGE_INTERFACE = "ru"
LANGUAGE_INTERFACE = LANGUAGE_INTERFACE_LIST[STATUS_LANGUAGE_INTERFACE]

# Setting timer
TIMER_INTERVAL = 1

# setting status learn words
PROGRAM_STATUS = True


# setting max random for old words
MAX_OLD_WORD = 10


# os platform
if platform == "linux" or platform == "linux2":
    PLATFORM = "Linux"
elif platform == "darwin":
    PLATFORM = "Apple"
elif platform == "win32":
    PLATFORM = "Windows"
else:
    PLATFORM = "Not found"
