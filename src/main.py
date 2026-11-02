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


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalize: bool = False,
        vocabulary: list = None
    ):
        if vocabulary is None:
            self.vocabulary = ['sarina', 'nika', 'armita', 'hamidreza']
        
        self.num_of_words = num_of_words
        self.capitalize = capitalize
        self.separator = separator
       
    def generate(self):
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() for word in password_words]

        print(self.separator.join(password_words))

password_generator = MemorablePasswordGenerator(capitalize=True)
password_generator.generate()
        

password_generator = RandomPasswordGenerator(length=8, include_numbers=True, include_symbols=True)
password_generator.generate()

password_generator = PinGenerator(length=8)
password_generator.generate()

