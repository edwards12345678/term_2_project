

from order_app_logic_pkg.Order import Order
from order_app_logic_pkg.OrderItem import OrderItem
from order_app_logic_pkg.Customer import Customer
from order_app_logic_pkg.Products import Products
from order_app_logic_pkg.Postal_Order import Postal_Order


class Order_mgt_UI:

    def __init__(self):
        self.cust_name=self.get_cust_name()
        self.cust_email=self.get_cust_email()
        #testing below: Creation of a regular Order and a Postal Order
        #self.orders=[self.create_postal_order()]
        
        self.orders=[self.create_order(),self.create_postal_order()]
        #self.orders=[self.create_postal_order()]

    def get_cust_name(self)->type[str]:
        done=False
        while not done:
            done=True
            name= input("Enter your name. 3-10 chars. No white space chars allowed: ")
            if len(name) <=3 or len(name)>=10:
                    print("Name should be between 3-10 chars. Try again")
                    done=False
            forbidden = [' ', '\n','\r','\t','\b']
            # Check if any forbidden characters are in the name
            #'any' returns true if any of the forbidden char is in name
            if any(a_char in name for a_char in forbidden):
                    print("You have used white space chars. Try again")
                    done=False
        return name
    
    def get_cust_email(self)->type[str]:
        done=False
        while not done:
            done=True
            email= input("Enter your email. 6-20 chars with an @. No white space chars allowed: ")
            if len(email) <=6 or len(email)>=20:
                    print("Email should be between 6-20 chars. Try again")
                    done=False
            forbidden = [' ', '\n','\r','\t','\b']
            if any(a_char in email for a_char in forbidden):
                    print("You have used white space chars. Try again")
                    done=False
            if email[0]=='@' or email.count('@')!=1:
                print("An in-between @ char expected in email. Try again")
                done=False
        return email
 
    def create_postal_order(self)->Postal_Order:
        a_customer = Customer(self.cust_name,self.cust_email)
        a_postal_order = Postal_Order(a_customer)
        done=False
        while not done:
            done=True
            a_postal_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                 done=False
        return a_postal_order
        
    def create_order(self)->Order:

        a_customer = Customer(self.cust_name,self.cust_email)
        an_order = Order(a_customer)
        done=False
        while not done:
            done=True
            an_order.add_item(self.create_order_item())
            correct_more=False
            while not correct_more:
                correct_more=True
                more = input("Do you want to order another item Y/N: ")
                more = more.strip()
                if more not in ['Y', 'y','N','n']:
                     print("You did not enter Y or N. Please try again")
                     correct_more=False
            if more in ['Y','y']:
                 done=False
        return an_order


    def create_order_item(self)->OrderItem:
        item_id=None
        item_name=None
        item_unit_price=None
        item_qty=None
        p=Products()
        print(str(p))#Available products
        correct_choice=False
        while not correct_choice:
            correct_choice=True
            choice=input("Enter your choice 1-4: ")
            if choice not in ['1','2','3','4']:
                print("Your entry was incorrect. Try again")
                correct_choice=False
        item_id=int(choice)
        item_name=Products.ALL_PRODUCTS[item_id-1]["name"]
        item_unit_price=Products.ALL_PRODUCTS[item_id-1]["unit_price"]

        correct_qty=False
        while not correct_qty:
            correct_qty=True
            item_qty=input("Input the quanity. Positive integers only: ")
            
            try:
                item_qty=int (item_qty)
            except:
                    print("You did not enter an integer. Try again")
                    correct_qty=False
            if item_qty<0:
                print("You did not enter a positive integer. Try again")
                correct_qty=False
        
        anItem =OrderItem(item_name,item_unit_price,item_qty)

        return anItem
         
           

