import os
import sys
from order_app_logic_pkg.Order import Order
from order_app_logic_pkg.Customer import Customer
from order_app_logic_pkg.OrderItem import OrderItem
from datetime import datetime
class Order_DB:
    filePath = "."+ os.sep+"assets"+os.sep+"data_files"+os.sep
    fileName = "Orders.txt"
    order_header_template = '{:12}, {:8}, {:5d}\n'
    customer_template = '{:10}, {:25}, {:30}\n'
    item_template = '{:50}, {:10f}, {:5d}\n'

    def __init__ (self,order):
        self.order = order

    # def __init__ (self):
    #     self.order = None
    
   

    @staticmethod
    def read_order(offset:int,bytes:int):
         f = open(Order_DB.filePath+Order_DB.fileName, "r")
         f.seek(offset, 0)
         line_1 = f.read(23)
         line_2 = f.read(67)
         header_tokens = line_1.split(',')
         order_id = int(header_tokens[0])
         order_date = header_tokens[1]
         order_count = int(header_tokens[2])
         customer_tokens = line_2.split(',')
         customer_id = int(customer_tokens[3])
         customer_name = customer_tokens[4]
         customer_email = customer_tokens[5]
         customer = Customer(customer_name,customer_email)
         customer_index__id = customer_id.index('_')
         customer_id = customer_id[customer_index__id+1:]
         customer.cust_id = str(customer_id)
         order = Order(customer)
         for i in range(order_count):
             line_3 = f.read(67)
             items_tokens = line_3.split(',')
             order_item_name = items_tokens[6]
             order_item_price = float(items_tokens[7])
             order_item_quantity = int(items_tokens[8])
             orderitem = OrderItem(order_item_name,order_item_price,order_item_quantity)
             order.add_item(orderitem)
         f.close()
         order.order_id = order_id
         dd = int(order_date[0:2])
         mm = int(order_date[2:4])
         yyyy =int(order_date[4:9])
         order.order_date = datetime(yyyy,mm,dd)
         p = Order_DB(order)
         return p
    
    def save_order(self):
        try:
         if not os.path.isfile(Order_DB.filePath+Order_DB.fileName):
             f = open(Order_DB.filePath+Order_DB.fileName, "x")
             f.close()
         f=open(Order_DB.filePath+Order_DB.fileName, "a")
         f.write(Order_DB.order_header_template.format(self.order.order_id,self.order.order_date,len(self.order.items)))
         f.write(Order_DB.customer_template.format(self.order.customer.cust_id,self.order.customer.customer_name,self.order.customer.customer_email))
         for i in self.order.items:
            f.write(Order_DB.item_template.format(i.name,i.price,i.qty))
         f.close()

        except Exception:
            e = sys.exc_info()[0]
            print("Error"+ str(e))
    
    
    
    


    
