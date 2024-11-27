from .dbConnection import db, cursor

def insert_data():
    fname = input("Enter your firstname :")
    lname = input("Enter your lastname :") 
    sql = f"insert into students ( fname, lname ) VALUES ('{fname}', '{lname}');"
    print(sql)
    cursor.execute(sql)
    db.commit()