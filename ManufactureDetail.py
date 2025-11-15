from DatabaseConnection import mycursor

def ManufactureDetail(ProductID):
    mycursor.execute(f"""SELECT ManufactureDetail.* 
                     FROM ManufactureDetail 
                     JOIN product 
                     ON Product.ProdID={ProductID}
                     AND ManufactureDetail.ManufactureID=Product.ManufactureID""")
    detail=mycursor.fetchone()
    if detail:
       print(*detail)
    else:
        return