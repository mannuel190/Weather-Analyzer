import pandas as pd
import os
import matplotlib.pyplot as plt

def analyze_weather_data():
    """
    Reads the weather data from a CSV file and generates two plots:
    1. Temperature over time
    2. Humidity over time
    The plots are saved as PNG files and displayed.
    """
    # Read the weather data from the CSV file
    df = pd.read_csv('weather_data.csv')
    
    # Convert the 'datetime' column to datetime objects
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Plot Temperature over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['datetime'], df['temperature'], marker='o')
    plt.title('Temperature Over Time')
    plt.xlabel('Datetime')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
    plt.tight_layout()  # Adjust the padding between and around subplots
    plt.savefig('temperature_over_time.png')  # Save the plot as a PNG file
    plt.show()  # Display the plot

    # Plot Humidity over Time
    plt.figure(figsize=(10, 5))
    plt.plot(df['datetime'], df['humidity'], marker='o', color='orange')
    plt.title('Humidity Over Time')
    plt.xlabel('Datetime')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability
    plt.tight_layout()  # Adjust the padding between and around subplots
    plt.savefig('humidity_over_time.png')  # Save the plot as a PNG file
    plt.show()  # Display the plot

if __name__ == "__main__":
    # If the script is executed directly, run the analyzer function
    analyze_weather_data()
