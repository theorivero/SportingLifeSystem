import PySimpleGUI as sg


class EquipmentView:

    def __init__(self):
        self.__window = None
        self.__equipments = ["equipamento 1","equipamento 2","equipamento 3","equipamento 4"]
        self.init_components()

    def init_components(self):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Nome do equipamento:   ', size=(14, 1)),sg.Input(default_text="Digite o nome do equipamento", key='name',size=(30, 1))],
            [sg.Text('Quantidade total:', size=(14, 1)),sg.Input(default_text="Digite a quantidade total", key='total_quantity',size=(30, 1))],
            [sg.Text('Quantidade disponível:', size=(14, 1)),sg.Input(default_text="Digite a quantidade total", key='available_quantity',size=(30, 1))],
            [sg.Text('Preço semanal:', size=(14, 1)),sg.Input(default_text="Digite o preço do aluguel semanal", key='rental_price',size=(30, 1))],
            [sg.Btn('Criar Cliente')],
            [sg.Listbox(values=self.__equipments, size=(30,5))],
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

view = EquipmentView()
view._open()