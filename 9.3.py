class Car:
def init(self, reg_number, max_speed):
self.reg_number = reg_number
self.max_speed = max_speed
self.speed = 0
self.distance = 0

def accelerate(self, speed_change):
self.speed += speed_change
if self.speed < 0:
self.speed = 0
elif self.speed > self.max_speed:
self.speed = self.max_speed

def drive(self, hours):
self.distance += self.speed * hours


car = Car("ABC-123", 142)


car.accelerate(30)


car.accelerate(70)


car.accelerate(50)


print("Current speed: {} km/h".format(car.speed))


car.accelerate(-200)


print("Final speed: {} km/h".format(car.speed))


car.drive(1.5)


print("Distance traveled: {} km".format(car.distance))