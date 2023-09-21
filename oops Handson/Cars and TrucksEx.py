class Car:

    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    def start_engine(self):
        self.is_engine_started = True

    def stop_engine(self):
        self.is_engine_started = False

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
        else:
            print("start the engine to accelerate")

    def apply_brakes(self):
        if self.is_engine_started:
            self.current_speed = self.tyre_friction
        else:
            print("start the engine to apply brakes")

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("car has not yet started")


class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight = max_cargo_weight
        self.load = 0

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Truck has not started yet")

    def load_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("cannot load cargo during motion")
        elif cargo_weight > self.max_cargo_weight:
            print("cannot load cargo more than max limit:{}".format(self.max_cargo_weight))
        else:
            self.load += cargo_weight

    def unload_cargo(self, cargo_weight):
        if self.is_engine_started:
            print("cannot load during motion")
        elif cargo_weight > self.load:
            print("cannot unload more cargo than available")
        else:
            self.load -= cargo_weight


truck = Truck("red", 100, 5, 0.5, 1000)
truck.load_cargo(500)
print(truck.load)
truck.unload_cargo(200)
print(truck.load)
