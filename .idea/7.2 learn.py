#Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending
# on whether the name was entered for the first time. Finally, the program lists out the input names one by one,
# one below another in any order. Use the set data structure to store the names.
names = set()
while True:
    name = (input("Enter the next name: "))
    names.add(name)
    if name == "":
        break

print(names)

names = set()
existing_names = set()

while True:
    name = input("Enter a name or an empty string to quit: ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

    existing_names.add(name)

print("\nList of names:")
for name in existing_names:
    print(name)
