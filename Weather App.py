import requests

API_KEY = "your_api_key_here"  # Get from https://openweathermap.org/api

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data.get("main"):
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        print(f"{city} Temperature: {temp}°C")
        print(f"Weather: {desc}")
    else:
        print("City not found!")

city = input("Enter city: ")
get_weather(city)
