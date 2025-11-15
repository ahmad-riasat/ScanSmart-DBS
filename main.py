from ProductDetail import ProductDetail
from ManufactureDetail import ManufactureDetail
from AddProduct import AddProduct
from DeleteProduct import DeleteProduct
from UpdateProduct import UpdateProduct
from BillHistory import BillHistory
from BillDetail import BillDetail

def main():
    last_id = None

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Show Product Detail")
        print("2. Show Manufacture Detail of SAME Product")
        print("3. Add New Product")
        print("4. Delete Product")
        print("5. Update Product")
        print("6. Show Bill History")
        print("7. Show Bill Detail")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                last_id = int(input("Enter Product ID: "))
                ProductDetail(last_id)

            case "2":
                if last_id is None:
                    print("You must first select a product using option 1.")
                else:
                    ManufactureDetail(last_id)

            case "3":
                AddProduct()

            case "4":
                pid = int(input("Enter Product ID to delete: "))
                DeleteProduct(pid)

            case "5":
                pid = int(input("Enter Product ID to update: "))
                UpdateProduct(pid)

            case "6":
                BillHistory()

            case "7":
                BillDetail()

            case "0":
                print("Exiting program...")
                break

            case _:
                print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()




 
 


 