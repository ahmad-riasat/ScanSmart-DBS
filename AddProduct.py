from DatabaseConnection import mycursor,mydb
from decimal import Decimal

def AddProduct():
    Name=input("Product Name:")
    Category=input("Category:")
    Price=Decimal(input("Price:"))
    QuantityAvailable=int(input("Available Quantity:"))
    ManufactureID=int(input("Manufacture ID:"))

    sql=("INSERT INTO Product (Name,Category,Price,QuantityAvailable,ManufactureID) VALUES (%s,%s,%s,%s,%s)")
    val=(Name,Category,Price,QuantityAvailable,ManufactureID)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Sucessfully Added")

