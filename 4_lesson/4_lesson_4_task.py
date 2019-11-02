from random import randint
my_list = [randint(0, 20) for el in range(100)]
new_list = [el for el in dict.fromkeys(my_list)]
print(f"Исходный список: {my_list} ")
print(f"Новый список: {new_list} ")