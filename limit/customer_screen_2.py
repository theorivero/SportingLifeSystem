from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class CustomerCreateScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Nome:   ', size=(7, 1)),sg.Input(default_text="Digite seu nome", key='name',size=(30, 1))],
            [sg.Text('Telefone:', size=(7, 1)),sg.Input(default_text="Digite seu telefone", key='phone',size=(30, 1))],
            [sg.Btn('Criar Cliente', key='createcustomer')]

        ]
        self.__window = sg.Window('Create / Modify', layout=layout, size=(300,100), finalize=True)

    def screen_options(self):
        self.init_components()
        button, values = self.__window.Read()
        if button is None:
            return None, None
        if self.check_int(values['phone']) and self.check_letters(values['name']):
            return button, values
        else:
            self.show_message('Error', 'Try Again')
            return None, None

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)
