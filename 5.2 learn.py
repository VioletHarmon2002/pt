#Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.




numbers = []
number = input("Write down a number (or an empty string to quit): ")

while number != "":
    number = int(number)
    numbers.append(number)
    number = input("Write down the next number (or an empty string to quit):")

numbers.sort()
print(numbers)



