from limit.customer_screen import CustomerScreen
from limit.customer_screen_2 import CustomerCreateScreen
from entity.customer import Customer
from dao.customerdao import CustomerDao


class CustomerController:
    __instance = None

    def __init__(self):
        self.__customerdao = CustomerDao()

        self.__customer_screen = CustomerScreen()
        self.__customer_create_screen = CustomerCreateScreen()

    def __new__(cls):
        if CustomerController.__instance is None:
            CustomerController.__instance = object.__new__(cls)
        return CustomerController.__instance

    @property
    def customerdao(self):
        return self.__customerdao

    @property
    def customers(self):
        return self.__customerdao.get_all()

    @property
    def customer_screen(self):
        return self.__customer_screen

    @property
    def customer_create_screen(self):
        return self.__customer_create_screen

    @staticmethod
    def system_exit():
        exit(0)

    def register_customer(self, name, phone_number):
        new_customer = Customer(name, phone_number)
        self.customerdao.add(new_customer)
        self.__customer_screen.show_message('Register', 'Successful registered')

    def modify_customer(self, name, phone_number, option):
        new_customer = Customer(name, phone_number)
        self.customerdao.remove(option[0][0].split()[-1])
        self.customerdao.add(new_customer)
        self.__customer_screen.show_message('Modify', 'Successful modified')

    def del_customer(self, option):
        self.customerdao.remove(option[0][0].split()[-1])
        self.__customer_screen.show_message('Del', 'Successful deleted')

    def open_screen(self):
        chosen_option, dicti = self.__customer_screen.screen_options([f"Name: {customer.name} | Phone: {customer.phone_number}" for customer in self.__customerdao.get_all()])
        switcher = {'createcustomer': self.open_create_screen,
                    'modifycustomer': self.open_modify_screen,
                    'deletecustomer': self.del_customer,
                    None: self.__customer_screen.close_screen
                    }
        self.__customer_screen.close_screen()
        if (chosen_option == 'modifycustomer') or (chosen_option == 'deletecustomer'):
            chosen_method = switcher[chosen_option]
            chosen_method(dicti)
        else:
            chosen_method = switcher[chosen_option]
            chosen_method()

    def open_create_screen(self):
        chosen_option, dicti = self.__customer_create_screen.screen_options()
        if chosen_option is None:
            self.__customer_create_screen.close_screen()
        else:
            self.__customer_create_screen.close_screen()
            self.register_customer(dicti['name'], dicti['phone'])

    def open_modify_screen(self, option):
        if len(self.customers) == 0:
            self.__customer_screen.show_message('Error', '0 Registered Customers')
        else:
            chosen_option, dicti = self.__customer_create_screen.screen_options()
            if chosen_option is None:
                self.__customer_create_screen.close_screen()
            else:
                self.__customer_create_screen.close_screen()
                self.modify_customer(dicti['name'], dicti['phone'], option)
