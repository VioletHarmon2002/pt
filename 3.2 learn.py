#Write a program that asks the user to enter the cabin class of a cruise ship
# and then prints out a written description
# according to the list below. You must use an if/elif/else structure in your solution.

#LUX: upper-deck cabin with a balcony.
#A: above the car deck, equipped with a window.
#B: windowless cabin above the car deck.
#C: windowless cabin below the car deck.

luokka = str(input("Valitse laivan hyttiluokka (LUX, A, B, C): "))
if luokka == "LUX":
   print("upper-deck cabin with a balcony.")
elif luokka == "A":
   print("above the car deck, equipped with a window.")
else:
    print("another room.")











