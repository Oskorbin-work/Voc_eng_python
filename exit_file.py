from database.sql_query_bd import WorkWithBd

class Exit_program(WorkWithBd):
    def bd_to_default_state(self):
        self.clear_temp_activate()