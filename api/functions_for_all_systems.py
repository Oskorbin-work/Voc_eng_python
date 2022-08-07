# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from functions.notifications import view_error_critical
# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML

# import module for OS
if settings.PLATFORM == "Windows":
    from api.windows_10 import Windows10
elif settings.PLATFORM == "Apple":
    from api.mac import Mac


class FuncForAllSystems:
    def change_language(self,language):
        # Program run on Windows
        if settings.PLATFORM == "Windows":
            Windows10.change_language(Windows10, language)
        elif settings.PLATFORM == "Apple":
            try:
                Mac.change_language(Mac, language)
            except:
                view_error_critical(XML.get_attr_XML("error_sector/xkbswitch_not_fount/short_description_error"),
XML.get_attr_XML("error_sector/xkbswitch_not_fount/long_description_error"))
        elif settings.PLATFORM == "Linux":
            pass