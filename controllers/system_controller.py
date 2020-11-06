from limit.system_screen import SystemScreen
from controllers.customer_controller import CustomerController
from controllers.equipment_controller import EquipmentController
from controllers.rent_controller import RentController

class SystemController:
    def __init__(self):
        self.__system_screen = SystemScreen(self)
        self.__customer_controller = CustomerController(self)
        self.__equipment_controller = EquipmentController(self)
        self.__rent_controller = RentController(self)

    @property
    def customer_controller(self):
        return self.__customer_controller

    @property
    def equipment_controller(self):
        return self.__equipment_controller

    def start_system(self):
        self.open_screen()

    def register_customer(self):
        self.__customer_controller.open_screen()

    def register_equipment(self):
        self.__equipment_controller.open_screen()

    def register_rent(self):
        self.__rent_controller.open_screen()

    def system_exit(self):
        exit(0)

    def open_screen(self):
        switcher = {1: self.register_customer,
                        2: self.register_equipment,
                        3: self.register_rent,
                        0: self.system_exit}
        while True:
            chosen_option = self.__system_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()
