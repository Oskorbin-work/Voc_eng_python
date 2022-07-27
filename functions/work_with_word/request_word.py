import requests
from bs4 import BeautifulSoup
import re
from tabulate import tabulate
import eng_to_ipa
from functions.work_with_clipboard.colour_console import bcolors
from database.sql_query_bd import WorkWithBd


class Word():
    id = ["id"]
    en = ["Слово на англ"]
    ru = ["Слово на русском"]
    transcription = ["Транскрипция"]
    pronoun = ["Местоимение"]
    definition = ["Дефиниция"]
    count_life = ["Количество жизней"]
    other_information = ["Разная информация"]
    work_count_life = ["Рабочие жизни"]
    status_word = ["Статус слова"]
    count_true_attempt = ["Количество попыток слова"]

    def set(self):
        Word.id = ["id"]
        Word.en = ["Слово на англ"]
        Word.ru = ["Слово на русском"]
        Word.transcription = ["Транскрипция"]
        Word.pronoun = ["Местоимение"]
        Word.definition = ["Дефиниция"]
        Word.count_life = ["Количество жизней"]
        Word.other_information = ["Разная информация"]
        Word.work_count_life = ["Рабочие жизни"]
        Word.status_word = ["Статус слова"]
        Word.count_true_attempt = ["Количество попыток слова"]


list_words = list()


def enter_word():
    enter_word = input().replace(" ","+")
    enter_word = enter_word.lower()
    #enter_word = "usa"
    #https://dictionary.cambridge.org/dictionary/english-russian/red
    return 'https://dictionary.cambridge.org/dictionary/english-russian/'\
           + enter_word.replace(" ", "+")

def request_all_link(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/94.0.4606.71 Safari/537.36'
    }
    resp = requests.get(link, headers=headers)
    return BeautifulSoup(resp.content, 'lxml')

def get_ru(el):
    if el.contents[0][-1] == " ":
        el.contents[0] = el.contents[0][:-1]
    return el.contents[0].capitalize() if hasattr(el, 'contents') else None

def get_en(el):
    sep = ","
    word_en = el.contents[0].capitalize() if hasattr(el, 'contents') else "None"
    word_en = word_en.split(sep, 1)[0]
    return word_en


def gen_name_en_3(el_soup, el_list, default_value):
    if el_list == "dsense-noh":
        span_en = el_soup.find("span", {"class": 'phrase-title dphrase-title'})
        try:
            return get_en(span_en.find(("b")))
        except AttributeError:
            return get_en(default_value)

def get_definition(el):
    definition = ""
    for i in el:
        #print(i)
        if re.findall(r"</span>", str(i)) == ['</span>']:
            big_tag = re.findall(r">(.+?)<a ", str(i))[0]
            list_rr = re.findall(r">(\w*)</a>", str(i))
            big_tag = big_tag + (' '.join([str(elem) for elem in list_rr]))
            big_tag = big_tag + re.findall(r"(?s:.*)</a>(.*)</span>", str(i))[0]
            definition = definition + big_tag
        elif re.findall(r"</a>", str(i)) == ['</a>']:
            definition = definition + re.findall(r">(\w*)</a>", str(i))[0]
        elif re.findall(r"abbreviation for",str(i)):
            print(i)
        else:
            definition = definition + i
    return  definition.capitalize()


def get_other_information(el):
    return str(el.span.contents[0])

def get_all(el, default_value='', type=''):
    el_soup = BeautifulSoup(str(el), "lxml")
    if type == "ru":
        return get_ru(el_soup.find("span", {"class": 'trans dtrans dtrans-se'}))
    elif type == "other_information":
        if el_soup.find("span", {"class": 'guideword dsense_gw'}) is not None:
            return get_other_information(el_soup.find("span", {"class": 'guideword dsense_gw'}))
        else:
            return "-"
    elif type == "definition":
        return get_definition(el_soup.find("div", {"class": 'def ddef_d db'}))
    elif len(el['class']) == 2:
        if type == "en":
            return get_en(el_soup.find("span", {"class": 'hw dsense_hw'}))
        if type == "pronoun":
            return default_value
    elif len(el['class']) == 3:
        if type == "en":
            return gen_name_en_3(el_soup, el['class'][2], default_value)
        if type == "pronoun":
                    if " " in str(gen_name_en_3(el_soup, el['class'][2], default_value)):
                        return "phrasal verb"
                    else:
                        return default_value

