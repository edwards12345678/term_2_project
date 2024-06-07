import platform
import os
import sys
from db_logicpackage.Product_DB import Product_DB
# from order_app_logic_pkg.Products import Products
class All_Products_DB:

    def __init__(self):
        self.all_products = []
        self.read_all_products()
    
    @property
    def all_products(self):
        return self._all_products
    
    @all_products.setter
    def all_products(self, all_products):
        self._all_products = all_products   


    def read_all_products(self):
        if not os.path.isfile(Product_DB.filePath+Product_DB.fileName):
            f = open(Product_DB.filePath+Product_DB.fileName, 'x')
            f.close()
        self.all_products.clear()
        statinfo = os.stat(Product_DB.filePath+Product_DB.fileName)
        fileSize = statinfo.st_size 
        i = 0
        while i < fileSize:
            p = Product_DB.read_product(offset = i, bytes=Product_DB.rec_length)
            i += Product_DB.rec_length
            self.all_products.append(p)
    
    def save_all_products(self):
        if os.path.isfile(Product_DB.filePath+Product_DB.fileName):
           os.remove(Product_DB.filePath+Product_DB.fileName)
        for p in self.all_products:
            p.saveNewProduct()
        

    def save_new_product(self, product:Product_DB)->bool:
        saved_new_product = True
        for p in self.all_products:
         if p.name == product.name:
            saved_new_product = False
            break
        if saved_new_product == True:
            self.all_products.append(product)
            product.saveNewProduct()
        return saved_new_product


    def __str__ (self) ->type[str]:
        star_line = "\n"+"-"*100+"\n"
        product_details = "Available products details are:\n"
        for rec in self.all_products:
            product_details += str(rec)
        return (star_line+product_details+star_line)
        
           
            

all_recs = All_Products_DB()
all_recs.save_all_products()

