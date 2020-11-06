from limit.customer_screen import CustomerScreen
from entity.customer import Customer


class CustomerController:

    def __init__(self, system_controller):
        self.__customers = []
        self.__controller = system_controller
        self.__customer_screen = CustomerScreen(self)
        self.__displaying_screen = True

    @property
    def customers(self):
        return self.__customers

    @property
    def customer_screen(self):
        return self.__customer_screen

    def register_customer(self):
        customer_data = self.__customer_screen.request_customer_data("")
        new_customer = Customer(customer_data["name"], customer_data["phone_number"])
        self.__customers.append(new_customer)

    def list_customers(self):
        i = 0
        for customer in self.__customers:
            i += 1
            self.__customer_screen.shows_customer_data(i, customer.name, customer.phone_number)
        self.__customer_screen.num_registered_customers(self.__customers)

    def delete_customer(self):
        i = 0
        for customer in self.__customers:
            i += 1
            self.__customer_screen.shows_customer_data(i, customer.name, customer.phone_number)
        indexs = range(1, i + 1)
        index_delete = self.__customer_screen.choose_customer_index(indexs, len(self.__customers))
        if index_delete == -1:
            return None
        self.__customer_screen.del_customer()
        del self.__customers[index_delete]

    def modify_customer(self):
        i = 0
        for customer in self.__customers:
            i += 1
            self.__customer_screen.shows_customer_data(i, customer.name, customer.phone_number)
        indexs = range(1, i + 1)
        index_modify = self.__customer_screen.choose_customer_index(indexs, len(self.__customers))
        if index_modify == -1:
            return None
        new_data_costumer = self.__customer_screen.request_customer_data("New ")
        modified_customer = self.__customers[index_modify]
        modified_customer.name = new_data_costumer['name']
        modified_customer.phone_number = new_data_costumer['phone_number']
        self.__customers[index_modify] = modified_customer

    def return_screen(self):
        self.__displaying_screen = False

    def open_screen(self):
        switcher = {0: self.return_screen, 1: self.register_customer, 2: self.modify_customer, 3: self.list_customers, 4: self.delete_customer}
        while self.__displaying_screen:
            chosen_option = self.__customer_screen.screen_options()
            chosen_method = switcher[chosen_option]
            chosen_method()
