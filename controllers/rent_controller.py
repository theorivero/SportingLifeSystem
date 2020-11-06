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
        self.__rent_screen.shows_rent_data(self.__rents)

    def delete_rent(self):
        indexs = []
        for i,v in enumerate(self.rents):
            indexs.append(i+1)
        self.__rent_screen.shows_rent_data(self.__rents)
        index_delete = self.__rent_screen.choose_rent_index(self.rents,"Delete", indexs)
        if index_delete == -1:
            return None
        else:
            del self.rents[index_delete] 


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

