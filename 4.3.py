min_number = 0
max_number = 0
first_number = False

while True:
    try:
        number = input("Syöttäkää satunnainen numero: ")
        if number == "":
            break

        else:
            number = int(number)
            if first_number == False:
                min_number = number
                max_number = number
                first_number = True

            if max_number > number > min_number:
                pass

            elif number > max_number:
                max_number = number

            elif number < min_number:
                min_number = number

            continue

    except:
        print("Syötetty numero on virheellinen")
        continue

print(f"Pienin numero {min_number}")
print(f"Isoin numero {max_number}")