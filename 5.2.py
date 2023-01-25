from audioop import reverse


numbers = []

number = int(input("Enter number: "))
while True:
    if(number != ""):
        numbers.append(int(number))
        number = input("Enter number: ")
    elif(number == ""):
        break

numbers.sort()
numbers.reverse()
print("five greatest numbers ",numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])