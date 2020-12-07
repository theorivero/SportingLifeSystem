from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg


class RentScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self, rents):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Listbox(values=rents, size=(60,5))],
            [sg.Btn('Criar Aluguel', key='createrent'),sg.Btn('Modificar', key='modifyrent'), sg.Btn('Excluir', key='deleterent')]
        ]
        self.__window = sg.Window('Customer Screen', layout=layout, size=(500,150), finalize=True)

    def screen_options(self, rents):
        self.init_components(rents)
        button, values = self.__window.Read()
        return button, values

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)
