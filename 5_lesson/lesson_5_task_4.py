numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

fa_in = open('lesson_5_task_4_txt_2.txt', 'w', encoding='UTF-8')
with open('lesson_5_task_4_txt.txt', encoding='UTF-8') as f_in:
    for pop in f_in:
        lop = pop.split(' - ')
        lop[1] = lop[1][:-1]
        fa_in.writelines(numbers[lop[0]] + ' - ' + lop[1] + '\n')

fa_in.close()