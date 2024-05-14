from  src.order_app_logic_pkg.Postal_Order import Postal_Order
from  src.order_app_logic_pkg.Customer import Customer

def test_has_partial_valid_state_sequence():
    cust = Customer(customer_name="Chris", customer_email="Chris@c.com")
    postal_order=Postal_Order(cust)    
    v_seq=["Initiated", "Packed", "Shipped", "Delivered"]
    #----------Testing valid state sequences-------------------------------------------
    assert postal_order.has_partial_valid_state_sequence([],v_seq)==True
    assert postal_order.has_partial_valid_state_sequence([0],v_seq)==True
    assert postal_order.has_partial_valid_state_sequence([0,1],v_seq)==True
    assert postal_order.has_partial_valid_state_sequence([0,1,2],v_seq)==True
    assert postal_order.has_partial_valid_state_sequence([0,1,2,3],v_seq)==True
    #----------Testing invalid state sequences-------------------------------------------
    assert postal_order.has_partial_valid_state_sequence([0,1,2,3,4],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([1],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([2],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([3],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([4],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([-1],v_seq)==False
    assert postal_order.has_partial_valid_state_sequence([0,2],v_seq)==False