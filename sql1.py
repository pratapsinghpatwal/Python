# write a program to create database in the mysql 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pintu")
