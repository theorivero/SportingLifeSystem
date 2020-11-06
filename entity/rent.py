from entity.customer import *
from entity.equipment import *


class Rent:
    def __init__(self, customer: Customer, equipment: Equipment, rental_quantity, rental_start, rental_deadline):
        self.__customer = customer
        self.__customer.rented_equipments(equipment)
        self.__equipment = equipment
        self.__rental_quantity = rental_quantity
        self.__rental_start = rental_start
        self.__rental_deadline = rental_deadline

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
    def rental_quantity(self):
        return self.__rental_quantity

    @rental_quantity.setter
    def rental_quantity(self, rental_quantity):
        self.__rental_quantity = rental_quantity

    @property
    def rental_start(self):
        return self.__rental_start

    @rental_start.setter
    def rental_start(self, rental_start):
        self.__rental_start = rental_start

    @property
    def rental_deadline(self):
        return self.__rental_deadline

    @rental_deadline.setter
    def rental_deadline(self, rental_deadline):
        self.__rental_deadline = rental_deadline
