import PySimpleGUI as sg


class CustomerView:

    def __init__(self):
        self.__window = None
        self.__clientes = ["cliente 1","cliente 2","cliente 3","cliente 4"]
        self.init_components()

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Nome:   ', size=(7, 1)),sg.Input(default_text="Digite seu nome", key='name',size=(30, 1))],
            [sg.Text('Telefone:', size=(7, 1)),sg.Input(default_text="Digite seu telefone", key='phone',size=(30, 1))],
            [sg.Btn('Criar Cliente')],
            [sg.Listbox(values=self.__clientes, size=(30,5))],
            [sg.Btn('Excluir'),sg.Btn('Modificar')],
            [sg.Btn('Voltar')]
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

view = CustomerView()
view._open()