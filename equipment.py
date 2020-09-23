from uuid import uuid4


class Equipment:
    def __init__(self, name, total_quantity, available_quantity, rental_price):
        self.__name = name
        self.__total_quantity = int(total_quantity)
        self.__id = uuid4().int
        self.__available_quantity = int(available_quantity)
        self.__rental_price = int(rental_price)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def total_quantity(self):
        return self.__total_quantity

    @total_quantity.setter
    def total_quantity(self, total_quantity):
        self.__total_quantity = total_quantity

    @property
    def available_quantity(self):
        return self.__available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        self.__available_quantity = available_quantity

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, rental_price):
        self.__rental_price = rental_price
