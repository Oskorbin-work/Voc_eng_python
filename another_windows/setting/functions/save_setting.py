# -----------------------------------------------------------
# Other library
# -----------------------------------------------------------
import os
# settings program
from settings import STATUS_LANGUAGE_INTERFACE, ROOT_DIR, PATH_SETTING
# work with XML file
import functions.work_with_XML_file.work_with_XML as XML
# notifications
from functions.notifications import view_info_question,view_info_information
class SaveSetting():

    def set_language(self,status):
        if (status == False):
            root_change = os.path.join(ROOT_DIR, PATH_SETTING)
            XML.change_val_XML(root_change,'current_language',self.combo_box_language.currentText())

    def check_language(self):
        if self.combo_box_language.currentText() != STATUS_LANGUAGE_INTERFACE:
           return False
        else:
            return True

    def call_notification_save(self):
        return view_info_question(
            XML.get_attr_XML("notifications/save_button/name"),
            XML.get_attr_XML("notifications/save_button/question"),
            XML.get_attr_XML("notifications/save_button/choice/yes"),
            XML.get_attr_XML("notifications/save_button/choice/no"))


    def call_notification_about_restore_program(self):
        return view_info_information(
            XML.get_attr_XML("notifications/save_button/notification_window/title"),
            XML.get_attr_XML("notifications/save_button/notification_window/text"),
        )
    def save_all(self):
        status_save = self.call_notification_save()
        print(status_save)
        if  status_save == XML.get_attr_XML("notifications/save_button/choice/yes"):
            self.set_language(self.check_language())
            self.check_language()
            self.call_notification_about_restore_program()