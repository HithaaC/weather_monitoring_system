# Real-Time Weather Monitoring System

## Overview

The Real-Time Weather Monitoring System is a Python-based application designed to continuously monitor weather conditions for major cities in India. It fetches real-time weather data from the OpenWeatherMap API, processes the data to calculate daily aggregates, and provides alerting functionality for temperature thresholds. The system also includes visualization of weather summaries and alerts.

## Features

- Fetches weather data for cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- Processes and stores weather data in a SQLite database.
- Calculates daily weather summaries, including:
  - Average temperature
  - Maximum temperature
  - Minimum temperature
  - Dominant weather condition
- Sends alerts when temperature exceeds user-defined thresholds.
- Visualizes daily weather summaries and historical trends.

## Prerequisites

- Python 3.x
- SQLite
- Required Python packages:
  - `requests`
  - `matplotlib`
  - `sqlite3` (included with Python)

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone (https://github.com/HithaaC/weather_monitoring_system.git)
   cd weather_monitoring_system

## Instal required packages
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install requests matplotlib

## Obtain OpenWeatherMap API Key:

Sign up at OpenWeatherMap to get a free API key.

## Configure API Key:

Update the API key in the config.py file:

OPENWEATHER_API_KEY = 'your_api_key_here'

## Create SQLite Database:

Open the command prompt or terminal and navigate to the data directory:

cd data
sqlite3 weather_data.db

## Run the following SQL command to create the necessary table:

CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    timestamp INTEGER,
    temperature REAL,
    feels_like REAL,
    main_weather TEXT
);

## Run the Application:

From the project root directory, run:

python src/main.py

## Usage
The application will start retrieving weather data at configurable intervals (e.g., every 5 minutes).

Alerts will be triggered and displayed in the console when temperature thresholds are exceeded.

## Visualizations of daily summaries can be accessed by running:
python src/visualize.py

## Test Cases
The application includes test cases to verify the functionality, such as:
System setup and API connectivity
Data retrieval and parsing
Temperature conversion
Daily weather summary calculation
Alerting thresholds

## Bonus Features
Extend the system to include additional weather parameters (e.g., humidity, wind speed).
Implement weather forecasts retrieval and generate summaries based on predicted conditions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
OpenWeatherMap API
SQLite
DB Browser for SQLite
