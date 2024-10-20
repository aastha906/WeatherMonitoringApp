import json
import os
from datetime import datetime
import pandas as pd

DATA_FILE = 'data/summaries.json'


def initialize_data_file():
    """Initialize the data file if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)


def process_weather_data(weather_data):
    """Process and store weather data."""
    initialize_data_file()

    # Extract relevant information
    city = weather_data['name']
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    weather_condition = weather_data['weather'][0]['main']
    timestamp = weather_data['dt']
    date = datetime.fromtimestamp(timestamp).date()

    # Load existing summaries
    with open(DATA_FILE, 'r') as f:
        summaries = json.load(f)

    # If the city entry does not exist, initialize it
    if city not in summaries:
        summaries[city] = {}

    # Initialize the day's summary if it does not exist
    if str(date) not in summaries[city]:
        summaries[city][str(date)] = {
            'temperatures': [],
            'weather_conditions': []
        }

    # Append the new data
    summaries[city][str(date)]['temperatures'].append(temp)
    summaries[city][str(date)]['weather_conditions'].append(weather_condition)

    # Calculate daily aggregates
    daily_summary = summaries[city][str(date)]
    avg_temp = sum(daily_summary['temperatures']) / len(daily_summary['temperatures'])
    max_temp = max(daily_summary['temperatures'])
    min_temp = min(daily_summary['temperatures'])
    dominant_condition = max(set(daily_summary['weather_conditions']), key=daily_summary['weather_conditions'].count)

    # Update the summary with aggregates
    summaries[city][str(date)]['summary'] = {
        'average_temperature': avg_temp,
        'maximum_temperature': max_temp,
        'minimum_temperature': min_temp,
        'dominant_condition': dominant_condition
    }

    # Save back to the file
    with open(DATA_FILE, 'w') as f:
        json.dump(summaries, f)

    print(f"Processed data for {city} on {date}: {summaries[city][str(date)]['summary']}")
