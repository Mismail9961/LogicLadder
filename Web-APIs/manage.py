import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)       # HTTP response code
print(response.json())            # Parse JSON response


if response.status_code == 200:
    data = response.json()
    print(data['key'])
else:
    print("Failed to fetch data.")


json_data = {
    "main": {"temp": 298.15},
    "weather": [{"description": "clear sky"}]
}


print(json_data["main"]["temp"])                # Access nested value
print(json_data["weather"][0]["description"])   # Access from list


import requests
import urllib.parse

API_KEY = 'de493c9d50ef084aa29d95783df647be'
city = input("Enter City Name : ")

# Encode city name (for spaces like "New York")
city_encoded = urllib.parse.quote_plus(city)

# Build the request URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={API_KEY}&units=metric"

# Send the request
response = requests.get(url)

# Debug output
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"✅ Weather in {city}: {description}, {temp}°C")
else:
    print("❌ City not found or error occurred.")
    print("Response:", response.text)  # Shows detailed error message
