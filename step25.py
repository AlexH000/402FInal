import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="menagerie"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, birth FROM pet ORDER BY birth ASC")

myresult = mycursor.fetchall()

for x in myresult:
    name = x[0]
    birthdate = x[1]
    birthdate_str = birthdate.strftime('%Y-%m-%d')
    birthmonth = birthdate.month
    print(f"{name}, {birthdate_str}, {birthmonth}")
