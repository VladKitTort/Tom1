class Stationery:
    title = 'название'

    def draw(self):
        print('Запуск отрисовки. Class Stationery.')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки. Class Pen')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки. Class Pencil')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки. Class Handle')

stationery_a = Stationery()
stationery_a.draw()

stationery_b = Pen()
stationery_b.draw()

stationery_c = Pencil()
stationery_c.draw()

stationery_d = Handle()
stationery_d.draw()