from ui.Order_mgt_UI import Order_mgt_UI
if __name__ == "__main__":
    o_ui=Order_mgt_UI()

    for order in o_ui.orders:
        print(str(order))

         
#Remove an item
#order.remove_item(item1)
#order.display_order()

print('test')
