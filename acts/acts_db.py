import sqlite3
connectionState = sqlite3.connect("acts_databs.db")
cursor  = connectionState.cursor()

def createTables():
    cursor.execute("""Create Table if not exists Category (

            categoryname TEXT PRIMARY KEY,
            numberofacts INT) """)
    
    cursor.execute("""Create Table if not exists Acts (

            categoryname INT,
            actId INT PRIMARY KEY,
            username TEXT,
            timestamp DATETIME,
            caption TEXT,
            imgB64 TEXT,
            upvotes INT,
            FOREIGN KEY(categoryname) REFERENCES Category(categoryname) ) """)

    connectionState.commit()
createTables()