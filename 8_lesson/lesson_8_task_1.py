class Date:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return f'{self.date}'

    @classmethod
    def date_view(cls, date):
        pop = date.split('-')
        date_int = []
        for i in pop:
            i = int(i)
            date_int.append(i)
        return date_int

    @staticmethod
    def date_validation(number, month, year):
        if number <= 0 or number >= 32:
            print('Не допустимое число.')
        else:
            print('Допустимое число для даты.')

        if month <= 0 or month >= 13:
            print('Не допустимое число.')
        else:
            print('Допустимое число для месяца.')
        if year < 0:
            print('Не допустимое число.')
        elif year < 2019:
            print('Год прошлого.')
        elif year > 2019:
            print('Год будующего.')
        else:
            print('Текущий год.')


p = Date("25-07-2007")
print(p)
print(p.date_view("25-07-2007"))
print(Date.date_validation(20, 11, 2019))