

class SystemScreen:
    def __init__(self, systemcontroller):
        self.__controller = systemcontroller

    def screen_options(self):
        print(' ---- System ---- ')
        print("Choose option")
        print("1: Screen Customer")
        print("2: Screen Equipment")
        print("3: Screen Rent")
        print("0: System Exit")

        option = int(input("Choose option: "))
        return option