import os
import sqlite3
import time
from sqlite3 import Error

from acgtsec.propertiesadd import Set1, team

dir = os.getenv('UPLOAD_DIR')

def makeTable(db_file, table_name):
    conn = sqlite3.connect('../hatchdata/client.db')
    cur = conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS client (
            Num INTEGER PRIMARY KEY,
            Fasta TEXT,
            GID INTEGER,
            TID INTEGER
            RCV TEXT
        )""")

        print("table made")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    conn.commit()
    conn.close()

def newFileSignal(table_name, type):
    conn = sqlite3.connect('../hatchdata/client.db')
    cur = conn.cursor()
    
    encryptedFilePaths = Set1(dir)
    TeamID = team()
    if encryptedFilePaths:
        encryptedFilePath = str(encryptedFilePaths[0])
        cur.execute(f"INSERT INTO {table_name} (GID, Fasta, TID) VALUES (?, ?, ?)", (type, encryptedFilePaths[0], TeamID[0]))
    else:
        print("no files")

    conn.commit()
    conn.close()

def insertData(db_file, table_name, data):
    cur.execute(f"INSERT INTO {table_name} (Fasta, GID, TID) VALUES (?, ?, ?)", data)
    
    print("data inserted!")
    conn.commit


def print_table(db_file, table_name):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()

        # Select all rows from the table
        cur.execute(f"SELECT * FROM {table_name}")
        
        # Fetch all rows from the cursor
        rows = cur.fetchall()
        
        # Print the column headers
        col_names = [description[0] for description in cur.description]
        print(" | ".join(col_names))
        
        # Print each row
        for row in rows:
            row_data = []
            for value in row:
                if value is None:
                    row_data.append("NULL")
                else:
                    row_data.append(str(value)[:50])  # Truncate long values
            print(" | ".join(row_data))


        conn.close()
    except sqlite3.Error as e:
        print(f"Error printing table: {e}")

def grabTID(db_file, table_name):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(f"SELECT TID FROM {table_name}")
        rows = cur.fetchall()
        for row in rows:
            tid = row
            print("TID:", tid)
            
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
    

