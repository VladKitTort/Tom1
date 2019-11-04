class Division_numbers(Exception):

    def __init__(self, text):
        self.text = text

try:

    inp_number_1 = int(input('Введите первое число: '))
    inp_number_2 = int(input('Введите торое число: '))

    inp_number_1 = int(inp_number_1)
    inp_number_2 = int(inp_number_2)
    result_dividing = inp_number_1 / inp_number_2
except ZeroDivisionError:
    print('На ноль делить нельзя.')
except ValueError:
    print('Вы ввели не число')
except Division_numbers as err:
    print(err)
else:
    print(f'Итог деления ваших чисел: {result_dividing}')