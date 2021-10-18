import settings

if settings.PLATFORM == "Apple":
    import os


class Mac:
    def change_language(self, language):
        try:
            if language == "en":
                os.system("xkbswitch -se RussianWin")
            elif language == "ru":
                os.system("xkbswitch -se ABC")
        except:
            print("error mac")
