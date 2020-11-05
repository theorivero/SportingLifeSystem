class EquipmentScreen:
    def __init__(self, equipment_controller):
        self__controller = equipment_controller

    def screen_options(self):
        print(' ---- Register Equipment ---- ')
        print("Choose option")
        print("1: Register Equipment")
        print("2: Modify Equipment")
        print("3: List Equipment")
        print("0: Return Screen")

        option = int(input("Choose option: "))
        return option

    def request_equipment_data(self):
        print("---- Register Equipment ----")
        name = input("Equipment Name: ")
        total_quantity = input("Equipment quantity: ")
        available_quantity = input("Equipment available quantity: ")
        rental_price = input("Equipment rental price: ")
        return {"name": name,"total_quantity":total_quantity, "available_quantity":available_quantity, "rental_price":rental_price}

    def shows_equipment_data(self, name: str):
        print("Name: ", name)