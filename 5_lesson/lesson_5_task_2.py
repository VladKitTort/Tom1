with open('str_1_2_3.txt') as pop:
    line = 0
    for i in pop:
        line += 1
        words = i.split(' ')
        print(f'Файл str_1_2_3.txt: в строке № {line} {len(words)} слова')
    print(f'В файле str_1_2_3.txt общее количество строк {line}.')