from entity.customer import *
from entity.equipment import *


class Rent:
    def __init__(self, customer: Customer, equipment: Equipment, weeks_quantity):
        self.__customer = customer
        self.__customer.rented_equipments.append(equipment)
        self.__equipment = equipment
        self.__weeks_quantity = weeks_quantity

    @property
    def customer(self):
        return self.__customer

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, equipment):
        self.__equipment = equipment

    @property
    def weeks_quantity(self):
        return self.__weeks_quantity

    @weeks_quantity.setter
    def weeks_quantity(self, weeks_quantity):
        self.__weeks_quantity = weeks_quantity