import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import json

API_KEY = '4b5d8970563fd331b855a8219beb9f42'  # Replace with your OpenWeatherMap API key

def get_weather_data(location):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather():
    location = location_entry.get()
    if location:
        data = get_weather_data(location)
        if data['cod'] == 200:
            city = data['name']
            country = data['sys']['country']
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            icon = data['weather'][0]['icon']
            weather_label.config(text=f"{city}, {country}\nTemperature: {temp}°C\nWeather: {weather.capitalize()}\nWind Speed: {wind_speed} m/s")
            load_icon(icon)
        else:
            messagebox.showerror("Error", "Location not found.")
    else:
        messagebox.showerror("Error", "Please enter a location.")

def load_icon(icon_code):
    """Load weather icon."""
    url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    icon_data = requests.get(url, stream=True).raw
    icon_image = tk.PhotoImage(data=icon_data)
    icon_label.config(image=icon_image)
    icon_label.image = icon_image

# Create the main application window
app = tk.Tk()
app.title("Weather App")
app.geometry("400x400")

# Create and place widgets
location_label = tk.Label(app, text="Enter Location:")
location_label.pack(pady=5)
location_entry = tk.Entry(app)
location_entry.pack(pady=5)

search_button = tk.Button(app, text="Get Weather", command=display_weather)
search_button.pack(pady=10)

weather_label = tk.Label(app, text="", font=("Helvetica", 14))
weather_label.pack(pady=20)

icon_label = tk.Label(app)
icon_label.pack(pady=5)

# Run the main application loop
app.mainloop()
