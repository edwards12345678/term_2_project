import os,sys
class Product_DB():
    file_path ='.'+os.sep+'assets'+os.sep+'data_files'+os.sep
    file_name = 'products.txt'
    rec_template = '{:50}, {:10.2f}, {:5d}\n'

    def __init__(self, name, unit_price, stock_quantity):
        self.name = name
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity

    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    def save(self):
        try:

            #create file if not created already
            if not os.path.isfile(Product_DB.file_path+ Product_DB.file_name):
                f = open(Product_DB.file_path+ Product_DB.file_name, 'x')
                f.close()
            # open the file in append mode
            f=open(Product_DB.file_path+ Product_DB.file_name, "a")
            f.write(Product_DB.rec_template.format(self.name, self.unit_price, self.stock_quantity))
            f.close()
        except Exception:
            e = sys.exc_info()[0]
            print("Error: "+str(e))

products=[Product_DB("Pen", 10, 100), Product_DB("Eraser", 5, 10)]
for a_product in products:
    a_product.save()
