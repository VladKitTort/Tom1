class Complex_number:

    def __init__(self, *args):
        self.number_complex = complex(*args)

    def __str__(self):
        return f'{self.number_complex}'

    def __add__(self, other):
        return Complex_number(self.number_complex + other.number_complex)

    def __mul__(self, other):
        return Complex_number(self.number_complex * other.number_complex)


o = Complex_number(5, 27)
p = Complex_number(13, 42)
print(f'Сумма двух комплексных чисел равна: {o + p}')
print(f'Умножение двух комплексных чисел равна: {o * p}')
