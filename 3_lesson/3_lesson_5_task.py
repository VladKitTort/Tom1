sum_1 = 0
def adder():
    while True:
        try:
            number = input('Введите числа через пробел для их сложения, для окончания введите "E": ')
            number_2 = number.split()
            if 'E' in number_2:
                try:
                    global sum_1
                    number_2 = list(map(float, number_2[:number_2.index('E')]))
                    sum_1 += sum(number_2)
                    print(f'Общая сумма чисел: {sum_1}. Программа окончена')
                    break
                except ValueError:
                    print('Необходимо вводить числа.')
            number_2 = list(map(float, number_2))
            sum_1 += sum(number_2)
            print(f'Общая сумма чисел: {sum_1}')
        except ValueError:
            print('Необходимо вводить числа.')
adder()