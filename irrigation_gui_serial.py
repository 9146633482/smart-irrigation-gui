import tkinter as tk
import serial
import threading
import time

CROP_THRESHOLD = 600
SERIAL_PORT = 'COM3'  # Change if needed
BAUD_RATE = 9600

use_serial = False  # Default to slider mode

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    use_serial = True
    print(f"Connected to Arduino on {SERIAL_PORT}")
except:
    print("No Arduino found. Using slider mode.")

def should_irrigate(moisture, rain_expected=False):
    return (moisture < CROP_THRESHOLD) and not rain_expected

def update_gui(moisture, rain_expected):
    status_text.set(f"Soil Moisture: {moisture}\nRain Expected: {rain_expected}")
    if should_irrigate(moisture, rain_expected):
        canvas.itemconfig(led, fill="green")
    else:
        canvas.itemconfig(led, fill="red")

def serial_reader():
    while use_serial:
        try:
            if ser.in_waiting > 0:
                value = ser.readline().decode().strip()
                if value.isdigit():
                    rain_expected = rain_var.get() == 1
                    update_gui(int(value), rain_expected)
        except:
            pass
        time.sleep(1)

def slider_update(*args):
    if not use_serial:
        moisture = moisture_slider.get()
        rain_expected = rain_var.get() == 1
        update_gui(moisture, rain_expected)

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Irrigation Simulator - Serial + Slider")

status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 14))
status_label.pack(pady=10)

# Slider for manual mode
moisture_slider = tk.Scale(root, from_=0, to=1023, orient="horizontal",
                           label="Soil Moisture Sensor (Manual Mode)")
moisture_slider.set(500)
moisture_slider.pack(pady=10)
moisture_slider.bind("<Motion>", slider_update)

# Rain expected toggle
rain_var = tk.IntVar()
rain_checkbox = tk.Checkbutton(root, text="Rain Expected", variable=rain_var,
                               command=slider_update)
rain_checkbox.pack(pady=5)

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack(pady=10)
led = canvas.create_oval(20, 20, 80, 80, fill="red")

update_gui(500, False)

if use_serial:
    threading.Thread(target=serial_reader, daemon=True).start()

root.mainloop()
