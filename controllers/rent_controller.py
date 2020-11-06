from limit.rent_screen import RentScreen
from entity.rent import Rent


class RentController:

    def __init__(self, system_controller):
        self.__rents = []
        self.__controller = system_controller
        self.__rent_screen = RentScreen(self)
        self.__displaying_screen = True

    @property
    def rents(self):
        return self.__rents

    def register_rent_(self):
        rent_data = self.__rent_screen.request_rent_data('')
        customers = self.__controller.customer_controller.customers
        equipments = self.__controller.equipment_controller
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

    def register_rent(self):
        equipment_controller = self.__controller.equipment_controller
        customer_controller = self.__controller.customer_controller

        customers = customer_controller.customers
        equipments = equipment_controller.equipments

        i = 0
        for customer in customers:
            i += 1
            customer_controller.customer_screen.shows_customer_data(i, customer.name, customer.phone_number)
        indexs_customer = range(1, i + 1)
        index_customer_rent = customer_controller.customer_screen.choose_customer_index(indexs_customer, len(customers))
        if index_customer_rent == -1:
            return None
        customer_rent = customers[index_customer_rent]

        indexs_equip = []
        for i, v in enumerate(equipment_controller.equipments):
            indexs_equip.append(i+1)
        rent_equipment_index = equipment_controller.equipment_screen.choose_equipment_index(equipments, "rent", indexs_equip)
        equipment_rent = equipments[rent_equipment_index]

        rent_data = self.__rent_screen.request_rent_data("")
        self.__rents.append(Rent(customer_rent, equipment_rent, rent_data["weeks_quantity"]))

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
