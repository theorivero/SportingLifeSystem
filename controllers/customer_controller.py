from limit.customer_screen import CustomerScreen
from entity.customer import Customer


class CustomerController:

    def __init__(self, systemcontroller):
        self.__customers = []
        self.__controller = systemcontroller
        self.__customer_screen = CustomerScreen(self)
        self.__displaying_screen = True

    def register_customer(self):
        customer_data = self.__customer_screen.request_customer_data()
        new_customer = Customer(customer_data["name"], customer_data["phone_number"])
        self.__customers.append(new_customer)

    def list_customers(self):
        for customer in self.__customers:
            self.__customer_screen.shows_customer_data(customer.name)

    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self):
        switcher = {0: self.return_screen,
                    1: self.register_customer,
                    3: self.list_customers}
        while self.__displaying_screen:
            chosen_option = self.__customer_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()