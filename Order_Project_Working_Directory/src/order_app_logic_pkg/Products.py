#A list of all products. 
#Hard coded here.
#In reality the data should be read from a file
class Products:
    ALL_PRODUCTS =[     {"name":"Pen", "unit_price":2}, 
                        {"name":"Computer Disk","unit_price":200},
                        {"name":"Scientific Calculator","unit_price":100},
                            {"name":"Sun Glasses","unit_price":300}]
    ALL_PRODUCTS_F =[ {f'1. {"name":4}':f'{"Pen":25}',                   f'{"unit_price":10}':f'${2:4d}'}, 
                {f'2. {"name":4}':f'{"Computer Disk":25}',         f'{"unit_price":10}':f'${200:4d}'},
                {f'3. {"name":4}':f'{"Scientific Calculator":25}', f'{"unit_price":10}':f'${100:4d}'},
                {f'4. {"name":4}':f'{"Sun Glasses":25}',           f'{"unit_price":10}':f'${300:4d}'}]

    def __str__(self)->type[str]:
        star_line = "\n"+"-"*100+"\n"
        product_details="Available products details are:\n"+'\n'.join(map(str, Products.ALL_PRODUCTS_F))
        return (star_line+product_details+star_line)

    