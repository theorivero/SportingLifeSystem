from abc import ABC, abstractmethod
from exception_handling.letter_exception import LetterException
import string

class AbstractScreen(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def screen_options(self):
        pass

    def check_option_int_number(self, msg, valid_ints):
        while True:
            check_value = input(msg)
            try:
                integer = int(check_value)
                if valid_ints and integer not in valid_ints:
                    raise ValueError
                return integer
            except ValueError:
                print("Incorrect Value: Choose another valid int: ")

    def check_int(self, msg):
        while True:
            check_value = input(msg)
            try:
                integer = int(check_value)
                if integer < 0:
                    raise ValueError
                return integer
            except ValueError:
                print("Only insert numbers.")

    def check_letters(self, msg):
        while True:
            check_str = input(msg)
            try:
                for letter in check_str:
                    if letter.lower() not in list(string.ascii_lowercase):
                        raise LetterException
                return check_str
            except Exception:
                print("Only insert letters.")
