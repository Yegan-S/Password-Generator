import random
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password.
        """
        pass


class PinGenerator(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate a random password.
    """
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters: str = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """
        Generate a password from specified characters.
        """
        return ''.join([random.choice(self.characters) for _ in range(self.length)])  


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
        self,
        num_of_words: int = 4,
        separator: str = '-',
        capitalize: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            self.vocabulary: list[str] = ['sarina', 'nika', 'armita', 'hamidreza']
        self.num_of_words: int = num_of_words
        self.capitalize: bool = capitalize
        self.separator: str = separator
       
    def generate(self) -> str:
        """
        Generate a password from a list of vocabulary words.
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize:
            password_words = [word.upper() for word in password_words]

        return  self.separator.join(password_words)

password_generator = MemorablePasswordGenerator(capitalize=True)
password_generator.generate()
        

password_generator = RandomPasswordGenerator(length=8, include_numbers=True, include_symbols=True)
password_generator.generate()

password_generator = PinGenerator(length=8)
password_generator.generate()
