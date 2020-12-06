from limit.abstract_screen import AbstractScreen

class EquipmentScreen(AbstractScreen):
    def __init__(self, equipment_controller):
        super().__init__()
        self__controller = equipment_controller

    def screen_options(self):
        print(' ---- Register Screen ---- ')
        print("Choose option")
        print("1: Register Equipment")
        print("2: Modify Equipment")
        print("3: List Equipment")
        print("4: Delete Equipment")
        print("0: Return Screen")

        option = self.check_option_int_number('Choose Number: ', [0, 1, 2, 3, 4])
        return option

    def request_equipment_data(self, type_method):
        print("---- Register Equipment ----")
        name = self.check_exist(f"{type_method}Equipment Name: ")
        total_quantity = self.check_int(f"{type_method}Equipment quantity: ")
        available_quantity = self.check_less_than_total(f"{type_method}Equipment available quantity: ",total_quantity)
        rental_price = self.check_int(f"{type_method}Equipment rental price per week: ")
        return {"name": name,"total_quantity":total_quantity, "available_quantity":available_quantity, "rental_price":rental_price}

    def choose_equipment_index(self, equipments, action, indexs):
        if len(equipments) == 0:
            print('0 Registered Equipment')
            return -1
        print(f"---- {action} Equipment ----")
        for index,equipment in enumerate(equipments):
            print(f"{index+1}º {equipment.name}")
        index_return = self.check_option_int_number(f'Nº of the equipment you want to {action}: ', indexs)
        return index_return-1

    

    def modify_equipment_data(self, new_equipment, type_method):
        new_equipment.name = self.check_exist(f"{type_method}Equipment Name: ")
        new_equipment.total_quantity = self.check_int(f"{type_method}Equipment quantity: ")
        new_equipment.available_quantity = self.check_less_than_total(f"{type_method}Equipment available quantity: ",new_equipment.total_quantity)
        new_equipment.rental_price = self.check_int(f"{type_method}Equipment rental price per week: ")

        return new_equipment


    def shows_equipment_data(self, equipments):
        print("---- Equipment List ----")
        i = 1
        for equipment in equipments:
            print(f"Equipment N°{i}")
            print(f"Equipment Name: {equipment.name}")
            print(f"Equipment quantity: {equipment.total_quantity}")
            print(f"Equipment available quantity: {equipment.available_quantity}")
            print(f"Equipment rental price per week: {equipment.rental_price}")
            print("------------------------")
            i += 1 

        