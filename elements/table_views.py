# -----------------------------------------------------------
# Import classical and Pyqt5`s modules
# -----------------------------------------------------------
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


# Class for create table. Used as structure table
class TableViews:
    def __init__(self,
                 column_count,
                 row_count,
                 vertical_header_set_visible=False,
                 horizontal_header_set_visible=False,
                 horizontal_header_set_stretch_last_section=False,
                 vertical_header_set_stretch_last_section=False):
        self.table_form = QTableWidget(row_count, column_count)
        self.table_form.setRowCount(row_count)
        self.table_form.setColumnCount(column_count)
        self.use_vertical_header_set_visible(vertical_header_set_visible)
        self.use_horizontal_header_set_visible(horizontal_header_set_visible)
        self.use_horizontal_header_set_stretch_last_section(horizontal_header_set_stretch_last_section)
        self.use_vertical_header_set_stretch_last_section(vertical_header_set_stretch_last_section)

        # dict for fill content table
        self.content_from_table = dict()

    # Attributes table
    # --------------------------------------------------------------------------------
    # set visible vertical header
    def use_vertical_header_set_visible(self, status):
        """
        :param status: True or False
        :return:
            True -- visible
            False -- not visible
        """
        self.table_form.verticalHeader().setVisible(status)

    # set visible horizontal header
    def use_horizontal_header_set_visible(self, status):
        """
        :param status: True or False
        :return:
            True -- visible
            False -- not visible
        """
        self.table_form.horizontalHeader().setVisible(status)

    # set stretch last section horizontal header
    def use_horizontal_header_set_stretch_last_section(self, status):
        """
        :param status: True or False
        :return:
            True -- stretch last section
            False -- not stretch last section
        """
        self.table_form.horizontalHeader().setStretchLastSection(status)

    # set stretch last section vertical header
    def use_vertical_header_set_stretch_last_section(self, status):
        """
        :param status: True or False
        :return:
            True -- stretch last section
            False -- not stretch last section
        """
        self.table_form.verticalHeader().setStretchLastSection(status)

    # --------------------------------------------------------------------------------

    # return check content empty
    def check_content_empty(self, dict_add):
        return ("".join(f"{v}" for k, v in dict_add.items())) == "-"

    # if content == "-" then row must empty
    def update_table_form(self, dict_add):
        if not self.check_content_empty(dict_add):
            self.content_from_table.update(dict_add)

    # add items to dict content_from_table
    def add_items_to_dict_table(self, list_items):
        for el in list_items:
            self.update_table_form(el)

    # add items to table
    def add_items_from_dict_to_table(self):
        num = 0
        for j, k in self.content_from_table.items():
            description_column = QTableWidgetItem(j)
            description_column.setFlags(Qt.ItemIsEnabled)
            self.table_form.setItem(num, 0, description_column)
            content_column = QTableWidgetItem(k)
            content_column.setFlags(Qt.ItemIsEnabled)
            self.table_form.setItem(num, 1, content_column)
            num += 1
