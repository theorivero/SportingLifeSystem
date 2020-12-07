from dao.abstractdao import DAO
from entity.equipment import Equipment

class EquipmentDao(DAO):

    def __init__(self):
        super().__init__('equipment.pkl')

    def add(self, equipment: Equipment):
        if (isinstance(equipment, Equipment) and (equipment is not None)):
            super().add(equipment.name, equipment)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)