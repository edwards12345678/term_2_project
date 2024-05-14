from  src.order_app_logic_pkg.Customer import Customer

def test___str__():
    """
    Testing __str__ function
    """
    cust=Customer(customer_name="Chris", customer_email="Chris@c.com")
    s=cust.__str__()
    assert cust.__str__()=='Customer details are:\nCustomer ID =Cust_2024_1         Customer name =Chris               Customer email =Chris@c.com                   \n'

