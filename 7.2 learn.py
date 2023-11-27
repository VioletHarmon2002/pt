#Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.



def season(month):
    seasons = ("Winter", "Spring", "Summer", "Fall")
    if month in ["June", "July", "August"]:
        return seasons[2]
    elif month in


