import requests


response = requests.get("https://api.chucknorris.io/jokes/random%22)


data = response.json()

joke_text = data["value"]


print(joke_text)
random")