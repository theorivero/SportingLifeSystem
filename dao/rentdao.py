from dao.abstractdao import DAO
from entity.rent import Rent

class RentDao(DAO):

    def __init__(self):
        super().__init__('rents.pkl')

    def add(self, rent: Rent):
        if (isinstance(rent, Rent) and (rent is not None)):
            super().add(str(rent.id), rent)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)