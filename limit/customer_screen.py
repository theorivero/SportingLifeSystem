
class CustomerScreen:
    def __init__(self, customer_controller):
        self__controller = customer_controller

    def screen_options(self):
        print(' ---- Register Customer ---- ')
        print("Choose option")
        print("1: Register Customer")
        print("2: Modify Customer")
        print("3: List Customers")
        print("4: Delete Customer")
        print("0: Return Screen")

        option = int(input("Choose option: "))
        return option

    def request_customer_data(self):
        print("---- Register Customer ----")
        name = input("Customer Name: ")
        phone_number = input("Customer Phone Number: ")
        return {"name": name, "phone_number": phone_number}

    def choose_customer_index(self, customer, todo):
        print(f"---- {todo} Customer ----")
        for index, customer in enumerate(customer):
            print(f"{index+1}º {customer.name}")
        index_return = int(input(f'Nº of the customer you want to {todo}: '))
        return index_return-1

    def modify_customer_data(self):
        name = input("New Customer Name: ")
        phone_number = input("New Customer Phone Number: ")
        return {"name": name, "phone_number": phone_number}

    def shows_customer_data(self, i, name, phone_number):
        print("---- Customers List ----")
        print(f"Customer N°{i}")
        print(f"Customer Name: {name}")
        print(f"Customer Phone Number: {phone_number}")
        print("------------------------")