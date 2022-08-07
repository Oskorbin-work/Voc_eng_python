# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
import sqlite3

# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from functions.notifications import view_error_critical
from settings import ROOT_MAIN_DB
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# Decorator for update query the database
def request_bd_update(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical(XML.get_attr_XML("error_sector/database/label_not_working_sql"), func(*args, **kwargs))
        return 0  # The comparison
    return wrapper


# Decorator for select query the database
def request_bd_select(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            value = (cur.fetchall())[0]
            conn.close()
        except sqlite3.Error:
            view_error_critical(XML.get_attr_XML("error_sector/database/label_not_working_sql"), func(*args, **kwargs))
            value = XML.get_attr_XML("error_sector/database/label_value")
        return value
    return wrapper


# Decorator for insert query the database
def request_bd_insert(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            conn.commit()
            conn.close()
        except sqlite3.Error:
            view_error_critical(XML.get_attr_XML("error_sector/database/label_not_working_sql"), func(*args, **kwargs))
        return 0  # The comparison
    return wrapper


# Decorator for select query the database
def request_bd_select_all(func):
    def wrapper(*args, **kwargs):
        try:
            conn = sqlite3.connect(ROOT_MAIN_DB)
            cur = conn.cursor()
            cur.execute(func(*args, **kwargs))
            value = (cur.fetchall())
            conn.close()
        except sqlite3.Error:
            view_error_critical(XML.get_attr_XML("error_sector/database/label_not_working_sql"), func(*args, **kwargs))
            value = XML.get_attr_XML("error_sector/database/label_value")
        return value
    return wrapper