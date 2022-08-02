# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
from elements.table_views import TableViews


# Class that create wrong table and fill their
class WrongTable(TableViews):

    # fill wrong table
    def fill_table_wrong(self, text_check, list_now_word, random_language_now):
        self.text_check = text_check
        self.list_now_word = list_now_word
        self.random_language_now = random_language_now
        self.default_name_label_wrong()
        self.add_items_to_dict_table(self.loop_description_all_row())
        self.add_items_from_dict_to_table()
        self.table_form.resizeColumnsToContents()

    # this method save default label in table. One column
    def default_name_label_wrong(self):
        self.default_name_label_text_check = "Ваш перевод"
        self.default_name_label_truth_translate_word = "Правильный перевод"
        self.default_name_label_part_of_a_word = "Часть слова"
        self.default_name_label_definition = "Дефиниция"
        self.default_name_label_theme = "Тема"

    # return word in russian or english word
    def determine_status_lang_word(self, flag_now_language=True):
        """
        flag_now_language has choice:
        1) True -- now choice translate word
        2) False -- now not choice translate word
        """
        if self.random_language_now == "en":
            if flag_now_language:
                return self.list_now_word[1]
            else:
                return self.list_now_word[2]
        elif self.random_language_now == "ru":
            if flag_now_language:
                return self.list_now_word[2]
            else:
                return self.list_now_word[1]

    # one row.
    def description_wrong_word(self):
        """
        Wrong translate
        """
        description_name_label_text_check = "Ваш перевод"
        content_name_label_text_check = self.text_check
        return {f'{description_name_label_text_check}': content_name_label_text_check}

    # two row.
    def description_true_word_and_translate(self):
        """
        Wrong translate
        """
        description_name_label_truth_translate_word = "Правильный перевод слова "
        content_name_label_truth_translate_word = self.determine_status_lang_word(False)
        return {f'{description_name_label_truth_translate_word}': content_name_label_truth_translate_word}

    # three row.
    def description_part_of_a_word(self):
        """
        Wrong translate word
        """
        description_name_label_part_of_a_word = "Часть слова"
        content_name_label_part_of_a_word = self.list_now_word[3]
        return {f'{description_name_label_part_of_a_word}': content_name_label_part_of_a_word}

    # four row.
    def description_transcription(self):
        """
        description transcription word
        """
        description_transcription = "Транскрипция"
        content_transcription = self.list_now_word[4]
        return {f'{description_transcription}': content_transcription}

    # five row.
    def description_definition(self):
        """
        description definition word
        """
        description_name_label_definition = "Дефиниция"
        content_name_label_definition = self.list_now_word[5]
        return {f'{description_name_label_definition}': content_name_label_definition}

    # six row.
    def description_theme_word(self):
        """
        Theme word or too translate word
        """
        description_name_label_theme = "Тема"
        content_name_label_theme = self.list_now_word[7]
        return {f'{description_name_label_theme}': content_name_label_theme}

    # add rows and columns to table
    def loop_description_all_row(self):
        list_description_all_row = list()
        list_description_all_row.append(self.description_wrong_word())
        list_description_all_row.append(self.description_true_word_and_translate())
        list_description_all_row.append(self.description_part_of_a_word())
        list_description_all_row.append(self.description_transcription())
        list_description_all_row.append(self.description_definition())
        list_description_all_row.append(self.description_theme_word())
        return list_description_all_row


