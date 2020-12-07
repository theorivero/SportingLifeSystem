from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class RentCreateScreen(AbstractScreen):

    def __init__(self):
        super().__init__()

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Customer Phone:', size=(14, 1)),sg.Input(default_text="Digite seu telefone", key='phone',size=(30, 1))],
            [sg.Text('Equipment Name:', size=(14, 1)), sg.Input(default_text="Digite o equipamento", key='equipmentname', size=(30, 1))],
            [sg.Text('Rental weeks:', size=(14, 1)), sg.Input(default_text="Digite as semanas", key='rentalweeks', size=(30, 1))],
            [sg.Btn('Criar Rent', key='createrent')]

        ]
        self.__window = sg.Window('Create / Modify', layout=layout, size=(350,120), finalize=True)

    def screen_options(self):
        self.init_components()
        button, values = self.__window.Read()
        if button is None:
            return None, None
        if self.check_int(values['phone']) and self.check_letters(values['equipmentname']) and \
                self.check_int(values['rentalweeks']):
            return button, values
        else:
            self.show_message('Error', 'Try Again')
            return None, None

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)
