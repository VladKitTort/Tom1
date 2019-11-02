name_1 = input('Ваше имя: ')
surname_1 = input('Ваша фамилия: ')
year_1 = int(input('Ваш год рождения: '))
city_1 = input('Ваш город проживания: ')
email_1 = input('Ваш email: ')
number_1 = int(input('Ваш контактный номер телефона: '))

def user(name, surname, year, city, email, number):
    print(f'Имя- {name}; Фамилия- {surname}; Год рождения- {year}; Город проживания- {city};  Ваш email- {email}; Ваш номер телефона- {number};')

user(name=name_1, surname=surname_1, year=year_1, city=city_1, email=email_1, number=number_1,)