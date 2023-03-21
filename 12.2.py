import requests


municipality = input("Enter a municipality name: ")


api_key = "YOUR_API_KEY_HERE"
url = f"https://api.openweathermap.org/data/2.5/weather?q=%7Bmunicipality%7D&appid=%7Bapi_key%7D"
response = requests.get(url)


data = response.json()
kelvin_temp = data["main"]["temp"]
celsius_temp = kelvin_temp - 273.15
description = data["weather"][0]["description"]


print(f"The weather in {municipality} is currently {description} with a temperature of {celsius_temp:.1f}°C.")
﻿
