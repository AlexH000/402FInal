import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, birth FROM pet")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
