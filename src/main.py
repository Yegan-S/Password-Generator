from abc import ABC, abstractmethod
import random
import string


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class PinGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length

    def generate(self):
        print(''.join([random.choice(string.digits) for _ in range(self.length)]))

password_generator = PinGenerator(length=8)
password_generator.generate()

