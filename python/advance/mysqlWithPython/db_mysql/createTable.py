from .dbConnection import cursor

def create_table():
    table_name = input("Enter a table name: ")
    table_config = input("Enter atble config: ")
    sql = f"create table {table_name} ({table_config});"
    print(sql)
    cursor.execute(sql)