import os
from dotenv import load_dotenv
import sys
sys.path.append(os.getcwd())
from MainPages import *
import pymysql
load_dotenv()
MY_SQL_PASSWORD = os.getenv('MY_SQL_PASSWORD')
SQL_FILE = os.getenv('SQL_FILE')
DB_NAME = os.getenv('DB_NAME')
USERNAME = os.getenv('USERNAME')

def checkSQL():
    conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, charset='utf8')
    cursor = conn.cursor()
    readSQLFile(SQL_FILE, cursor)
    conn.commit()
    conn.close()

def readSQLFile(filename, cursor):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        if command.strip() != '':
            cursor.execute(command)

if __name__ == "__main__":
    checkSQL()
    Main_Page().mainloop()