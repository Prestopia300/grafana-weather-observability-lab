from prometheus_client import start_http_server, Gauge
import requests
import time
import os

# Load API key and city from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Seattle,US")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Define Prometheus metrics
temperature_gauge = Gauge("weather_temperature_celsius", "Current temperature in Celsius")
humidity_gauge = Gauge("weather_humidity_percent", "Current humidity in %")
wind_speed_gauge = Gauge("weather_wind_speed_mps", "Current wind speed in meters/sec")

def fetch_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        temperature_gauge.set(temperature)
        humidity_gauge.set(humidity)
        wind_speed_gauge.set(wind_speed)

        print(f"Updated: {temperature}°C, {humidity}%, {wind_speed}m/s")
    except Exception as e:
        print(f"Error fetching weather: {e}")

if __name__ == "__main__":
    start_http_server(8000)  # metrics available at http://localhost:8000/metrics
    while True:
        fetch_weather()
        time.sleep(300)  # update every 5 minutes
