from limit.equipment_screen import EquipmentScreen
from entity.equipment import Equipment

class EquipmentController:

    def __init__(self, system_controller):
        self.__equipments = []
        self.__controller = system_controller
        self.__equipment_screen = EquipmentScreen(self)
        self.__displaying_screen = True
    
    @property
    def equipments(self):
        return self.__equipments


    def register_equipment(self):
        equipment_data = self.__equipment_screen.request_equipment_data()
        new_equipment = Equipment(equipment_data["name"], equipment_data["total_quantity"], 
                                    equipment_data["available_quantity"],equipment_data["rental_price"])
        self.__equipments.append(new_equipment)
    
    def list_equipments(self):
        self.__equipment_screen.shows_equipment_data(self.__equipments)

    def delete_equipment(self):
        index_delete = self.__equipment_screen.choose_equipment_index(self.__equipments,"Delete")
        del self.__equipments[index_delete] 
    
    def modify_equipment(self):
        index_modify = self.__equipment_screen.choose_equipment_index(self.__equipments,"Modify")
        modified_equipment = self.__equipment_screen.modify_equipment_data(self.__equipments[index_modify])
        self.__equipments[index_modify] = modified_equipment
        
    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self):
        switcher = {0: self.return_screen,
                    1: self.register_equipment,
                    2: self.modify_equipment,
                    3: self.list_equipments,
                    4: self.delete_equipment}
        while self.__displaying_screen:
            chosen_option = self.__equipment_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()
