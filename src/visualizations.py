import matplotlib.pyplot as plt
import pandas as pd
import json

DATA_FILE = 'data/summaries.json'


def plot_daily_summary(city):
    """Plot daily weather summary for a specified city."""
    with open(DATA_FILE, 'r') as f:
        summaries = json.load(f)

    if city in summaries:
        dates = []
        avg_temps = []
        max_temps = []
        min_temps = []

        for date, data in summaries[city].items():
            dates.append(date)
            avg_temps.append(data['summary']['average_temperature'])
            max_temps.append(data['summary']['maximum_temperature'])
            min_temps.append(data['summary']['minimum_temperature'])

        # Create a DataFrame for easy plotting
        df = pd.DataFrame({
            'Date': pd.to_datetime(dates),
            'Average Temperature': avg_temps,
            'Max Temperature': max_temps,
            'Min Temperature': min_temps
        })

        df.set_index('Date', inplace=True)
        df.plot(figsize=(10, 5))
        plt.title(f'Daily Weather Summary for {city}')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid()
        plt.show()
    else:
        print(f"No data available for {city}.")
