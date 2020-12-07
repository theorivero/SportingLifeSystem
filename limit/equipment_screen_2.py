from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class EquipmentCreateScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Nome do equipamento:   ', size=(17, 1)),sg.Input(default_text="Digite o nome do equipamento", key='name',size=(30, 1))],
            [sg.Text('Quantidade total:', size=(17, 1)),sg.Input(default_text="Digite a quantidade total", key='total_quantity',size=(30, 1))],
            [sg.Text('Quantidade disponível:', size=(17, 1)),sg.Input(default_text="Digite a quantidade total", key='available_quantity',size=(30, 1))],
            [sg.Text('Preço semanal:', size=(17, 1)),sg.Input(default_text="Digite o preço do aluguel semanal", key='rental_price',size=(30, 1))],
            [sg.Btn('Cadastrar Equipamento')]
        ]
        self.__window = sg.Window('Create / Modify', layout=layout, size=(450,150), finalize=True)

    def screen_options(self):
        self.init_components()
        button, values = self.__window.Read()
        if self.check_int(values['total_quantity']) and self.check_int(values['available_quantity'])  and self.check_int(values['rental_price']):
            return button, values
        else:
            self.show_message('Error', 'Try Again')
            return None, None

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)
