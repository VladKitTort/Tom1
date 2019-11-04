def division():
    try:
        first = float(input('Первое число для деления - '))
        second_number = float(input('Второе число для деления - '))
        n = round((first / second_number), 2)
        return n
    except ZeroDivisionError:
        return 'Делить на "0" нельзя.'
print(division())