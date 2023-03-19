classCar:
def init(self, registration_number, max_speed):
self.registration_number = registration_number
self.max_speed = max_speed
self.current_speed = 0
self.distance_traveled = 0


new_car = Car("ABC-123", 142)


print("Registration number: ", new_car.registration_number)
print("Maximum speed: ", new_car.max_speed, "km/h")
print("Current speed: ", new_car.current_speed, "km/h")
print("Distance traveled: ", new_car.distance_traveled, "km")