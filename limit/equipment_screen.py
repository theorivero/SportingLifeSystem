from limit.abstract_screen import AbstractScreen

class EquipmentScreen(AbstractScreen):
    def __init__(self, equipment_controller):
        super().__init__()
        self__controller = equipment_controller

    def screen_options(self):
        print(' ---- Register Equipment ---- ')
        print("Choose option")
        print("1: Register Equipment")
        print("2: Modify Equipment")
        print("3: List Equipment")
        print("4: Delete Equipment")
        print("0: Return Screen")

        option = AbstractScreen.check_option_int_number(self, 'Choose Number: ', [0, 1, 2, 3, 4])
        return option

    def request_equipment_data(self):
        print("---- Register Equipment ----")
        name = input("Equipment Name: ")
        total_quantity = input("Equipment quantity: ")
        available_quantity = input("Equipment available quantity: ")
        rental_price = input("Equipment rental price: ")
        return {"name": name,"total_quantity":total_quantity, "available_quantity":available_quantity, "rental_price":rental_price}

    def choose_equipment_index(self, equipments, todo):
        print(f"---- {todo} Equipment ----")
        for index,equipment in enumerate(equipments):
            print(f"{index+1}º {equipment.name}")
        index_return = int(input(f'Nº of the equipment you want to {todo}: '))
        return index_return-1

    def modify_equipment_data(self, equipment):
        equipment.name = input("New Equipment Name: ")
        equipment.total_quantity = input("New Equipment quantity: ")
        equipment.available_quantity = input("New Equipment available quantity: ")
        equipment.rental_price = input("New Equipment rental price: ")
        return equipment


    def shows_equipment_data(self, equipments):
        print("---- Equipment List ----")
        i = 1
        for equipment in equipments:
            print(f"Equipment N°{i}")
            print(f"Equipment Name: {equipment.name}")
            print(f"Equipment quantity: {equipment.total_quantity}")
            print(f"Equipment available quantity: {equipment.available_quantity}")
            print(f"Equipment rental price: {equipment.rental_price}")
            print("------------------------")
            i += 1 

        