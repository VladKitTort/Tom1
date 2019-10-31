import json

with open('lesson_5_task_7_txt.txt') as f_1:
    dip = 0
    i = []
    n = []
    f = []
    pol = []

    for line in f_1:
        pop = line.split()
        n.append(pop[0])
        nom = int(pop[2]) - int(pop[3])
        f.append(nom)
        if nom > 0:
            i.append(nom)

    dip = int(sum(map(int, i)) / len(i))
    nip = dict(zip(n, f))
    l = {'Средняя прибль компаний': dip}
    print(dip)
    ui = (nip, l)
    print(ui)

with open("my_file.json", "w") as write_f:
    json.dump(ui, write_f)