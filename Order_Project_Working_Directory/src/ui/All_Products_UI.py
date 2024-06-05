from db_logicpackage.All_Products_DB import All_Products_DB
from db_logicpackage.Product_DB import Product_DB
import sys
class All_Products_UI:
    all_prdcts_db = All_Products_DB

    def input_a_product(self):
        name = input("Enter the name of your product: ")
        unitprice = input("Enter the unitprice of your product: ")
        stock = input("Enter the stock of your product: ")
        product = Product_DB(name,unitprice,stock)
        self.all_prdcts_db.save_new_product(product)

    def display_products(self):
        for p in self.all_prdcts_db.all_products:
            print(str(p))
    
    def update_a_product(self):
        try:
            All_Products_UI.display_products()
            to_be_updated_name = input("Enter the name of the product to be updated")
            for p in self.all_prdcts_db.all_products:
                if p.name == to_be_updated_name:
                    change_unitprice = input("Do you want to change the unitprice?(Y/N) ")
                    if change_unitprice.lower() == "y":
                        new_unitprice = input("What is the new unitprice? ")
                        p.unitprice = new_unitprice
                    change_stock = input("Do you want to change the stock?(Y/N) ")
                    if change_stock.lower() == "y":
                        new_stock = input("What is the new stock? ")
                        p.unitprice = new_stock
                p.update_this_product_in_file()  
        
        except Exception:
            e = sys.exc_info()[0]
            print("Error"+ str(e))
