import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = mydb.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)
