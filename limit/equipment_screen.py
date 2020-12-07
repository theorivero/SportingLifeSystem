from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class EquipmentScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self, equipments):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Listbox(values=equipments, size=(30,5))],
            [sg.Btn('Criar Equipamento', key='createequipment'),sg.Btn('Modificar', key='modifyequipment'), sg.Btn('Excluir', key='deleteequipment')]
        ]
        self.__window = sg.Window('Equipment Screen', layout=layout, size=(300,150), finalize=True)

    def screen_options(self, equipments):
        self.init_components(equipments)
        button, values = self.__window.Read()
        return button, values

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)

        