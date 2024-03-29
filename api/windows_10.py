# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from functions.notifications import view_error_critical
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

if settings.PLATFORM == "Windows":
    import win32api

    class Windows10:
        def change_language(self, language="ru"):
            try:
                if language == "en":
                    win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_RUSSIAN}', 1)
                elif language == "ru":
                    win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_ENGLISH}', 1)
            except:
                view_error_critical(XML.get_attr_XML("error_sector/language_keyboard/windows_10/change_language"))
