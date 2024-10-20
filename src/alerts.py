def check_alerts(current_temp, threshold):
    """Check if current temperature exceeds the specified threshold."""
    if current_temp > threshold:
        print(f"Alert! Current temperature is {current_temp}°C, which exceeds the threshold of {threshold}°C.")
