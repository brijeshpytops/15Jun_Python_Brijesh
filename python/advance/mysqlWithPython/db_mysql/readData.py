from .dbConnection import cursor

def get_all_students():
    sql = "select * from students"
    cursor.execute(sql)
    return cursor.fetchall()