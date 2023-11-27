#Write a program that asks for the biological gender and hemoglobin value (g/l). T
# the program the notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("Write a biological gender: ")
hemoglobin_value = int(input("Write a hemoglobin value (g/l): "))
if gender == "Female":
 if 117 <= hemoglobin_value <= 155:
    print("Your hemoglobin level is normal.")
elif hemoglobin_value < 117:
    print("Your hemoglobin level is low.")
elif hemoglobin_value > 155:
    print("Your hemoglobin level is high")

if gender == "Male":
    hemoglobin_value2 = int(input("Write a hemoglobin value (g/l): "))
    if hemoglobin_value2 > 167:
        print("Your level is high")
    elif hemoglobin_value2 < 134:
        print("Your level is low")
    elif  134 <= hemoglobin_value2 >= 167:
        print("Your level is normal")









