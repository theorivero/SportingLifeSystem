from uuid import uuid4

class client:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.id = uuid4().int
        self.rented_equipment = []

    def return_id(self):
        return self.id

    def return_name(self):
        return self.name

    def update_name(self,new_name):
        self.name = new_name
        return self.name

    def return_phone_number(self):
        return self.phone_number

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        return self.phone_number

    def return_rented_equipment(self):
        return self.rented_equipment


