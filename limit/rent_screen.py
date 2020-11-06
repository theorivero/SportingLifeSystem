from limit.abstract_screen import AbstractScreen

class RentScreen(AbstractScreen):
    def __init__(self, rent_controller):
        super().__init__()
        self__controller = rent_controller

    def screen_options(self):
        print(' ---- Rent Screen ---- ')
        print("Choose option")
        print("1: Register Rent")
        print("2: Modify Rent")
        print("3: List Rent")
        print("4: Delete Rent")
        print("0: Return Screen")

        option = AbstractScreen.check_option_int_number(self, 'Choose Number: ', [0, 1, 2, 3, 4])
        return option

    def request_rent_data(self, type_method):
        print("---- Register Rent ----")
        customer_phone_number = AbstractScreen.check_int(self, f'{type_method}Customer Phone Number: ')
        equipment_name = AbstractScreen.check_letters(self, f"{type_method}Equipment Name: ")
        rental_quantity = AbstractScreen.check_int(self, f'{type_method}Rental Quantity: ')
        rental_start = input("Rental Start: ")
        rental_deadline = input("Rental Deadline: ")
        return {"customer_phone_number": customer_phone_number,
                "equipment_name": equipment_name,
                'rental_quantity': rental_quantity,
                'rental_start': rental_start,
                'rental_deadline': rental_deadline}

    def shows_rent_data(self, i, customer_name, customer_phone_number, equipment_name,
                        rental_quantity, rental_start, rental_deadline):
        if i == 1:
            print("---- Rents List ----")
        print(f"Rent N°{i}")
        print(f"Customer Name: {customer_name}")
        print(f"Customer Phone Number: {customer_phone_number}")
        print(f"Equipment Name: {equipment_name}")
        print(f"Equipment Rental Quantity: {rental_quantity}")
        print(f"Rental Start: {rental_start}")
        print(f"Rental Deadline: {rental_deadline}")
        print("------------------------")

    def num_registered_rents(self, rents):
        print(f"{len(rents)} Registered Rents.")

