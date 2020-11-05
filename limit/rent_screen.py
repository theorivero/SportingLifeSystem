
class RentScreen:
    def __init__(self, rent_controller):
        self__controller = rent_controller

    def screen_options(self):
        print(' ---- Register Rent ---- ')
        print("Choose option")
        print("1: Register Rent")
        print("2: Modify Rent")
        print("3: List Rent")
        print("4: Delete Rent")
        print("0: Return Screen")

        option = int(input("Choose option: "))
        return option

    def request_rent_data(self):
        print("---- Register Rent ----")
        print('Choose Customer Index')

        customer_index = input("Customer Index: ")

        equipment_index = input("Equipment Index: ")
        return {"customer_index": customer_index, "equipment_index": equipment_index}