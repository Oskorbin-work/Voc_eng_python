import pyttsx3
import os
import settings


# class for voice in Window 10
class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()

# voice text
def voice(text):
    text = text[0][0]
    # class for voice in Mac
    if settings.PLATFORM == "Apple":
        os.system("/usr/bin/say " + text)
    # class for voice in Window 10
    elif settings.PLATFORM == "Windows":
        tts = _TTS()
        tts.start(text)
        del (tts)
