class Car:
    def init(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed


new_car = Car("ABC-123", 142)


new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)

# печатаем текущую скорость автомобиля
print("Current speed: ", new_car.current_speed, "km/h")

# экстренное торможение, уменьшаем скорость на -200 км/ч
new_car.accelerate(-200)

# печатаем конечную скорость автомобиля
print("Current speed: ", new_car.current_speed, "km/h")
