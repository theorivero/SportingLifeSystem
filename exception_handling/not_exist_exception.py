class NotExistException(Exception):
    def __init__(self):
        self.mensagem = "Digite Alguma coisa"
        super().__init__(self.mensagem)