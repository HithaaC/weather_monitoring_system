# src/weather.py
import requests
import sqlite3
from datetime import datetime
import os

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def create_database():
    if not os.path.exists('data/weather_data.db'):
        conn = sqlite3.connect('data/weather_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                city TEXT,
                timestamp INTEGER,
                temperature REAL,
                feels_like REAL,
                main_weather TEXT
            )
        ''')
        conn.commit()
        conn.close()


def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'main_weather': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
    else:
        print(f"Failed to fetch weather data for {city}: {response.status_code}")
        return None

def save_weather_data(data):
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO weather (city, timestamp, temperature, feels_like, main_weather)
        VALUES (?, ?, ?, ?, ?)
    ''', (data['city'], data['timestamp'], data['temperature'], data['feels_like'], data['main_weather']))
    conn.commit()
    conn.close()

def get_daily_summary():
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT city, 
               DATE(timestamp, 'unixepoch') AS date,
               AVG(temperature) AS avg_temp,
               MAX(temperature) AS max_temp,
               MIN(temperature) AS min_temp,
               main_weather
        FROM weather
        GROUP BY city, date
    ''')
    summaries = cursor.fetchall()
    conn.close()
    return summaries

if __name__ == "__main__":
    create_database()
