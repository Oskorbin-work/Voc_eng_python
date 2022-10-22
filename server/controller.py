# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
import uuid


class ControllerServer():
    def __init__(self):
        # Пользователь
        # Уникальный айди пользователя
        self.check_user_id()

    def check_user_id(self):
        print(XML.get_attr_XML_server("server/data_xml/user.xml", "user_id"))
        user_id = self.user_get_id()
        status_user_id = XML.get_attr_XML_server("server/data_xml/user.xml", "user_id")
        if status_user_id is "None":
            XML.set_val_XML("server/data_xml/user.xml", "user_id", user_id)
        elif status_user_id == None:
            XML.change_val_XML("server/data_xml/user.xml", "user_id", user_id)

    def user_get_id(self):
        # начальные цифры для определения что это айди пользователя
        # означает User
        user_start_id = "62927891-"
        user_finally_id = str(uuid.uuid1())
        user_id = user_start_id + user_finally_id
        return user_id
