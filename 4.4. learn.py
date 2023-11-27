#Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number.
#After each guess the program prints out a text:
#Too high, Too low or Correct. Notice that the computer must not change the number between guesses.

import random

secret_number = random.randint(1, 10)
print("Welcome to our game")

attempts = 0  # Corrected the variable name

while True:
    
        guess = int(input("Write down the number: "))
        attempts += 1
        if guess == secret_number:
            print("Correct")
            break  # Exit the loop when the guess is correct
        elif guess > secret_number:
            print("Too high")
        else:
            print("Too low")














