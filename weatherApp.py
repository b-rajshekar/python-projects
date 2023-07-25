import requests
import json
import pyttsx3


def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=036beaa8954b4d2196d04644232507&q={city}"

r = requests.get(url)
weatherDIC = json.loads(r.text)
ltimeDIC = json.loads(r.text)

w = weatherDIC["current"]["temp_c"]
lt = ltimeDIC["location"]["localtime"]

speak(f" 'The current weather in {city} is {w} degrees as of {lt}'")
