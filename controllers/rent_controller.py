from limit.rent_screen import RentScreen
from entity.rent import Rent


class RentController:

    def __init__(self, system_controller):
        self.__rents = []
        self.__controller = system_controller
        self.__rent_screen = RentScreen(self)
        self.__displaying_screen = True

    def register_rent(self):
        rent_data = self.__rent_screen.request_rent_data('')
        customers = self.__controller.customer_controller.customers
        rent_customer = None
        rent_equipment = None
        if len(customers) == 0:
            return self.__controller.customer_controller.list_customers()
        for customer in customers:
            if customer.phone_number == rent_data['customer_phone_number']:
                rent_customer = customer
        '''equipments = self.__controller.equipment_controller.equipments
        if len(equipments) == 0:
            return self.__controller.equipment_controller.list_equipments
        for equipment in equipments:
            if equipment.name == rent_data['equipment_name']:
                rent_equipment = equipment'''
        rent_customer.__rented_equipments.append(rent_equipment)
        #rent_equipment.__available_quantity -= rent_data['rental_quantity']
        new_rent = Rent(rent_customer, rent_equipment, rent_data['rental_quantity'], rent_data['rental_start'],
                        rent_data['rental_deadline'])
        self.__rents.append(new_rent)

    def list_rents(self):
        i = 0
        for rent in self.__rents:
            i += 1
            self.__rent_screen.shows_rent_data(i, rent.customer.name, rent.customer.phone_number, rent.equipment.name,
                                               rent.rental_quantity, rent.rental_start, rent.rental_deadline)
        self.__rent_screen.num_registered_rents(self.__rents)

    def delete_rent(self):
        pass

    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self):
        switcher = {0: self.return_screen,
                    1: self.register_rent,
                    2: self.list_rents,
                    3: self.delete_rent}
        while self.__displaying_screen:
            chosen_option = self.__rent_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()
