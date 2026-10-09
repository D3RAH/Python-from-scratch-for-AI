import requests
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import json
import os


today = datetime.now()
week_ago = today - timedelta(days=7)

start_date =  week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
print(end_date)
print(start_date)

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)

data = response.json()
print(json.dumps(data, indent=4))


daily_data = data["daily"]

df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"]
})

# converting the data string to Datetime
df["date"] = pd.to_datetime(df["date"])

print(df)

#-------------------------------Matplotlib----------------------------

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('data/weather_chart.png')
plt.show()

df.to_csv("data/paris_weather.csv", index=False)
