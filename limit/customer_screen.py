
class CustomerScreen:
    def __init__(self, customer_controller):
        self__controller = customer_controller

    def screen_options(self):
        print(' ---- Register Customer ---- ')
        print("Choose option")
        print("1: Register Customer")
        print("2: Modify Customer")
        print("3: List Customers")
        print("0: Return Screen")

        option = int(input("Choose option: "))
        return option

    def request_customer_data(self):
        print("---- Register Customer ----")
        name = input("Customer Name: ")
        phone_number = input("Customer Phone Number: ")
        return {"name": name, "phone_number": phone_number}

    def shows_customer_data(self, name: str):
        print("Name: ", name)