my_dict = {el for el in range(1, 10) if el}
print('Первичный список: ', my_dict)
from functools import reduce
def my_func (prev_el, el):
        return prev_el + el
print('Сумма всех элементов спаика: ', reduce(my_func, my_dict))