# src/main.py
import time
import schedule
from weather import fetch_weather_data, save_weather_data, get_daily_summary
from visualize import plot_weather_summary

def job():
    for city in ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]:
        weather_data = fetch_weather_data(city)
        if weather_data:
            save_weather_data(weather_data)

def run_visualization():
    plot_weather_summary()

if __name__ == "__main__":
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
        run_visualization()
