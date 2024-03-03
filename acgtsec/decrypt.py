import json
import os
import sqlite3
from base64 import b64decode

from Crypto.Cipher import AES

#pull filepath from database




def grabFasta(db_file, table_name):
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(f"SELECT Fasta FROM {table_name}")
        rows = cur.fetchall()
        for row in rows:
            fasta = row[0]
            print("Fafsa:", fasta)
            return fasta  # Return fasta directly
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return None
    finally:
        if conn:
            conn.close()

keyLoca = os.getenv('KEY_LOCATION')
def Decrypt(jsonFilePath, keyFilePath):
    with open(jsonFilePath, 'rb') as setInput:
        jsonInput = setInput.read()
    with open(keyFilePath, 'rb') as keyLog:
        key = keyLog.read()
    try:
        b64 = json.loads(jsonInput)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        pt = cipher.decrypt(ct)
        return pt.decode('utf-8')
    except (ValueError, KeyError):
        print("Incorrect decryption")
        return None

#Decrypt(jsonFilePath, keyFilePath)
def userCheck(username, password):
    return username == "admin" and password == "PapaWhiskey1"

db_file = 'client.db'
table_name = 'client'
fasta_file_path = grabFasta(db_file, table_name)
if fasta_file_path:
    keyFilePath = os.getenv('KEY_LOCATION')
    decrypted_text = Decrypt(fasta_file_path, keyLoca)
    if decrypted_text:
        print("Decrypted text:", decrypted_text)