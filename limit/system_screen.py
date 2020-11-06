from limit.abstract_screen import AbstractScreen

class SystemScreen(AbstractScreen):
    def __init__(self, system_controller):
        super().__init__()
        self.__controller = system_controller

    def screen_options(self):
        print(' ---- System ---- ')
        print("Choose option")
        print("1: Screen Customer")
        print("2: Screen Equipment")
        print("3: Screen Rent")
        print("0: System Exit")

        option = AbstractScreen.check_option_int_number(self, 'Choose Number: ', [0, 1, 2, 3])
        return option