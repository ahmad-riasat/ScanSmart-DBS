from DatabaseConnection import mycursor, mydb

def UpdateProduct(ProductID):
    # Check if product exists
    mycursor.execute(f"SELECT ProdID FROM Product WHERE ProdID ={ProductID}")
     
    result = mycursor.fetchone()

    if result is None:
        print("Product not found.")
        return

    # Product exists → update quantity
    AvailableQuantity = int(input(f"Enter new quantity for Product {ProductID}: "))

    update_sql = "UPDATE Product SET QuantityAvailable = %s WHERE ProdID = %s"
    mycursor.execute(update_sql, (AvailableQuantity, ProductID))
    mydb.commit()

    print(f"Product {ProductID} quantity updated to {AvailableQuantity}.")
