from DatabaseConnection import mycursor
def BillDetail():
    mycursor.execute ("SELECT * FROM BillDetail ")
    results=mycursor.fetchall()
    for result in results:
        print(*result)