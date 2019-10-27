my_dict = {1: "январь", 2:"февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
kio = int(input('Введите номер месяца: '))
for n in range(len(my_dict)):
    if kio == n + 1:
        if 3 <= kio <= 5:
            print(f'Это весна, месяц: {my_dict.get(n + 1)}')
        elif 6 <= kio <= 8:
            print(f'Это лето, месяц: {my_dict.get(n + 1)}')
        elif 9 <= kio <= 11:
            print(f'Это осень, месяц: {my_dict.get(n + 1)}')
        else:
            print(f'Это зима, месяц: {my_dict.get(n + 1)}')
