class Car:

    def __init__(self, speed=0):
        self.name = "Car"
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def _top_speed(self, increment: int):
        # Check top speed
        top_speed = 1000
        if self.speed + increment >= top_speed:
            self.speed = top_speed
            print("I am reaching top speeds!")
            return True     # we are at top speed(yes)
        else:
            return False     # we are not reaching top speed(no)

    def _stopped(self, decrement: int):
        stopped = 0
        if self.speed - decrement <= stopped:
            self.speed = stopped
            print("I have been fully stopped!")
            return True  # we are stopping(yes)
        else:
            return False  # we are not stopping(no)

    def accelerate(self):
        increment = 5
        if not self._top_speed(increment):
            self.speed += increment

    def brake(self):
        decrement = 5
        if not self._stopped(decrement):
            self.speed -= decrement

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            format_float = f"{self.odometer / self.time:.2f}"
            return format_float
        else:
            pass


class Mini (Car):
    """
    Inheritance and override
    """
    def __init__(self, speed=0):
        super().__init__(speed)
        self.name = "Mini"

    def accelerate(self):
        increment = 7
        if not self._top_speed(increment):
            self.speed += increment


class Tesla(Car):
    """
    Inheritance and override
    """
    def __init__(self, speed=0):
        super().__init__(speed)
        self.name = "Tesla"

    def accelerate(self):
        increment = 10
        if not self._top_speed(increment):
            self.speed += increment

    def rocket_accelerate(self):
        increment = 111
        if not self._top_speed(increment):
            self.speed += increment

    def fast_brake(self):
        decrement = 111
        if not self._stopped(decrement):
            self.speed -= decrement


class BMW(Car):
    """
    Inheritance and override
    """

    def __init__(self, speed=0):
        super().__init__(speed)
        self.name = "BMW"

    def accelerate(self):
        increment = 8
        if not self._top_speed(increment):
            self.speed += increment


if __name__ == '__main__':

    cars = "Which car would you like? A [N]ormal car, a [M]ini, a [B]MW or a [T]esla?"
    car_options = "BNMT"
    car_input = ""

    while car_input not in car_options or len(car_input) != 1:
        car_input = input(cars).upper()

    if car_input == "N":
        my_car = Car()
    elif car_input == "M":
        my_car = Mini()
    elif car_input == "T":
        my_car = Tesla()
    elif car_input == "B":
        my_car = BMW()

    print(f"I am a {my_car.name}!")

    actions = "ABRFOS" if isinstance(my_car, Tesla) else "ABOS"
    tesla_action = "[R]ocket Accelerate, [F]ast Brake,"
    action_inputs = f"What should I do? [A]ccelerate, [B]rake, {tesla_action if isinstance(my_car, Tesla) else ''} " \
                    f"show [O]dometer, or show average [S]peed?"
    while True:
        action = input(action_inputs).upper()
        if action not in actions or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        elif action == 'R':
            my_car.rocket_accelerate()
        elif action == 'F':
            my_car.fast_brake()
        my_car.step()
        my_car.say_state()
