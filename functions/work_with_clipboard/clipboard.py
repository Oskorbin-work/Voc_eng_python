from pandas.io.clipboard import clipboard_get


def check_file(text):
    data = set(line.strip() for line in open('new_words.txt', 'r'))
    data.add(text)
    f = open('new_words.txt', 'w')
    for index, text_line in enumerate(sorted(data)):
        if index == len(data)-1:
            f.write(str(text_line))
        else:
            f.write(str(text_line) + '\n')

    f.close()


def copy_clipboard():
    text = clipboard_get()[:1].capitalize() + clipboard_get()[1:].lower()
    if text != "":
        check_file(text)


def clipboard():
    copy_clipboard()
