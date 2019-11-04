f_1 = open('lesson_5_task_6_txt.txt')


sujects = {}

for line in f_1:
    suject, lect, pract, lab = line.split()
    sujects[suject] = int(lect) + int(pract) + int(lab)

f_1.close()

print(sujects)
