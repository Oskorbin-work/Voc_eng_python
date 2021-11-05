import pyttsx3

from database.sql_query_bd import WorkWithBd

list = {index[0] for index in WorkWithBd.get_english_word(WorkWithBd)}
sett = set(list)
engine = pyttsx3.init()
for index, text in enumerate(sett):
    print(text)
    engine.say(text + ". ")
    engine.runAndWait()

    if index == 10:
        break




