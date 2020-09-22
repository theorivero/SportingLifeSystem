from uuid import uuid4
class equipment:
    def __init__(self, name, quantity_in_stock, available_quantity, rental_price):
        self.name = name
        self.quantity_in_stock = int(quantity_in_stock)
        self.id = uuid4().int
        self.available_quantity = int(available_quantity)
        self.rental_price = int(rental_price)

    def return_id(self):
        return self.id
    
    def return_name(self):
        return self.name

    def update_name(self,new_name):
        self.name = new_name
        return self.name

    def return_quantity_in_stock(self):
        return self.quantity_in_stock

    def update_quantity_in_stock(self,new_quantity_in_stock):
        self.quantity_in_stock = new_quantity_in_stock
        return self.quantity_in_stock

    def return_available_quantity(self):
        return self.available_quantity

    def update_available_quantity(self,new_available_quantity):
        self.available_quantity = new_available_quantity
        return self.available_quantity
    
    def return_rental_price(self):
        return self.rental_price

    def update_rental_price(self,new_rental_price):
        self.rental_price = new_rental_price
        return self.rental_price

halter = equipment('halter 8kg', 5, 4, 30)
print(halter.update_rental_price(70))