from limit.rent_screen import RentScreen
from entity.rent import Rent
from controllers.customer_controller import CustomerController
from controllers.equipment_controller import EquipmentController

class RentController:

    def __init__(self, systemcontroller):
        self.__rents = []
        self.__equipments = []
        self.__customers = []
        self.__controller = systemcontroller
        self.__rent_screen = RentScreen(self)
        self.__displaying_screen = True

    def register_rent(self):

        rent_data = self.__rent_screen.request_rent_data()
        new_rent = Rent()
        self.__rents.append(new_rent)

    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self, equipments, customers):
        self.__equipments = equipments
        self.__customers = customers
        """switcher = {0: self.return_screen,
                    1: self.register_equipment,
                    2: self.modify_equipment,
                    3: self.list_equipments,
                    4: self.delete_equipment}
        while self.__displaying_screen:
            #chosen_option = self.__equipment_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()"""

        print(self.__equipments,self.__customers)