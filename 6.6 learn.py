#Write a function that receives two parameters: the diameter of a round pizza in centimeters
# and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
import math
def pizza(diameter_cm, price_euros):
    diameter_m = diameter_cm / 100
    area_m2 = math.pi * (diameter_m / 2) ** 2
    unit_price = price_euros / area_m2
    return unit_price
diameter_1pizza = int(input(f"Enter the diameter of first pizza in cm: "))
price_1pizza = int(input("Enter the price of first pizza in euros: "))
diameter_2pizza = int(input("Enter the diameter of second pizza in cm: "))
price_2pizza = int(input("Enter the price of second pizza in euros: "))

unit_price_1 = pizza(diameter_1pizza, price_1pizza)
unit_price_2 = pizza(diameter_2pizza, price_2pizza)

print(f"Unit price for the first pizza: {unit_price_1:.2f} euros/m²")
print(f"Unit price for the second pizza: {unit_price_2:.2f} euros/m²")

if unit_price_1 < unit_price_2:
    print("The first pizza provides better value for money.")
elif unit_price_2 < unit_price_1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas have the same unit price.")







