def format_file(text,width = 500):
    text_format = ''
    for word in text.split():
        if len(text_format.split('\n')[-1]) <width*0.1:
            text_format = text_format + ' ' + word
        else:
            text_format = text_format + '\n' + ' ' + word
    return text_format