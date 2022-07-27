from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


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

        self.content_from_table = dict()

    # Attributes table
    # --------------------------------------------------------------------------------
    def use_vertical_header_set_visible(self, status):
        self.table_form.verticalHeader().setVisible(status)

    def use_horizontal_header_set_visible(self, status):
        self.table_form.horizontalHeader().setVisible(status)

    def use_horizontal_header_set_stretch_last_section(self, status):
        self.table_form.horizontalHeader().setStretchLastSection(status)

    def use_vertical_header_set_stretch_last_section(self, status):
        self.table_form.verticalHeader().setStretchLastSection(status)

    # --------------------------------------------------------------------------------

    def check_content_empty(self, dict_add):
        return ("".join(f"{v}" for k, v in dict_add.items())) == "-"

    def update_table_form(self, dict_add):
        if not self.check_content_empty(dict_add):
            self.content_from_table.update(dict_add)

    def add_items_to_dict_table(self, list_items):
        for el in list_items:
            self.update_table_form(el)

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
