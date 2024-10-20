import time
import json
import requests
from data_processing import process_weather_data
import schedule

API_KEY = 'ac60c00a0727add05a44fd98a211b00e'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data(city):
    """Fetch weather data for a specified city from OpenWeatherMap."""
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}")
        return None

def job():
    """Scheduled job to fetch weather data and process it."""
    for city in CITIES:
        weather_data = fetch_weather_data(city)
        if weather_data:
            process_weather_data(weather_data)

# Manually call the job once at startup for debugging
job()

# Schedule the job every 5 minutes
schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    print("Starting weather monitoring system...")
    while True:
        schedule.run_pending()
        time.sleep(1)
