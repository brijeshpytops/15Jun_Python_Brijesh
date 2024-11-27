from .dbConnection import db, cursor

def create_database():
    database_name = input("Enter a database name: ")
    sql = f"create database {database_name}"
    cursor.execute(sql)