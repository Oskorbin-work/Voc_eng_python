
from database.sql_query_bd import WorkWithBd


def old_data():

    Lines = open('database/old_program/List of words.txt', 'r')

    for line in Lines:
        list = line.split("/", 6)
        list[6] = list[6].strip("\n")
        WorkWithBd.insert_row(WorkWithBd, list)