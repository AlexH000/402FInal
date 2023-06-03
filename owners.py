import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
