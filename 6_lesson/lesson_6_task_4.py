import random

class Car:

    def characteristics_Car(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Заводим автомобиль {self.name}.')

    def stop(self):
        print(f'Остонавливааем автомобиль {self.name}.')

    def turn_left(self):
        print(f'Автомобиль {self.name} поворачивает на лево.')

    def turn_right(self):
        print(f'Автомобиль {self.name} поворачивает на право.')

    def show_speed(self, speed_car):
        self.speed_car = speed_car


class TownCar(Car):

    speed = 80
    color = 'Red'
    name = 'Lada'
    is_police = False

    def speeding(self):
        if self.speed_car >= 60:
            print(f'Автомобиль {self.name} превысил скорость на '
                  f'{self.speed_car - 60} км/ч.')


class SportCar(Car):

    speed = 90
    color = 'Green'
    name = 'Toyota Camry'
    is_police = False


class WorkCar(Car):

    speed = 100
    color = 'Blue'
    name = 'Mercedes-Benz'
    is_police = False

    def speeding(self):
        if self.speed_car >= 40:
            print(f'Автомобиль {self.name} превысил скорость на '
                  f'{self.speed_car - 40} км/ч.')


class PoliceCar(Car):

    speed = 120
    color = 'Black and white'
    name = 'Lexus RX 350'
    is_police = True


speed_trap = TownCar()
speed_trap.characteristics_Car(60, 'Red', 'Lada', False)
speed_trap.show_speed(random.randint(10, 120))
speed_trap.speeding()
speed_trap.stop()

speed_trap = WorkCar()
speed_trap.characteristics_Car(100, 'Blue', 'Mercedes-Benz', False)
speed_trap.show_speed(random.randint(10, 120))
speed_trap.speeding()
