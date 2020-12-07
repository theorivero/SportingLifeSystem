from limit.abstract_screen import AbstractScreen


class CustomerScreen(AbstractScreen):

    def __init__(self, customer_controller):
        super().__init__()
        self__controller = customer_controller

    def screen_options(self):
        print(' ---- Customer Screen ---- ')
        print("Choose option")
        print("1: Register Customer")
        print("2: Modify Customer")
        print("3: List Customers")
        print("4: Delete Customer")
        print("0: Return Screen")

        option = self.check_option_int_number('Choose Number: ', [0, 1, 2, 3, 4])
        return option

    def request_customer_data(self, type_method):
        print(f"---- {type_method}Customer Data ----")
        name = self.check_letters(f"{type_method}Customer Name: ")
        phone_number = self.check_int(f'{type_method}Customer Phone Number: ')
        return {"name": name, "phone_number": phone_number}

    def choose_customer_index(self, indexs, len_list_costumers):
        if len_list_costumers == 0:
            print('0 Registered Costumers')
            return -1
        print(f"---- Choose Customer ----")
#testar
        index = self.check_option_int_number(f'Nº of the customer: ', indexs)
        return index-1

    def shows_customer_data(self, i, name, phone_number):
        if i == 1:
            print("---- Customers List ----")
        print(f"Customer N°{i}")
        print(f"Customer Name: {name}")
        print(f"Customer Phone Number: {phone_number}")
        print("------------------------")

    def num_registered_customers(self, customers):
        print(f"{len(customers)} Registered Customers.")

    def del_customer(self):
        print("Successful deleted!")
