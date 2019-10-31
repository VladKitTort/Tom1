
m_str = input('Напишите что лежит у вас на столе: ').split()
li = 0
print(f'Ваш список: {m_str}')
while li + 1 < len(m_str):
    if li % 2 == 0:
        m_str.insert(li, m_str.pop(li + 1))
    li+=1
print(f'Измененный список: {m_str}')
