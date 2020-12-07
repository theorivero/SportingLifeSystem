from limit.abstract_screen import AbstractScreen
import PySimpleGUI as sg

class ReportScreen(AbstractScreen):

    def __init__(self):
        super().__init__()
        self.__window = None

    def init_components(self, report_values):
        sg.theme('DarkGrey5')
        layout = [
            [sg.Text('Nº de Clientes: ', size=(14, 1)), sg.Text(report_values["quantity_customers"])],
            [sg.Text('Nº de equipamentos diferentes: ', size=(25, 1)), sg.Text(report_values["quantity_equipments"])],
            [sg.Text('Nº total de equipamentos: ', size=(25, 1)), sg.Text(report_values["equipments_total_quantity"])],
            [sg.Text('Nº de equipamentos disponíveis: ', size=(25, 1)), sg.Text(report_values["equipments_available_quantity"])],
            [sg.Text('Nº de aluguéis: ', size=(25, 1)), sg.Text(report_values["total_rents"])],
            [sg.Text('Faturamento em R$: ', size=(25, 1)), sg.Text(report_values["total_money"])],
            [sg.Text('N° de semanas alugadas: ', size=(25, 1)), sg.Text(report_values["total_rent_weeks"])],
        ]
        self.__window = sg.Window('Report', layout=layout, size=(500,250), finalize=True)

    def screen_options(self, report_values):
        self.init_components(report_values)
        button, values = self.__window.Read()
        return button, values

    def close_screen(self):
        self.__window.Close()

    @staticmethod
    def show_message(title, message):
        sg.Popup(title, message)