import requests, json
from tellcommand import take_command, talk

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


def weather():
    talk("hello sir, please tell the city for weather")
    CITY = take_command()
    API_KEY = '6f8be79031ae9a3c8d10299e4970dcd4'

    URL = BASE_URL + "q=" + CITY + "&units=metric" + "&appid=" + API_KEY

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature} ")
        talk(f"Temperature: {temperature} degree Celcius" )
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the HTTP request")
        talk("Error in the HTTP request")


