from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class CustomerScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self, customers):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Listbox(values=customers, size=(30,5))],
            [sg.Btn('Criar Cliente', key='createcustomer'),sg.Btn('Modificar', key='modifycustomer'), sg.Btn('Excluir', key='deletecustomer')]
        ]
        self.__window = sg.Window('Customer Screen', layout=layout, size=(300,150), finalize=True)

    def screen_options(self, customers):
        self.init_components(customers)
        button, values = self.__window.Read()
        return button, values

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)
