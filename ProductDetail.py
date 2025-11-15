
from DatabaseConnection import mycursor
from decimal import Decimal
def ProductDetail(ProductID):
    
    mycursor.execute(f"SELECT * FROM product WHERE ProdID={ProductID}")
    detail=mycursor.fetchone()
    if detail:
        detail_list=[str(d) if isinstance(d,Decimal) else d for d in detail] #for printing price as 180.00 instead of Decimal(180.00)
        print(*detail_list) #for printing simple instead of bracket and commas we use print(*)
      
    else:
        return
    
    