def get_block_name(pos_body):
    default_value_name = pos_body.find("span", {"class": 'hw dhw'})
    default_value_pronoun = pos_body.find("span", {"class": 'pos dpos'}).getText()
    default_value_trans = pos_body.find("span", {"class": 'ipa dipa lpr-2 lpl-1'}).getText()
    pr_dsense_list = pos_body.find_all("div", {"class":  re.compile('^pr dsense')})
    default_value_count_life = 3
    default_value_status_word = "is_activate"
    default_value_count_true_attempt = 0
    for el in pr_dsense_list:
        try:
            list_words[-1].id.append("null")
        except:
            print("Сломался айди слова (Указывается дефолтн. слово)" + default_value_name)
        list_words[-1].en.append(get_all(el, default_value_name, "en"))
        list_words[-1].ru.append(get_all(el, default_value_name, "ru"))
        list_words[-1].transcription.append(eng_to_ipa.convert(list_words[-1].en[-1]).replace("*",""))
        list_words[-1].pronoun.append(get_all(el, default_value_pronoun, "pronoun"))
        list_words[-1].definition.append(get_all(el, default_value_pronoun, "definition"))
        list_words[-1].count_life.append(default_value_count_life)
        list_words[-1].other_information.append(get_all(el, default_value_pronoun, "other_information"))
        list_words[-1].work_count_life.append(default_value_count_life)
        list_words[-1].status_word.append(default_value_status_word)
        list_words[-1].count_true_attempt.append(default_value_count_true_attempt)

def check_word_in_bd(word):
    list_en_word = list(t[0] for t in WorkWithBd.get_all_english_word(WorkWithBd))
    if word in list_en_word:
        return bcolors.WARNING+ "Слово уже есть в бд. Не добавляй." + bcolors.ENDC
    else:
        return bcolors.OKGREEN +"Это новое слово. Можно добавлять."+ bcolors.ENDC

while True:
    print("Введите слово:")
    link = enter_word()
    print("\n\n\n\n\n\n\n")
    soup = request_all_link(link)
    try:
        name = soup.find("span", {"class":  'hw dhw'}).text.capitalize()
    except AttributeError:
        print("Слова не существует по данной ссылке:")
        print(link)
        continue
    list_words.append(Word)
    pos_body = soup.find_all("div", {"class": 'pr entry-body__el'})
    if len(pos_body) >= 1:
        try:
            get_block_name(pos_body[0])
        except Exception as e :
            print("Первый блок сломался")
            print(e)
    if len(pos_body) >= 2:
        try:
            get_block_name(pos_body[1])
        except:
            print("Второй блок сломался")

    list_words_all_column = [
        list_words[-1].id,
        list_words[-1].en,
        list_words[-1].ru,
        list_words[-1].pronoun,
        list_words[-1].transcription,
        list_words[-1].definition,
        list_words[-1].count_life,
        list_words[-1].other_information,
        list_words[-1].work_count_life,
        list_words[-1].status_word,
        list_words[-1].count_true_attempt,

        ]
    print("ТАБЛИЦА 1")
    print(tabulate(list_words_all_column, tablefmt="grid"))
    dict_words_all_row = {
        "name_column": ["№"],
    }
    count = len(list_words[-1].id)-1
    for i in range(count):
        dict_words_all_row["word "+str(i)] = [i+1]

    for i in list_words_all_column:
        dict_words_all_row["name_column"].append(i[0])
    for i in list_words_all_column:

        for j in range(count):

            dict_words_all_row["word " + str(j)].append(i[j+1])


    list_words_all_row = [dict_words_all_row["name_column"]]
    for i in range(count):
        list_words_all_row.append(dict_words_all_row["word " + str(i)])
    print("ТАБЛИЦА 2")
    print(tabulate(list_words_all_row, tablefmt="grid"))
    print("ВИД КАК SQL-ЗАПРОСЫ:")
    for i in range(count):
        sql_request = str(i+1) +")\n INSERT INTO Main_table \n VALUES ("
        for j in dict_words_all_row["word " + str(i)][1:]:

            if j == "null":
                sql_request += "null, "
            elif type(j) is str:
                sql_request += "'" + j + "', "
            elif type(j) is int:
                sql_request += str(j) + ", "
        sql_request = sql_request[:-2]+ ");"
        print(sql_request)
        sql_request = ""

    print(check_word_in_bd(list_words[-1].en[-1]))
    list_words[-1].set(Word)
    print("Ссылка для проверки: " + link)
    del list_words[-1]
    # VALUES (null, 'Screw up', 'Заваливать', 'phrasal verb', 'skruː ʌp',
    # 'to make a mistake, or to spoil something'
    # , 3, 'A2',3, 'is_activate', 1);
