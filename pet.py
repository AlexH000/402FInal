import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("DESCRIBE pet")

for x in mycursor:
    print(x)
