from uuid import uuid4


class Customer:
    def __init__(self, name: str, phone_number: int):
        self.__name = name
        self.__phone_number = phone_number
        self.__id = uuid4().int
        self.__rented_equipments = []

    @property
    def return_id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def rented_equipments(self):
        return self.__rented_equipments

    @rented_equipments.setter
    def rented_equipments(self, equipments):
        self.__rented_equipments.append(equipments)
