#Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
#Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
import random

def roll_dice():
    return random.randint(1, 6)

while True:
    result = roll_dice()
    print("Dice roll result:", result)
    if result == 6:
        break


