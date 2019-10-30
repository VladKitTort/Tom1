def int_func(name):
    return name.capitalize()
print(int_func('вАсЯ'))

def int_func():
    word_list = input('Напишите список слов через пробел: ')
    return word_list
list_word = int_func()
print(list_word.capitalize())