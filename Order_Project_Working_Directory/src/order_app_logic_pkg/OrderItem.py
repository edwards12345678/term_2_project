
class OrderItem:
    #initializes an OrderItem
    def __init__(self, name:type[str], price:type[float], qty:type[int]):
        self.name = name
        self.price = price
        self.qty=qty
    @property
    def name(self)->type[str]:
        return self._name
    @name.setter
    def name(self, name:type[str]):
        if name!=None and name!="":
            self._name=name
    @property
    def price(self)->type[float]:
        return self._price
    
    @price.setter
    def price(self, price:type[float]):
        if price>0:
           self._price=price
    @property
    def qty(self)->type[int]:
        return self._qty
    @qty.setter
    def qty(self, qty:type[int]):
        if qty>0:
            self._qty=qty
             
    def __str__(self)->type[str]:
        return (f"Item name = {self.name:40}Item price =${self.price:<10.2f}Item Qty ={self.qty:2d}")
