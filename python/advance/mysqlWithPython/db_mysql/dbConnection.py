import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="school"
)

cursor = db.cursor()

if db.is_connected():
    print("Successfully connected to MySQL database")
else:
    print("Failed to connect to MySQL database")