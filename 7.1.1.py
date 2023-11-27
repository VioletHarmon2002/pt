#Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

def seasons(type_of_season):
 type_of_season = ("Spring", "Summer", "Autumn", "Winter")
 return type_of_season

months = int(input("Enter the month of a year: "))
if months == "June" or months == "July" or months == "August":
 print(seasons[1])
elif months == "September" or months == "October" or months == "November":
 print(seasons[2])
elif months == "March" or months == "April" or months == "May":
 print(seasons[0])
else:
 print(seasons[3])

result = seasons(months)
print(result)


def get_season(month):
 seasons = ("Winter", "Spring", "Summer", "Autumn")
 if month in ["June", "July", "August"]:
  return seasons[2]     . #, значение, которое будет возвращено из функции это элемент списка seasons с индексом 2.
 elif month in ["September", "October", "November"]:
  return seasons[3]
 elif month in ["March", "April", "May"]:
  return seasons[1]
 else:
  return seasons[0]

#конец функции
month = input("Enter the name of a month: ")
result = get_season(month)
print(f"The season corresponding to {month} is {result}.")








