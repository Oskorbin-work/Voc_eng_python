# -----------------------------------------------------------
# Work with XML-file
# -----------------------------------------------------------
import xml.etree.ElementTree as ET
# -----------------------------------------------------------
# Other library
# -----------------------------------------------------------
import os
import settings


def get_language(name="current_language"):
    path = settings.ROOT_DIR + settings.PATH_SETTING

    try:
        root_conf = ET.parse(path).getroot()
    except Exception:
        return path + " має помилки або не існує "

    if root_conf.find(name) is not None:
        return root_conf.find(name).text
    else:
        return " Тег " + name + " не існує в файлі " + path
def get_attr_XML(name):
    path = settings.LANGUAGE_INTERFACE
    try:
        root_conf = ET.parse(path).getroot()
    except Exception:
        return settings.STATUS_LANGUAGE_INTERFACE+".xml" + " має помилки або не існує "

    if root_conf.find(name) is not None:
        return root_conf.find(name).text
    else:
        return " Тег " + name + " не існує в файлі " + settings.STATUS_LANGUAGE_INTERFACE+".xml"

def change_val_XML(path, val,new_val):
    root_change = ET.parse(path)
    for t in root_change.iterfind(val):
        t.text = new_val
    root_change.write(path, encoding="UTF-8", xml_declaration=True)