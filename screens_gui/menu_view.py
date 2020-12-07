import PySimpleGUI as sg


class MenuView:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Txt('                                    '),sg.Button('Clientes', size=(20, 3),  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Equipamentos', size=(20, 3),  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Aluguéis', size=(20, 3),  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Relatórios', size=(20, 3),  font=("Helvetica", 10))],
            [sg.Txt('                                    '),sg.Button('Sair', size=(20, 3),  font=("Helvetica", 10))],
        ]
        self.__window = sg.Window('Menu', layout=layout, size=(500,300), finalize=True)

    def _open(self):
        button, values = self.__window.Read()
        print(button)
        return button, values

    def close(self):
        self.__window.Close()
    
    def show_message(self, title, message):
        sg.Popup(title, message)

dicti = {}