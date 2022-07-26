from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt


class TableViews:
    def __init__(self,column_count,
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

    def use_vertical_header_set_visible(self, status):
        self.table_form.verticalHeader().setVisible(status)

    def use_horizontal_header_set_visible(self, status):
        self.table_form.horizontalHeader().setVisible(status)

    def use_horizontal_header_set_stretch_last_section(self, status):
        self.table_form.horizontalHeader().setStretchLastSection(status)

    def use_vertical_header_set_stretch_last_section(self, status):
        self.table_form.verticalHeader().setStretchLastSection(status)
