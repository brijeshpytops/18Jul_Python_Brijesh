from .dbConnection import cursor

def create_tables():
    table_name = input("Enter a table-name: ")
    fields_config = input("Enter a fields config: ")
    sql = f"create table {table_name} ({fields_config});"
    cursor.execute(sql)