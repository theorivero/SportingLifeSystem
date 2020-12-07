from dao.abstractdao import DAO
from entity.customer import Customer

class CustomerDao(DAO):

    def __init__(self):
        super().__init__('customers.pkl')

    def add(self, customer: Customer):
        if (isinstance(customer, Customer) and (customer is not None)):
            super().add(customer.phone_number, customer)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)