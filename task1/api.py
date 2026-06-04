#Q7
import requests

url = "https://jsonplaceholder.typicode.com/posts?userId=3"

try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    data = res.json()

    for post in data:
        print(post["title"].upper())

    print(f"Total posts: {len(data)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")

#Q8
import requests

city = "Chandigarh"
lat = 30.6970
lon = 76.7491

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

weather_map = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    61: "Light rain",
    80: "Rain showers",
    95: "Thunderstorm"
}

try:
    res = requests.get(url, timeout=5)
    res.raise_for_status()
    data = res.json()["current_weather"]

    temp = data["temperature"]
    code = data["weathercode"]
    condition = weather_map.get(code, "Unknown")

    print(f"City       : {city}")
    print(f"Temperature: {temp}°C")
    print(f"Condition  : {condition}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")