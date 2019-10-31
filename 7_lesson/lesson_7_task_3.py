class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(int(self.cells / other.cells))

    def __str__(self):
        return f'{self.cells}'

    def make_order(self, cell):
        self.cell = cell
        print(int((('*' * self.cell) + '\n') * (self.cells // self.cell)
                  + ((self.cells % self.cell) + '\n')))


square_1 = Cell(20)
square_2 = Cell(15)
square_1.make_order(5)
print(f'Сумма клеток- {square_1 + square_2}')
print(f'Разность кеток- {square_1 - square_2}')
print(f'Перемножение клеток- {square_1 * square_2}')
print(f'Деление клеток- {square_1 / square_2}')