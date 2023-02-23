import random
import re

def count_lines(filename="functions/work_with_clipboard/new_words.txt", chunk_size=1<<13):
    with open(filename) as f:
        line_count = 0
        for line in f:
            if (re.search(r"^[^\\+]",line[0:-2])):
                line_count += 1

    return line_count

def random_value():
    return search_word(random.randint(0,count_lines()))

def search_word(random_value):
    with open("functions/work_with_clipboard/new_words.txt") as f:
        n = 0
        for line in f:
            n += 1
            if n == random_value:
                return line[0:-1]

