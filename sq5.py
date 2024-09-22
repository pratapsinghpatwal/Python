# inserting data in to the  table


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("kanha", "Delhi")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")