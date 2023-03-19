import random

cool car:
initialization of def(self, name, speed):
self.name = name
self.speed = speed
proper distance = 0

drive def (self):
proper distance += proper speed

class race:
initialization of the definition (self, name, distance, cars):
self.name = name
self.distance = distance
self.cars = cars

def hour_passes(self):
for a car in self.cars:
car.speed += random.randint(-5, 5)
car.drive()

def print_status(self):
print(f"{'Name':<10}{'Speed':<10}{'Distance':<10}")
for a car in self.cars:
print(f"{car.name :<10}{car.speed:<10}{car.distance:<10}")

def race_finished(self):
for a car in self.cars:
if car.distance >= self.distance:
return the True value
returns the value False

# Creating cars
car1 = Car ("Car 1", 100)
car2 = Car("Car 2", 120)
car3 = Car ("Car 3", 110)
car4 = Car("Car 4", 105)
car5 = Car ("Car 5", 90)
car6 = Car("Car 6", 95)
car7 = Car("Car 7", 115)
car8 = Car ("Car 8", 130)
car9 = Car ("Car 9", 125)
car10 = Car("Car 10", 135)


race = Race("Grand Demolition Derby", 8000, [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10])


clock = 0
until the race.race_finished():
if the clock is %10 == 0:
print(f"\Current status after {hours} hours:")
race.print_status()
race.pass_hour()
hours += 1