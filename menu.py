from customer import *
from equipment import *
from rent import *
import time
import sys

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
        print('Cliente cadastrado com sucesso')
    
    def start(self):
        choice = 0
        while choice != 5:
            print("************MAIN MENU**************")
            time.sleep(1)
            print()
            choice = int(input("""
1: Cadastrar Cliente
2: Cadastrar Equipamento
3: Ver base de clientes
4: Ver estoque de equipamentos
5: Fechar sistema


Por favor escolha a opção: """))
            if choice == 1: 
                self.register_customer()
                time.sleep(1)
            if choice == 2: 
                print('Escolha 2')
            if choice == 3: 
                for customer in self.customer_base: 
                    print( customer.name, customer.phone_number )
                time.sleep(4)
            if choice == 4: 
                print('Escolha 4')
        print('Sistema fechado com sucesso')