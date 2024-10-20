import unittest
from data_processing import process_weather_data


class TestWeatherDataProcessing(unittest.TestCase):
    
    def test_process_weather_data(self):
        # Sample weather data for testing
        weather_data = {
            'name': 'Delhi',
            'main': {'temp': 30, 'feels_like': 32},
            'weather': [{'main': 'Clear'}],
            'dt': 1634764800  # Sample timestamp
        }
        
        process_weather_data(weather_data)

        # Check if the summary was created correctly (load the data file to verify)
        with open('data/summaries.json', 'r') as f:
            summaries = json.load(f)

        self.assertIn('Delhi', summaries)
        self.assertIn('2021-10-20', summaries['Delhi'])  # Check for date entry


if __name__ == '__main__':
    unittest.main()
