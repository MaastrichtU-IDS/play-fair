# Module Imports
import mysql.connector as mysql
import sys
# Connect to MariaDB Platform
try:
    conn = mysql.connect(
        user="mariadb",
        password="ludiluda",
        host='mariadb',
        port=3306,
        database="ludiiGames"
    )
except:
    print(f"Error connecting to MariaDB database")
    sys.exit(1)

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
    with open('data/database/ludiiGames.sql', 'r') as f:
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