from limit.rent_screen import RentScreen
from entity.rent import Rent
from controllers.customer_controller import CustomerController
from controllers.equipment_controller import EquipmentController

class RentController:

    def __init__(self, systemcontroller):
        self.__rents = []
        self.__equipments =
        self.__controller = systemcontroller
        self.__rent_screen = RentScreen(self)
        self.__displaying_screen = True

    def register_rent(self):

        rent_data = self.__rent_screen.request_rent_data()



        new_rent = Rent(rent_data["name"], rent_data["phone_number"])
        self.__rents.append(new_rent)
