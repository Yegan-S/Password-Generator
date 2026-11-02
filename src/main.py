from abc import ABC, abstractmethod
import random
import string


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        print(''.join([random.choice(string.digits) for _ in range(self.length)]))

class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self):
         print(''.join([random.choice(self.characters) for _ in range(self.length)]))  

password_generator = RandomPasswordGenerator(length=8, include_numbers=True, include_symbols=True)
password_generator.generate()

password_generator = PinGenerator(length=8)
password_generator.generate()

