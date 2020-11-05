from entity.rent import *
import time


class Menu:
    def __init__(self):
        self.__customer_base = []
        self.__stock = []

    @property
    def customer_base(self):
        return self.__customer_base

    @customer_base.setter
    def name(self, customer_base):
        self.__customer_base = customer_base
    
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    def register_customer(self):
        name = input('Qual o Nome do cliente: ')
        phone_number = input('Qual o numero do cliente: ')
        new_customer = Customer(name, phone_number)
        self.__customer_base.append(new_customer)
        time.sleep(1)
        print(f'Cliente {name} cadastrado com sucesso')

    def equipment_questions(self):
        name = input('Qual equipmento você quer cadastrar: ')
        total_quantity = input('Você tem quantos equipmentos desse tipo: ')
        available_quantity = input('Quantos estão disponiveis hoje: ')
        rental_price = input('Quanto custa o aluguel mensal desse equipmento: ')
        return name,total_quantity,available_quantity,rental_price

    def register_equipment(self):
        name,total_quantity,available_quantity,rental_price = self.equipment_questions()
        new_equipment = Equipment(name, total_quantity, available_quantity, rental_price)
        self.__stock.append(new_equipment)
        time.sleep(1)
        print(f'equipmento {name} cadastrado no estoque')

    
    def start(self):
        choice = 0
        while choice != 5:
            print("************MAIN MENU**************")
            time.sleep(1)
            print()
            choice = int(input("""
1: Cadastrar Cliente
2: Cadastrar equipmento
3: Ver base de clientes
4: Ver estoque de equipmentos
5: Fechar sistema


Por favor escolha a opção: """))
            if choice == 1: 
                self.register_customer()
                time.sleep(1)
            if choice == 2: 
                self.register_equipment()
                time.sleep(1)
            if choice == 3: 
                for customer in self.customer_base: 
                    print( customer.name, customer.phone_number )
                time.sleep(4)
            if choice == 4: 
                for equipment in self.stock: 
                    print( equipment.name, equipment.total_quantity, equipment.available_quantity, equipment.rental_price)
                time.sleep(4)
        print('Sistema fechado com sucesso')