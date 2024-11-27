from db_mysql.createDatabase import create_database
from db_mysql.createTable import create_table
from db_mysql.insertData import insert_data
from db_mysql.readData import get_all_students
# create_database()
# create_table()
# insert_data()

for stu in get_all_students():
    print(stu[0], stu[1], stu[2])

