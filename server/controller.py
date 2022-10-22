# Work with XML file
import functions.work_with_XML_file.work_with_XML as XML
import uuid
from settings import STATUS_LANGUAGE_INTERFACE
class ControllerServer():
    def __init__(self):
        self.list_status_session ={
            "Successfully completed": "Успішно завершено",
            "Partially completed": "Завершено частково",
            "Completed to no avail": "Завершено без користі",
            "Failed to complete": "Невдало завершено",
        }
        self.count_pause_control = -1
        self.check_count_pause_program()
        self.check_user_id()
        self.create_session()

    def check_temp_word(self,count_temp):
        XML.change_val_XML("server/data_xml/session.xml", "temp_word", str(count_temp))

    def check_activity_word(self,count_activity):
        XML.change_val_XML("server/data_xml/session.xml", "activate_word", str(count_activity))

    def check_not_activity_word(self, count_not_activity):
        XML.change_val_XML("server/data_xml/session.xml", "not_activate_word", str(count_not_activity))

    #  Сохраняет количество остановок программы
    def check_count_pause_program(self):
        self.count_pause_control = self.count_pause_control+1
        XML.change_val_XML("server/data_xml/session.xml", "count_pause_program", str(self.count_pause_control))

    def check_status_session(self, type_status):
        status_session = self.list_status_session[type_status]
        XML.change_val_XML("server/data_xml/session.xml", "status_session", str(status_session))

    def check_user_id(self):
        user_id = self.user_get_id()
        status_user_id = XML.get_attr_XML_server("server/data_xml/user.xml", "user_id")
        if status_user_id == "None":
            XML.set_val_XML("server/data_xml/user.xml", "user_id", user_id)
        elif status_user_id is None:
            XML.change_val_XML("server/data_xml/user.xml", "user_id", user_id)

    def user_get_id(self):
        # начальные цифры для определения что это айди пользователя
        # означает User
        user_start_id = "62927891-"
        user_finally_id = str(uuid.uuid1())
        user_id = user_start_id + user_finally_id
        return user_id

    def create_session(self):
        self.check_language()

    def get_end_information_about_session(self,list_info):
        self.get_timer = list_info[0]
        self.check_time(self.get_timer)
        self.get_all_word = list_info[1]
        self.check_all_word(self.get_all_word)

    def check_language(self):
        now_language = STATUS_LANGUAGE_INTERFACE
        XML.change_val_XML("server/data_xml/session.xml", "language", now_language)

    def check_time(self, time):
        XML.change_val_XML("server/data_xml/session.xml", "time", time)

    def check_all_word(self, all_word):
        XML.change_val_XML("server/data_xml/session.xml", "all_word", all_word)
