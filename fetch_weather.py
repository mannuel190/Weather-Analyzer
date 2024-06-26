import json
import requests
import pandas as pd
from datetime import datetime, timedelta


with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Your Meteomatics API credentials
USERNAME = 'setu_aadegbola_emmanuel'
PASSWORD = '10nf4Sq0LY'

# The location for which you want to fetch weather data (latitude,longitude)
LOCATION = '53.03,7.3'

# Define the start and end dates for the weather data request
START_DATE = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
END_DATE = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%dT%H:%M:%SZ')

# The interval between data points (in this case, every 3 hours)
INTERVAL = 'PT1H'

# Construct the API request URL using the defined parameters
URL = f'https://api.meteomatics.com/{START_DATE}--{END_DATE}:{INTERVAL}/t_2m:C,relative_humidity_2m:p/{LOCATION}/json'

def fetch_weather_data():

    # Fetches weather data from the Meteomatics API and returns it as a pandas DataFrame.
    
    # Make the GET request to the Meteomatics API
    response = requests.get(URL, auth=(USERNAME, PASSWORD))
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)


    # Parse the JSON response from the API
    data = response.json()
    
    # Extract the weather data from the JSON response
    weather_data = data['data']
    
    # Extract time series and humidity series from the weather data
    time_series = weather_data[0]['coordinates'][0]['dates']
    humidity_series = weather_data[1]['coordinates'][0]['dates']
    
    # Create a list to hold the formatted weather data
    weather_list = []
    
    # Loop through the time series and humidity series to populate the weather list
    for temp, humidity in zip(time_series, humidity_series):
        weather_list.append({
            'datetime': temp['date'],        # Date and time of the weather data point
            'temperature': temp['value'],    # Temperature value in Celsius
            'humidity': humidity['value']    # Humidity value in percentage
        })
    
    # Convert the weather list to a pandas DataFrame
    return pd.DataFrame(weather_list)

if __name__ == "__main__":
    # Fetch the weather data
    df = fetch_weather_data()

    if df is not None:
        # Save the weather data to a CSV file
        df.to_csv('weather_data.csv', index=False)
        
        # Print a confirmation message
        print("Weather data fetched and saved to weather_data.csv")
    else:
        print("Failed to fetch weather data")