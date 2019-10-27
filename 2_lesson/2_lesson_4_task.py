m_list = input('Напишите нескколько слов: ')
for ind, el, in enumerate(m_list.split(), 1):
    print(ind, el[:10])

