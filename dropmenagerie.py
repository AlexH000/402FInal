import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

myursor = mydb.cursor()

mycursor.execute("DOP DATABASE menagerie")
