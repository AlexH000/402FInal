import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM pet WHERE species = 'dog' AND sex = 'f'")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
