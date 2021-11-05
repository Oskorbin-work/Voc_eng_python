from pandas.io.clipboard import clipboard_get


def check_file(text):
    data = set(line.strip() for line in open('new_words.txt', 'r'))

    if not(text in data):
        print(text + "\n")

    data.add(text)
    f = open('new_words.txt', 'w')
    for index, text_line in enumerate(sorted(data)):
        if index == len(data)-1:
            f.write(str(text_line))
        else:
            f.write(str(text_line) + '\n')

    f.close()


def copy_clipboard(buffer):
    text = buffer[:1].capitalize() + buffer[1:].lower()
    if text != "":
        check_file(text)


def clipboard():
    buffer = clipboard_get()
    if str(type(buffer)) == "<class 'objc.pyobjc_unicode'>":
        copy_clipboard(buffer)
