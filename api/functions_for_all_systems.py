# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
import settings
from functions.notifications import view_error_critical

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
                view_error_critical("Установите xkbswitch", "Oткройте файл READMI.MD. После чего следуйте инструкциям"
                                                            " установки необходимого моудуля в пункте один.")


        elif settings.PLATFORM == "Linux":
            pass