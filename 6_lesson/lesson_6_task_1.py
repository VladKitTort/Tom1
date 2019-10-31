from time import *

class TrafficLight:

    __color = ['Зеленый', 'Желтый', 'Красный']
    stage = 1

    def running(self):
        i = 0
        while True:
            if TrafficLight.stage == 1:
                if i == 3: i = 0
                print('Свктафор мигает')
                TrafficLight.stage = 2
                sleep(2)
            else:
                print(TrafficLight.__color[i])
                TrafficLight.stage = 1
                i += 1
                sleep(7)

work_TrafficLight = TrafficLight()
work_TrafficLight.running()

