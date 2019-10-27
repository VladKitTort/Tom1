with open('lesson_5_task_3_txt.txt', 'r') as f:
    summ = []
    pop = []
    line = f.read().split('\n')
    for i in line:
        i = i.split()
        if int(i[1]) < 20000:
            pop.append(i[0])
        summ.append(i[1])
    dip = int(sum(map(int, summ)) / len(summ))
    print(f'Сотрудники с ЗП ниже 20000 рублей: {pop}')
    print(f'Средняя зарплата сотрудников компании состовляет: {dip} рублей')