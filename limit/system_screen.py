import PySimpleGUI as sg

class SystemScreen:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Txt('                                    '),sg.Button('Clientes', size=(20, 3), key='customerscreen',  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Equipamentos', size=(20, 3), key='equipmentscreen',  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Aluguéis', size=(20, 3), key='rentscreen',  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Relatórios', size=(20, 3),  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Sair', size=(20, 3), key='exit', font=("Helvetica", 10))],
        ]
        self.__window = sg.Window('Menu', size=(500,300)).Layout(layout)

    def screen_options(self):
        button, values = self.__window.Read()
        return button, values

    def close_screen(self):
        self.__window.Close()

    def show_message(self, title: str, message: str):
        sg.Popup(title, message)