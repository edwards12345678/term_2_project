#A list of all products. 
#Hard coded here.
#In reality the data should be read from a file
from db_logicpackage.All_Products_DB import All_Products_DB
from db_logicpackage.Product_DB import Product_DB
class Products:
    def __init__ (self):
       self.allprdct = All_Products_DB()

    def __str__(self)->type[str]:
        star_line = "\n"+"-"*100+"\n"
        stringaling = ""
        for i in self.allprdct.all_products:
            stringaling += str(i)
        return (star_line+stringaling+star_line)

    