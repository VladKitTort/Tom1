name = 'Miki'
mass = 34

print(name)
print(int(mass))

print(type(name))
print(type(mass))

yourName = input('Введите ваше смешное прозвище: ')
growth = int(input('Напишите Ваш рост: '))

print('Вы уверины, что {} ваше самое смешное прозвище?'.format(yourName))
print('{} метра, многовато будет.'.format(growth))

bike = int(input('Сколько весил ваш первый велосипед? '))
speed = int(input('Самая большая скорость которую вы развивали на велосипеде: '))
dog = input('Имя вашей первой сабаки: ')

print('{} катала ваш {} килограмовый велосипед со скоростью {} километров в час.'.format(dog, bike, speed))