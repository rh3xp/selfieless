import sqlite3
connectionState = sqlite3.connect("user_databs.db")
cursor  = connectionState.cursor()

def createTables():
    cursor.execute("""Create Table if not exists User (

            username TEXT PRIMARY KEY,
            password TEXT )""")
    
    connectionState.commit()

createTables()  