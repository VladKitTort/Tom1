from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):

    def calculation(self):
        return (self.size / 6.5 + 0.5)

    @property

    def consumption(self):
        return f'Размер польто- {self.size}.'

class Suit(Clothes):


    def calculation(self):
        return (2 * self.size + 0.3)

    @property

    def consumption(self):
        return f'Рост костюма- {self.size}'

cloth_1 = Coat(54)
print(cloth_1.consumption)
print(f'Суммарный расход ткани на одно польто- {round(cloth_1.calculation(), 2)}')
cloth_2 = Suit(2)
print(cloth_2.consumption)
print(f'Суммарный расход ткани на один костюм- {round(cloth_2.calculation(), 2)}')