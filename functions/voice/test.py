import pyttsx3
import time

from database.sql_query_bd import WorkWithBd

list = WorkWithBd.get_english_word(WorkWithBd)
sett = set(list)
engine = pyttsx3.init()
for index, text in enumerate(sett):
    print(text[0])
    engine.say(text[0] + ". ")
    engine.runAndWait()

    if index == 10:
        break




