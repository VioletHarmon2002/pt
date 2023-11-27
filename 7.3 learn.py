#Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)


options = "A new airport", "Information", "Quit"
option = input("Enter the option (A new airport, Information or Quit): ")
ICAO = {"EFHK": "Helsinki-Vantaa"}

while True:
    if options[0]:
        ICAO_code = input("Enter the ICAO code: ")
        name_airport = input("Enter the name of airport: ")
        ICAO[ICAO_code] = name_airport
        print("Airport data added.")
    elif options[1]:
        ICAO_code = input("Enter the ICAO code: ")
        if ICAO_code in ICAO:
            print(f"The name of the airport with ICAO code {ICAO_code} is {ICAO[ICAO_code]}.")
        else:
            print(f"Airport with ICAO code {ICAO_code} not found in the database.")
    elif options[2]:
        print("Program execution stopped.")
        break

