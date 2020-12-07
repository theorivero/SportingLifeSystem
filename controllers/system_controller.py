from limit.system_screen import SystemScreen
from controllers.customer_controller import CustomerController
from controllers.equipment_controller import EquipmentController
from controllers.report_controller import ReportController
from controllers.rent_controller import RentController

class SystemController:
    __instance = None

    def __init__(self):
        self.__system_screen = SystemScreen()
        self.__customer_controller = CustomerController()
        self.__equipment_controller = EquipmentController()
        self.__report_controller = ReportController()
        self.__rent_controller = RentController()

    def __new__(cls):
        if SystemController.__instance is None:
            SystemController.__instance = object.__new__(cls)
        return SystemController.__instance

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
    
    def open_report(self):
        self.__report_controller.open_screen()

    def system_exit(self):
        exit(0)

    def open_screen(self):
        switcher = {'customerscreen': self.register_customer,
                        'equipmentscreen': self.register_equipment,
                        'rentscreen': self.register_rent,
                        'reportscreen': self.open_report,
                        'exit': self.system_exit,
                        None: self.system_exit
                    }
        while True:
            chosen_option, dict = self.__system_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()