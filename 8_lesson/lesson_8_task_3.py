class checking_list(Exception):

    def __init__(self, text):
        self.text = text

try:
    text_list = input('Введите что-нибудь: ')
    print(type(text_list))
    if type(text_list) is bool:
        raise TypeError('Введент не подходящий тип данных.')
    elif type(text_list) is str:
        raise TypeError('Введент не подходящий тип данных.')
    else:
        print(f'Ваш текст- {text_list}')

except TypeError:
    print('Не соответствующий тип данных.')

