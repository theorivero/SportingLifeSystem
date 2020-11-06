class LetterException(Exception):
    def __init__(self):
        self.mensagem = "Digite apenas letras"
        super().__init__(self.mensagem)
    