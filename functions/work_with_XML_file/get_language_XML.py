# -----------------------------------------------------------
# Work with XML-file
# -----------------------------------------------------------
import xml.etree.ElementTree as ET

def get_language(path, name="current_language"):

    try:
        root_conf = ET.parse(path).getroot()
    except Exception:
        return path + " має помилки або не існує "

    if root_conf.find(name) is not None:
        return root_conf.find(name).text
    else:
        return " Тег " + name + " не існує в файлі " + path