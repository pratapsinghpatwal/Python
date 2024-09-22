# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql="SELECT name, address FROM customers"

#sql="SELECT name, address FROM customers where address='Alwar'"
# sql = "SELECT * FROM customers ORDER BY name"

#sql = "DELETE FROM customers WHERE address = 'Delhi'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 
