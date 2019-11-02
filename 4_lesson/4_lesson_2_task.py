from random import randint
my_list = randint(range(0, 20))
i = [el for num, el in enumerate(my_list) if my_list[num] > my_list[num-1]]
print(i)