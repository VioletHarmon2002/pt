#Write a Car class that has the following properties: registration number, maximum speed,
# current speed and travelled distance. Add a class initializer that sets the first two
# of the properties based on parameter values. The current speed and travelled distance
# of a new car must be automatically set to zero. Write a main program where you create
# a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out
# all the properties of the new car.

#Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed
# . The method must change the value of the speed property of the object. The speed of the car must stay
# below the set maximum and cannot be less than zero. Extend the main program
# so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake
# by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = new_speed

# Create a Car object
carA = Car("ABC-123", 142)

# Print initial details
print(f"Registration Number: {carA.registration_number}")
print(f"Maximum Speed: {carA.maximum_speed} km/h")
print(f"Current Speed: {carA.current_speed} km/h")
print(f"Travelled Distance: {carA.travelled_distance} km")

# Accelerate the car
carA.accelerate(30)
carA.accelerate(70)
carA.accelerate(50)

# Print the current speed after acceleration
print(f"Car speed after acceleration: {carA.current_speed} km/h")

# Emergency brake
carA.accelerate(-200)

# Print the current speed after emergency brake
print(f"Car speed after emergency brake: {carA.current_speed} km/h.")
