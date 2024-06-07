from ui.Order_mgt_UI import Order_mgt_UI
from ui.All_Products_UI import All_Products_UI
from db_logicpackage.Product_DB import Product_DB
from db_logicpackage.All_Products_DB import All_Products_DB
# if __name__ == "__main__":
#     o_ui=Order_mgt_UI()

#     for order in o_ui.orders:
#         print(str(order))
keepgoing = True
AllprocutsUI = All_Products_UI()
while keepgoing == True:
    choice = input("Do you want to input new products? Y/N:  ")
    if choice == "Y":
        AllprocutsUI.input_a_product()
    else:
        keepgoing = False

ordermgt = Order_mgt_UI()