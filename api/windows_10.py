
import settings

if settings.PLATFORM == "Windows":
    import win32api


    class Windows10:
        def change_language(self, language="ru"):
                if language == "en":
                    win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_RUSSIAN}', 1)
                elif language == "ru":
                    win32api.LoadKeyboardLayout(f'{settings.KEYBOARD_ENGLISH}', 1)
