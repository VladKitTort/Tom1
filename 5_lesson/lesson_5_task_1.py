out_f = open("out_file.txt", "w")
pop = []
while True:
    n = input('Введите строку: ')
    if True:
        pop.append(n)
    if not n:
        break
str_list = [el + '\n' for el in pop]
out_f.writelines(str_list)
out_f.close()

