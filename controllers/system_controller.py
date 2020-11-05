from limit.system_screen import SystemScreen
from controllers.customer_controller import CustomerController


class SystemController:
    def __init__(self):
        self.__system_screen = SystemScreen(self)
        self.__customer_controller = CustomerController(self)

    def start_system(self):
        self.open_screen()

    def register_customer(self):
        self.__customer_controller.open_screen()

    def register_equipment(self):
        pass

    def register_rent(self):
        pass

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