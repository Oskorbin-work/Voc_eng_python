
from database.work_with_bd import WorkWithBd

def test ():
    Lines = open('database/old_program/List of words.txt', 'r')

    for line in Lines:
        list = line.split("/", 6)
        list[6] = list[6].strip("\n")
        print(WorkWithBd.insert_row(WorkWithBd, list))
        break
        print([str(i) + ") " + x for i, x in enumerate(list)])
