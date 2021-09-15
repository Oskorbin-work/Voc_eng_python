# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sqlite3

# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from list_error import view_error_critical
from settings import ROOT_DIR


# Decorator for update query the database
def request_bd_update(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical("Not working sql:", func(*args, **kwargs))
        return 0  # The comparison
    return wrapper


# Decorator for select query the database
def request_bd_select(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_DIR + "database" + '\\' + 'data_word.sqlite')
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            value = (cur.fetchall())[0]
            conn.close()
        except sqlite3.Error:
            view_error_critical("Not working sql:", func(*args, **kwargs))
            value = "Error"
        return value
    return wrapper