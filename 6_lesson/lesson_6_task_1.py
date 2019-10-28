class TrafficLight:

    from threading import Timer
    from time import sleep

    def hello():
        print("Hello user!")

    def bye():
        sleep(10)
        print("Bye...bye...")

    while 1:
        timer = Timer(2, hello)
        timer.start()
        bye()

work_TrafficLight = TrafficLight()
work_TrafficLight.running()

