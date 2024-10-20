# Real-Time Weather Monitoring System with Rollups and Aggregates

## Objective

This project is a real-time data processing system for monitoring weather conditions in different cities across India. The system retrieves weather data from the OpenWeatherMap API and provides summarized insights using rollups and aggregates. It also includes features like alerting and data visualization.

## Features

- Fetch real-time weather data for multiple cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Process and aggregate daily weather summaries (average, max, min temperatures, and dominant weather conditions).
- Configurable temperature and condition thresholds to trigger alerts.
- Store weather data and summaries in JSON format for persistent storage.
- Visualization of weather summaries and trends (e.g., daily temperature changes).
  
## Technologies Used

- **Python 3.9+**
- **OpenWeatherMap API** for weather data.
- **Pandas** for data manipulation and analysis.
- **Matplotlib** for visualizations.
- **Schedule** for periodic data fetching.

## Prerequisites

- Python 3.9+ installed on your machine.
- OpenWeatherMap API Key (you can sign up for free at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up)).

## Project Structure

```
.
├── data
│   └── summaries.json       # File where daily summaries are stored
├── src
│   ├── main.py              # Entry point for the weather monitoring system
│   ├── data_processing.py   # Processes fetched weather data and aggregates summaries
│   ├── alerts.py            # Contains alerting logic for threshold violations
│   └── visualizations.py    # Functions to generate visualizations
├── README.md                # Project documentation
└── requirements.txt         # List of required Python packages
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/weather-monitoring-system.git
   cd weather-monitoring-system
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:

   Install all necessary packages listed in `requirements.txt` by running:

   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:
   - `requests`: For making API calls to OpenWeatherMap.
   - `pandas`: For data processing and aggregation.
   - `schedule`: For scheduling periodic API calls.
   - `matplotlib`: For generating visualizations.

4. **Get an OpenWeatherMap API Key**:

   - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and generate your API key.
   - Replace the placeholder in `main.py` with your actual API key:

     ```python
     API_KEY = 'your_actual_api_key'
     ```

## Usage

1. **Run the Application**:

   To start the weather monitoring system, run:

   ```bash
   python src/main.py
   ```

   The system will:
   - Fetch weather data for the predefined cities every 5 minutes.
   - Process and aggregate the data.
   - Store the daily summaries in the `data/summaries.json` file.
   - Output the current status in the console.

2. **Visualization**:

   After collecting some data, you can generate visualizations by running the following command:

   ```bash
   python src/visualizations.py
   ```

   This will generate a plot showing temperature trends and weather summaries.

3. **Alerts**:

   Alerts can be configured in `alerts.py` for certain weather conditions like temperatures exceeding thresholds (e.g., 35°C for two consecutive updates). Alerts will be printed in the console.

## Configuration

- You can modify the list of cities, alert thresholds, or API request intervals in the `main.py` file.
- The request interval (currently set to 5 minutes) can be changed by modifying the scheduling logic:

  ```python
  schedule.every(5).minutes.do(job)
  ```

## Testing

To test the core functionalities of the application, you can:
- Simulate weather API responses for test cases.
- Run the application and check whether the `data/summaries.json` file is populated correctly.
- Verify alerting thresholds and ensure alerts are triggered when conditions are met.
  
## Troubleshooting

### 1. **401 Unauthorized Error**:
   - Ensure the API key in `main.py` is valid.
   - Check that your OpenWeatherMap account is active and the API key is not expired.
   - If you still encounter issues, generate a new API key and retry.

### 2. **Missing Dependencies**:
   - Make sure to install the necessary dependencies using `pip install -r requirements.txt`.

### 3. **JSONDecodeError**:
   - If `summaries.json` is empty or corrupted, delete the file, and the program will recreate it.

## Future Enhancements

- Support for additional weather parameters (e.g., humidity, wind speed).
- Add forecast data processing.
- Advanced visualization features (e.g., interactive charts).
- Implement email or SMS alerts.

## License

This project is open-source and available under the MIT License. Feel free to use and modify the code as needed.

---

### Notes:
- Replace placeholders such as the GitHub repo URL and API key instructions with your actual details.
- Ensure that you’ve included `requirements.txt` in your repository for easy installation of dependencies.

Let me know if you'd like to customize any section!
