import streamlit as st
import requests
import random

# Function to get weather data using OpenWeatherMap API
def get_weather(city="Pune", api_key="fdcc5b2fb232a3c729a38473e0970c97"):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        r = requests.get(url).json()
        temp = r["main"]["temp"]
        humidity = r["main"]["humidity"]
        return temp, humidity
    except:
        return None, None

# Title
st.title("Smart Irrigation System for Tomato Crop")
st.subheader("Real-time soil moisture, temperature, and humidity monitoring")

# Simulate soil moisture value (0-1023)
soil_moisture = st.slider("Soil Moisture (simulate)", 0, 1023, 500)

# Get weather data
temp, humidity = get_weather()

if temp is None or humidity is None:
    st.warning("Could not fetch live weather data. Using sample values.")
    temp, humidity = 28, 60  # fallback values

# Define thresholds for tomato crop
soil_threshold = 450  # moisture threshold for tomato (0-1023 scale)
temp_range = (18, 30)  # ideal temperature in °C
humidity_range = (50, 80)  # ideal humidity in %

# Display readings
st.write(f"**Soil Moisture:** {soil_moisture}")
st.write(f"**Temperature:** {temp} °C")
st.write(f"**Humidity:** {humidity} %")

# Irrigation decision logic
if soil_moisture < soil_threshold:
    irrigation = True
elif temp > temp_range[1] and humidity < humidity_range[0]:
    irrigation = True
else:
    irrigation = False

# Show irrigation status
if irrigation:
    st.success("Irrigation ON 💧 (Conditions are dry)")
else:
    st.info("Irrigation OFF (Soil and weather are optimal)")
