import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="ahmad32",
    database="INVENTORY_MANAGEMENT"

)
mycursor=mydb.cursor()