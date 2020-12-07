from limit.report_screen import ReportScreen

from entity.equipment import Equipment
from dao.equipmentdao import EquipmentDao
from dao.customerdao import CustomerDao
from dao.rentdao import RentDao

class ReportController:
    def __init__(self):
        self.__equipmentdao = EquipmentDao()
        self.__customerdao = CustomerDao()
        self.__rentdao = RentDao()
        self.__report_values = {}

        self.__report_screen = ReportScreen()
    
    @property
    def rents(self):
        return self.__rentdao.get_all()
    
    @property
    def customers(self):
        return self.__customerdao.get_all()
    
    @property
    def equipments(self):
        return self.__equipmentdao.get_all()

    def get_customer_report_data(self):
        customers = self.customers

        self.__report_values['quantity_customers'] = len(customers)

    def get_equipment_report_data(self):
        equipments = self.equipments
        total_available_quantity = 0
        total_quantity = 0
        for equipment in equipments:
            total_available_quantity += equipment.available_quantity
            total_quantity += equipment.total_quantity

        self.__report_values['equipments_total_quantity'] = total_quantity
        self.__report_values['equipments_available_quantity'] = total_available_quantity
        self.__report_values['quantity_equipments'] = len(equipments)

    def get_rent_report_data(self):
            rents = self.rents
            total_rents = len(rents)
            total_money = 0
            total_rent_weeks = 0
            for rent in rents:
                total_money += rent.price
                total_rent_weeks += rent.weeks_quantity

            self.__report_values['total_rents'] = total_rents
            self.__report_values['total_money'] = total_money
            self.__report_values['total_rent_weeks'] = total_rent_weeks

    def open_screen(self):
        self.get_equipment_report_data()
        self.get_customer_report_data()
        self.get_rent_report_data()
        switcher = { None: self.__report_screen.close_screen
                    }
                
        
        chosen_option, dict = self.__report_screen.screen_options(self.__report_values)
        chosen_method = switcher[chosen_option]
        chosen_method()
