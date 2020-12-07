from limit.equipment_screen import EquipmentScreen
from limit.equipment_screen_2 import EquipmentCreateScreen
from entity.equipment import Equipment
from dao.equipmentdao import EquipmentDao


class EquipmentController:
    __instance = None

    def __init__(self):
        self.__equipmentdao = EquipmentDao()

        self.__equipment_screen = EquipmentScreen()
        self.__equipment_create_screen = EquipmentCreateScreen()

    def __new__(cls):
        if EquipmentController.__instance is None:
            EquipmentController.__instance = object.__new__(cls)
        return EquipmentController.__instance

    @property
    def equipmentdao(self):
        return self.__equipmentdao

    @property
    def equipments(self):
        return self.__equipmentdao.get_all()

    @property
    def equipment_screen(self):
        return self.__equipment_screen

    @property
    def equipment_create_screen(self):
        return self.__equipment_create_screen

    @staticmethod
    def system_exit():
        exit(0)

    def register_equipment(self, name, total_quantity, available_quantity, rental_price):
        new_equipment = Equipment(name, total_quantity, available_quantity, rental_price)
        self.__equipmentdao.add(new_equipment)
        self.__equipment_screen.show_message('Register', 'Successful registered')

    def modify_equipment(self,  name, total_quantity, available_quantity, rental_price, option):
        new_equipment = Equipment(name, total_quantity, available_quantity, rental_price)
        self.__equipmentdao.remove(option[0][0].split()[0])
        self.__equipmentdao.add(new_equipment)
        self.__equipment_screen.show_message('Modify', 'Successful modified')

    def del_equipment(self, option):
        self.__equipmentdao.remove(option[0][0].split()[0])
        self.__equipment_screen.show_message('Del', 'Successful deleted')

    def open_screen(self):
        chosen_option, dicti = self.__equipment_screen.screen_options([f"{equipment.name} | Total quantity: {equipment.total_quantity} | Price: {equipment.rental_price}" for equipment in self.__equipmentdao.get_all()])
        switcher = {'createequipment': self.open_create_screen,
                    'modifyequipment': self.open_modify_screen,
                    'deleteequipment': self.del_equipment,
                    None: self.__equipment_screen.close_screen
                    }
        self.__equipment_screen.close_screen()
        if (chosen_option == 'modifyequipment') or (chosen_option == 'deleteequipment'):
            chosen_method = switcher[chosen_option]
            chosen_method(dicti)
        else:
            chosen_method = switcher[chosen_option]
            chosen_method()

    def open_create_screen(self):
        chosen_option, dicti = self.__equipment_create_screen.screen_options()
        if chosen_option is None:
            self.__equipment_create_screen.close_screen()
        else:
            self.__equipment_create_screen.close_screen()
            self.register_equipment(dicti['name'], dicti['total_quantity'], dicti['available_quantity'], dicti['rental_price'])

    def open_modify_screen(self, option):
        if len(self.equipments) == 0:
            self.__equipment_screen.show_message('Error', '0 Registered Equipments')
        else:
            chosen_option, dicti = self.__equipment_create_screen.screen_options()
            if chosen_option is None:
                self.__equipment_create_screen.close_screen()
            else:
                self.__equipment_create_screen.close_screen()
                self.modify_equipment(dicti['name'], dicti['total_quantity'], dicti['available_quantity'], dicti['rental_price'], option)