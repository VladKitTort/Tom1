"""
my_list = [8, 5, 3, 1]
print(my_list)
while True:
    number = int(input('Введите число от 1 до 9: '))
    if number < 10 and number > 0:
        break
my_list.append(number)
my_list.sort()
my_list.reverse()
print(my_list)
"""

my_list = [8, 5, 3, 1]
while True:
    print(f'Начальнй состав чисел: {my_list}')
    number_2 = int(input('Введите число для добовления в спсок:'))
    if number_2 != 111111:
        if my_list.count(number_2):
            my_list.insert(my_list.index(number_2) + 1, number_2)
        else:
            param = 0
            n_param = 0
            for n, i in enumerate(my_list):
                if number_2 > i:
                    if param < i:
                        param = i
                else:
                    n_param = n + 1
            my_list.insert(n_param, number_2)
    else:
        break
