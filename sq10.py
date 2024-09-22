# droping the table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE custo"

mycursor.execute(sql) 
print("The table is droped")