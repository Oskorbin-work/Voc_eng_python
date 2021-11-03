from pandas.io.clipboard import clipboard_get


def check_file(text):
    data = set(line.strip() for line in open('new_words.txt','r'))
    data.add(text)
    f = open('new_words.txt','w')
    for index in sorted(data):
        f.write(index + '\n')

    f.close()


def copy_clipboard():
    text = clipboard_get()[:1].capitalize() + clipboard_get()[1:].lower()
    if text != "":
        check_file(text)


def clipboard():
    copy_clipboard()
