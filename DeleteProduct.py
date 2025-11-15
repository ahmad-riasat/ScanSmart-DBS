from DatabaseConnection import mycursor,mydb

def DeleteProduct(ProductID):
    if (mycursor.execute(f"DELETE FROM Product WHERE ProdID={ProductID}")):
        mydb.commit()
        print(f"Product {ProductID} deleted successfully")
    else :
        print("Product is not Found")
        return
