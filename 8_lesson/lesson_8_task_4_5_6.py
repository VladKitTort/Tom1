class Office_equipment_warehouse:

    def __init__(self):
        pass


class Office_equipment:

    def __init__(self, *args):
        self.name = input('Введите наименование техники- ')
        self.manufacturer = input('Введите производителя: ')
        self.price = float(input('Введите цену в рублях: '))


class Printer(Office_equipment):

    def __init__(self, name, manufacturer, price):
        super().__init__(name, manufacturer, price)

    def __str__(self):
        return f'Xerox- {self.name} {self.manufacturer}, {self.price}.'

    def characteristic(self):
        self.print_per_minute = input('Введите количесство печатуимой бумаги в минуту- ')
        self.papers_in_drawer = input('Введите объем ящика для бумаги- ')

    def data_entry(self):
        i = (f'name: {self.name}, manufacturer: {self.manufacturer}, price: {self.price},'
              f' print_time: {self.print_per_minute}, cartridge_model: {self.papers_in_drawer}')
        return dict(e.split(': ') for e in i.split(','))


class Scanner(Office_equipment):

    def __init__(self, name, manufacturer, price):
        super().__init__(name, manufacturer, price)

    def __str__(self):
        return f'Xerox- {self.name} {self.manufacturer}, {self.price}.'

    def characteristic(self):
        self.scanning_speed = input('Введите скорость печати- ')
        self.lamp_name = input('Введите наименование лампы- ')

    def data_entry(self):
        i = (f'name: {self.name}, manufacturer: {self.manufacturer}, price: {self.price},'
              f' print_time: {self.scanning_speed}, cartridge_model: {self.lamp_name}')
        return dict(e.split(': ') for e in i.split(','))


class Xerox(Office_equipment):

    def __init__(self, name, manufacturer, price):
        super().__init__(name, manufacturer, price)

    def __str__(self):
        return f'Xerox- {self.name} {self.manufacturer}- {self.price}.'

    def characteristic(self):
        self.cartridge_model = input('Введите наименование картриджа- ')
        self.print_time = input('Введите время печати- ')

    def data_entry(self):
        i = (f'name: {self.name}, manufacturer: {self.manufacturer}, price: {self.price},'
              f' print_time: {self.cartridge_model}, cartridge_model: {self.print_time}')
        return dict(e.split(': ') for e in i.split(','))

printer_1 = Printer(1, 2, 3)
printer_1.characteristic()
print(printer_1.data_entry())

scanner_1 = Scanner(1, 2, 3)
scanner_1.characteristic()
print(scanner_1.data_entry())

xerox_1 = Xerox(1, 2, 3)
xerox_1.characteristic()
print(xerox_1.data_entry())
