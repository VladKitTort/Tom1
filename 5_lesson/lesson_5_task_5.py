from random import randint

summ = 0
with open('lesson_5_task_5_txt.txt', 'w') as f_12:
    for i in range(100):
        el = randint(1, 100)
        summ += el
        f_12.write(str(el) + ' ')

print(f' Сумма всех чисел: {summ}')

"""
with open('lesson_5_task_5_txt.txt', 'r') as f:
    print(*(sum(map(int, line.split())) for line in f), sep='\n')
"""