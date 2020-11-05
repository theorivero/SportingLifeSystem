from limit.equipment_screen import EquipmentScreen
from entity.equipment import Equipment

class EquipmentController:

    def __init__(self, systemcontroller):
        self.__equipaments = []
        self.__controller = systemcontroller
        self.__equipment_screen = EquipmentScreen(self)
        self.__displaying_screen = True

    def register_equipment(self):
        equipment_data = self.__equipment_screen.request_equipment_data()
        new_equipment = Equipment(equipment_data["name"], equipment_data["total_quantity"], 
                                    equipment_data["available_quantity"],equipment_data["rental_price"])
        self.__equipaments.append(new_equipment)
    
    def list_equipments(self):
        for equipment in self.__equipaments:
            self.__equipment_screen.shows_equipment_data(equipment.name)

    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self):
        switcher = {0: self.return_screen,
                    1: self.register_equipment,
                    3: self.list_equipments}
        while self.__displaying_screen:
            chosen_option = self.__equipment_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()