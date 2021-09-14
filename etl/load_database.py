# Module Imports
# import mysql.connector as mysql
import pymysql.cursors
import sys
# Connect to MariaDB Platform
# try:
conn = pymysql.connect(
    user="carlos",
    password="newpassword",
    host='localhost',
    port=3306,
    database="test-ludeme",
    cursorclass=pymysql.cursors.DictCursor
)
# except mysql.Error as e:
#     print(f"Error connecting to MariaDB database {e}")
#     sys.exit(1)

if conn.is_connected():
    db_Info = conn.get_server_info()
    print("Connected to ", db_Info)
    # cursor.close() 
    cursor = conn.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to the database: ", record)
    
# # Get Cursor
# cursor = conn.cursor()

try:
    print('Loading the .sql file in the MariaDB database')
    with open('data/ludiiGames.sql', 'r') as f:
        cursor.execute(f.read(), multi=True)
        print('SQL file executed, now commiting')
        conn.commit()


    print("Show tables in the database:")
    cursor.execute('show tables;')
    records = cursor.fetchall()
    for i in records:
        print(i)

finally:
    cursor.close()