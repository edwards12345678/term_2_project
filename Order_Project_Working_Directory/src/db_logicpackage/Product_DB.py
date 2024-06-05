import platform
import os
import sys
class Product_DB:
    filePath = "."+ os.sep+"assets"+os.sep+"data_files"+os.sep
    fileName = "Products.txt"
    rec_template = '{:50}, {:10.2f}, {:5d}\n'
    rec_length = 70
    statinfo = os.stat(filePath+fileName)
    file_size = statinfo.st_size
    def __init__ (self,name:str, unitprice:float,stock:int):
        self.name = name
        self.unitprice = unitprice
        self.stock = stock
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name !=None and name != " ":
            self._name = name
        else:
            self._name = "None"
    
    @property
    def unitprice(self):
        return self._unitprice
    
    @unitprice.setter
    def unitprice(self, unitprice):
        if unitprice !=None and unitprice != " ":
            self._unitprice = unitprice
        else:
            self._unitprice = "None"
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, stock):
        if stock !=None and stock != " ":
            self._stock = stock
        else:   
            self._stock = "None"
   
    def saveNewProduct(self):
        try:
         if not os.path.isfile(Product_DB.filePath+Product_DB.fileName):
             f = open(Product_DB.filePath+Product_DB.fileName, "x")
             f.close()
        
         f=open(Product_DB.filePath+Product_DB.fileName, "a")
         f.write(Product_DB.rec_template.format(self.name, self.unitprice, self.stock))
         f.close()

        except Exception:
            e = sys.exc_info()[0]
            print("Error"+ str(e))
    @staticmethod
    def read_product(offset:int, bytes:int):
        f = open(Product_DB.filePath+Product_DB.fileName, "r")
        f.seek(offset,0)
        s = f.read(bytes)
        tokens = s.split(',')
        name = tokens[0].strip()
        unitprice = float(tokens[1].strip())
        stock = int(tokens[2].strip())
        f.close()
        P = Product_DB(name,unitprice,stock)
        return P
    @staticmethod 
    def update_product(offset:int, bytes:int, product):
        f = open(Product_DB.filePath+Product_DB.fileName, "w+")
        f.seek(offset, 0)
        f.write(Product_DB.rec_template.format(product.name, product.unitprice, product.stock))
        f.close()
       

    def __str__(self):
        return f'{self.name:20}, {self.unitprice:5.2f}, {self.stock:5d}\n'
    

    def update_this_product_in_file(self)->bool:
        updated = False
        offset = 0
        f = open(Product_DB.filePath+Product_DB.fileName,'r+')
        while offset<Product_DB.file_size:
            f.seek(offset,0)
            s = f.read(Product_DB.rec_length)
            tokens = s.split(",")
            name = tokens[0].strip()
            unitprice = float(tokens[1].strip())
            stock = int(tokens[2].strip())
            p = Product_DB(name,unitprice,stock)
            if p == self.name:
                f.seek(offset,0)
                f.write(Product_DB.rec_template.format(p.name, p.unitprice, p.stock))
                updated = True
            offset += Product_DB.rec_length
        f.close()
        return updated
    
    
        

# pinaple = Product_DB("Gun", 12.99, 100)
# apple = Product_DB("Apple",123,145)
# pinaple.saveNewProduct()
# apple.saveNewProduct()
# apple.name = "BLUPBLUP"
# Product_DB.update_product(70,70,apple)
# p = Product_DB.read_product(70,70)
# print(p.name)



