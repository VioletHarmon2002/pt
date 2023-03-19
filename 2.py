# Conversion factors
TALENT_TO_POUND = 20
POUND_TO_LOT = 32
LOT_TO_GRAM = 13.3

# Ask the user to enter a mass in medieval units
talents = float(input("Enter mass in talents: "))
pounds = float(input("Enter mass in pounds: "))
lots = float(input("Enter mass in lots: "))

# Convert the mass to kilograms and grams
total_lots = talents * TALENT_TO_POUND * POUND_TO_LOT + pounds * POUND_TO_LOT + lots
total_grams = total_lots * LOT_TO_GRAM
total_kilos = total_grams // 1000
remainder_grams = total_grams % 1000

# Print the result
print("The mass is equivalent to {:.0f} kg and {:.1f} g.".format(total_kilos, remainder_grams))
