#Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends

inches = int(input("Write the inches: "))
while inches >= 0:
    cm = inches * 2.54
    print(f"{inches} inches is {cm} centimetres ")
    inches = int(input("Enter the inches: "))
else:
    print("Execution stopped")





