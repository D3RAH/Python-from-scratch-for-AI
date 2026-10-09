import requests 

response = requests.get('https://github.com')
print(response.status_code)


numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

if 2 in numbers or 3 in numbers:
    print("2 or 3 are in the list")
else:
    print("2 and 3 are not in the list")
    
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person.get("job"))

# ----------------------------Nested Dictionaries -----------------------------------

people = {
    "person1": {"name": "Alice", "age": 30, "city": "New York"},
    "person2": {"name": "Bob", "age": 25, "city": "Los Angeles"},
    "person3": {"name": "Charlie", "age": 35, "city": "Chicago"}
}

people["person2"]["age"] = 26

print(people)

scores = dict(math=95, english=87, science=92)

print(scores)

people["person3"]["name"]

people.get("person3").get("name")




# ----------------------------working with lists-----------------------------------

nested_list = [
    ["Apple", "Banana"],
    ["Carrot", "Potato"],
    ["Hawk", "Eagle"]
]

learning = nested_list[0][0:]

print(learning)

if "Apple" in nested_list[0] and "Carrot" in nested_list[1]:
    print("Apple and Carrot are in the nested list")
else:
    print("Apple and Carrot are not in the nested list")
    

new = [sorted(newlist) for newlist in nested_list]

print(new)


# ----------------------------working with Tuples----------------------------------

# tuple unpacking 
point =(3,5)
print(id(point))
x, y = point

z = y
y = x
x = z

point = (x, y)
print(id(point))


# ----------------------------working with Sets---------------------------------
fruits = set(["apple", "banana","apple",  "orange"])
print(fruits)

colors = {"red", "blue"}

colors.add("pink")
colors.remove("blue")
colors.discard("magenta")  # use .discard to avoid if item not found in the set/ list 

# ----------------------------working with Sets---------------------------------


counter = 0 

def increment():
    counter = 2
    counter += 1
    return counter

increment()


def greet(name):
    message = "hello there, "
    return message + name
    
greet("dera")

def add_item(item, list=None):
    if list is None:
        list = []
    list.append(item)
    return list

add_item("beans", "rice")


def add_print(a, b):
    print(a + b)
    
add_print(5, 3)

def add_return(a, b):
    add_print(2,2)
    return a * b

add_return(7,3)


def get_min_max(numbers):
    return min(numbers), max(numbers)

get_min_max([2,4,5,8,7,9,0])

import requests 
import pandas as pd


response = requests.get("https://pokeapi.co")

data = response.json()

print(data)

import pandas as pd

data = {
    "name": ["alice", "bob", "charlie"],
    "age": [26, 18, 90],
    "city": ['NYC', 'LA', "CHICAGO"]
}

df = pd.DataFrame(data)

print(df)


# ----------------------------API calling---------------------------------
import json

latitude = 48.85
longitude = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)
print(json.dumps(data, indent=2))

temperature = data["current"]["temperature_2m"]

print(temperature)


# ----------------------------working with data---------------------------------
from datetime import datetime, timedelta

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url2 = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response2 = requests.get(url2)
data2 = response2.json()

print(json.dumps(data2, indent=4))

# Loading Data into Pandas

# Getting the daily Data from the json
daily_data = data["daily"]

# creating a dataframe
df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temperature": daily_data["temperature_2m_max"],
    "min_temperature": daily_data["temperature_2m_min"]
})
df['date'] = pd.to_datetime(df['date'])
print(df)

# Create a simple line chart using matplotlip to visualize the data

import matplotlib.pyplot as plt


# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temperature'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temperature'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('weather_chart.png')
plt.show()


# saving the data as csv file for later use.
import os

path = os.getcwd()


# create path if it doesnt exist 
if not os.path.exists("data"):
    os.makedirs("data")
    
# save to CSV 
csv_file = df.to_csv("data/paris_weather.csv", index=False)

file_path = "data/paris_weather.csv"

if os.path.exists(file_path):
    print(f"file saved.... check {file_path} dir")
else:
    print(f"file not saved to {file_path}")
    

