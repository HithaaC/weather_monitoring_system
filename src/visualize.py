# src/visualize.py
import sqlite3
import matplotlib.pyplot as plt

def plot_weather_summary():
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT date, AVG(temperature) AS avg_temp
        FROM weather
        GROUP BY date
    ''')
    data = cursor.fetchall()
    conn.close()

    dates = [row[0] for row in data]
    avg_temps = [row[1] for row in data]

    plt.plot(dates, avg_temps, marker='o')
    plt.title('Daily Average Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
