'''

Get Weather with API (openweather)

'''


import requests

API_KEY = '401aaae2226ae6db02ef3371bb9ff658'

def weather(key):
    city = input("Enter a city: ")
    base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"
    weather_data = requests.get(base_url).json()

    city = weather_data['name']
    weather = weather_data['weather'][0]['main']
    temp = weather_data['main']['temp'] - 273.15

    return f"\n\nCity: {city}\nWeather: {weather}\nTemperature: {temp:0.2f}\n\n"

print(weather(API_KEY))