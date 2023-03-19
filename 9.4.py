import random

cool car:
def init(self, reg_num, max_speed):
self.reg_num = reg_num
self.max_speed = maximum speed
proper speed = 0
proper distance = 0

def accelerates (independently):
self.speed += random.randint(-10, 15)
if own speed < 0:
own speed = 0
select self.speed > self.max_speed:
self.speed = self.max_speed

drive def (self):
proper distance += proper speed

def str(self):
return f"{self.reg_num}\t{self.max_speed} km/h\t{self.speed} km/h\t{self.distance} km"

# Create a list of 10 car objects with random maximum speeds and registration numbers
cars = []
for i in the range(1, 11):
reg_num = f"ABC-{i}"
max_speed = random.randint(100, 200)
car = Car(reg_num, max_speed)
cars.add(car)

# Simulate the winner of a car race
=
No, while the winner is None:
for a car in cars:
car.acceleration()
car.drive()
if the car.distance >= 10000:
winner = car
break

# Print out the characteristics of each car in a clear tabular format
print("Registration number\tMax Speed\tSpeed\tDistance")
for the car in cars:
printing(car)