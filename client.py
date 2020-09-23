from uuid import uuid4


class Client:
    def __init__(self, name, phone_number):
        self.__name = name
        self.__phone_number = phone_number
        self.__id = uuid4().int
        self.__rented_equipments = []

    @property
    def return_id(self):
        return self.id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.phone_number = phone_number

    @property
    def rented_equipments(self):
        return self.rented_equipments

    @rented_equipments.setter
    def rented_equipments(self, equipments):
        self.rented_equipments.append(equipments)
