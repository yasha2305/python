import requests

API_KEY = "YOUR_API_KEY"

# Get weather data
def get_weather(city):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        data = response.json()

        if data["cod"] != 200:
            print("City not found.")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        print("\n--- WEATHER REPORT ---")
        print(f"City        : {city}")
        print(f"Temperature : {temp}°C")
        print(f"Condition   : {weather}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind Speed  : {wind} m/s")

    except requests.exceptions.RequestException:
        print("Network error occurred.")

# Main
def main():
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Invalid city name.")

if __name__ == "__main__":
    main()