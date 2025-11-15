from DatabaseConnection import mycursor
def BillHistory():
    mycursor.execute ("SELECT * FROM Bill ")
    results=mycursor.fetchall()
    for result in results:
        print(*result)


    