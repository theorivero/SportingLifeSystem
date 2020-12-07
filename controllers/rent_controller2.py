from limit.rent_screen2 import RentScreen
from limit.rent_screen2_2 import RentCreateScreen
from entity.rent import Rent
from dao.rentdao import RentDao
from controllers.customer_controller import CustomerController
from controllers.equipment_controller import EquipmentController

from entity.equipment import Equipment


class RentController:
    __instance = None

    def __init__(self):
        self.__rentdao = RentDao()
        self.__rent_screen = RentScreen()
        self.__rent_create_screen = RentCreateScreen()
        self.__customer_controller = CustomerController()
        self.__equipment_controller = EquipmentController()

    def __new__(cls):
        if RentController.__instance is None:
            RentController.__instance = object.__new__(cls)
        return RentController.__instance

    @property
    def customer_controller(self):
        return self.__customer_controller

    @property
    def rents(self):
        return self.__rentdao.get_all()

    @property
    def rent_screen(self):
        return self.__rent_screen

    @property
    def rent_create_screen(self):
        return self.__rent_create_screen

    @staticmethod
    def system_exit():
        exit(0)

    def register_rent(self, phone, equipment_name, rental_weeks):
        try:
            customer = self.customer_controller.customerdao.get(phone)
            equipment = self.__equipment_controller.equipmentdao.get(equipment_name)
            new_rent = Rent(customer, equipment, rental_weeks)
            self.__rentdao.add(new_rent)
        except Exception:
            self.__rent_screen.show_message('Error', 'Try Again')

    def modify_rent(self, phone, equipment_name, rental_weeks, option):
        customer = self.customer_controller.customerdao.get(phone)
        equipment = self.__equipment_controller.equipmentdao.get(equipment_name)
        new_rent = Rent(customer, equipment, rental_weeks)
        self.__rentdao.remove(option[0][0].split()[-1])
        self.__rentdao.add(new_rent)

    def del_rent(self, option):
        self.__rentdao.remove(option[0][0].split()[-1])

    def open_screen(self):
        chosen_option, dicti = self.__rent_screen.screen_options([f'{rent.equipment.name} {rent.customer.phone_number} {rent.id}' for rent in self.__rentdao.get_all()])
        switcher = {'createrent': self.open_create_screen,
                    'modifyrent': self.open_modify_screen,
                    'deleterent': self.del_rent,
                    None: self.__rent_screen.close_screen
                    }
        self.__rent_screen.close_screen()
        if (chosen_option == 'modifyrent') or (chosen_option == 'deleterent'):
            chosen_method = switcher[chosen_option]
            chosen_method(dicti)
        else:
            chosen_method = switcher[chosen_option]
            chosen_method()

    def open_create_screen(self):
        chosen_option, dicti = self.__rent_create_screen.screen_options()
        if chosen_option is None:
            self.__rent_create_screen.close_screen()
        else:
            self.__rent_create_screen.close_screen()
            self.register_rent(dicti['phone'], dicti['equipmentname'], dicti['rentalweeks'])

    def open_modify_screen(self, option):
        if len(self.rents) == 0:
            self.__rent_screen.show_message('Error', '0 Registered Customers')
        else:
            chosen_option, dicti = self.__rent_create_screen.screen_options()
            if chosen_option is None:
                self.__rent_create_screen.close_screen()
            else:
                self.__rent_create_screen.close_screen()
                self.modify_rent(dicti['phone'], dicti['equipmentname'], dicti['rentalweeks'], option)
