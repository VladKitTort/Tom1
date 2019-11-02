from math import factorial
def fibo_gen():
    for el in range(1, 16):
        yield el
pop = fibo_gen()
print(pop)
for el in pop:
    print('Факториал от 1 до 15: ', factorial(el))
i = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15
print('Факториал 15: ', i)