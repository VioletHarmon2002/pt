days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number] #индексирование #day = days_of_the_week[day_number] calculates
# the index in the days_of_the_week tuple based on the day_number
print(f"Day number {day_number} is {day}.")