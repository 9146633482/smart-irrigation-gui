import serial
import time
import requests
import streamlit as st

# ---- SETTINGS ----
API_KEY = "330daeb966445571600c64b3388909f2" 
CITY = "Pune,IN"         
SERIAL_PORT = "COM3"     
BAUD_RATE = 9600

# ---- Thresholds for Tomato Crop ----
MOISTURE_THRESHOLD = 550  # Soil moisture (0-1023) for tomatoes
TEMP_OPTIMAL = (18, 27)   # Optimal temp range in °C
HUMIDITY_OPTIMAL = (60, 80)  # Optimal humidity %

# ---- Setup Serial Connection ----
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    arduino_connected = True
except:
    arduino_connected = False

# ---- Weather API function ----
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    r = requests.get(url).json()
    temp = r['main']['temp']
    humidity = r['main']['humidity']
    season = "Summer" if temp > 30 else "Winter" if temp < 15 else "Moderate"
    return temp, humidity, season

# ---- Streamlit GUI ----
st.title("Smart Irrigation System for Tomato Crop")
st.write("Real-time soil moisture, temperature, and humidity monitoring.")

# Read soil moisture
if arduino_connected:
    ser.write(b"R")  # Send request (optional)
    if ser.in_waiting > 0:
        moisture = ser.readline().decode().strip()
    else:
        moisture = "No data"
else:
    moisture = st.slider("Soil Moisture (simulate)", 0, 1023, 400)

# Get weather data
temp, humidity, season = get_weather()

# Decision logic
irrigation_needed = int(moisture) < MOISTURE_THRESHOLD or temp > TEMP_OPTIMAL[1]

st.metric("Soil Moisture", f"{moisture} / 1023")
st.metric("Temperature", f"{temp} °C")
st.metric("Humidity", f"{humidity} %")
st.metric("Season", season)

if irrigation_needed:
    st.success("Irrigation ON - Conditions require watering.")
else:
    st.info("Irrigation OFF - Conditions are optimal.")
