from limit.abstract_screen import AbstractScreen

class RentScreen(AbstractScreen):
    def __init__(self, rent_controller):
        super().__init__()
        self__controller = rent_controller

    def screen_options(self):
        print(' ---- Rent Screen ---- ')
        print("Choose option")
        print("1: Register Rent")
        print("2: List Rent")
        print("3: Delete Rent")
        print("0: Return Screen")

        option = AbstractScreen.check_option_int_number(self, 'Choose Number: ', [0, 1, 2, 3])
        return option

    def request_rent_data(self, type_method):
        print("---- Register Rent ----")
        weeks_quantity = AbstractScreen.check_int(self, f'{type_method}Rental weeks: ')
        return {"weeks_quantity": weeks_quantity}

    def shows_rent_data(self, rents):
        i = 1
        print("---- Rents List ----")
        for rent in rents:
            print(f"Rent N°{i}")
            print(f"Customer Name: {rent.customer.name}")
            print(f"Customer Phone Number: {rent.customer.phone_number}")
            print(f"Equipment Name: {rent.equipment.name}")
            print(f"Rental weeks: {rent.weeks_quantity}")
            print(f"Rental price: {rent.price}")
            print("------------------------")
            i +=1
    def num_registered_rents(self, rents):
        print(f"{len(rents)} Registered Rents.")

    def choose_rent_index(self, rents, action, indexs):
        if len(rents) == 0:
            print('0 Registered Rents')
            return -1
        index_return = AbstractScreen.check_option_int_number(self, f'Nº of the equipment you want to {action}: ', indexs)
        return index_return-1

