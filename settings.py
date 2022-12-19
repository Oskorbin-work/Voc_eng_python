# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import os
from sys import platform
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------


from functions.work_with_XML_file.get_language_XML import get_language
# path to other files
PATH_SETTING = "another_windows/setting/label_settings.xml"

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

# language_setting.xml have error => set default language
DEFAULT_LANGUAGE_INTERFACE = "ua"

# set language
STATUS_LANGUAGE_INTERFACE = get_language(ROOT_DIR + PATH_SETTING) if get_language(ROOT_DIR + PATH_SETTING) in LANGUAGE_INTERFACE_LIST.keys()\
    else DEFAULT_LANGUAGE_INTERFACE
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
