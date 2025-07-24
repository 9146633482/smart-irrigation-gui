import tkinter as tk
import random
import time

CROP_THRESHOLD = 600

def should_irrigate(moisture, rain_expected=False):
    return (moisture < CROP_THRESHOLD) and not rain_expected

def update_status():
    moisture = random.randint(300, 800)
    rain_expected = random.choice([False, False, True])

    status_text.set(f"Moisture: {moisture}\nRain Expected: {rain_expected}")

    if should_irrigate(moisture, rain_expected):
        canvas.itemconfig(led, fill="green")
    else:
        canvas.itemconfig(led, fill="red")

    root.after(2000, update_status)  # repeat every 2 seconds

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Irrigation Simulator")

status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 14))
status_label.pack(pady=10)

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack()
led = canvas.create_oval(20, 20, 80, 80, fill="red")

update_status()
root.mainloop()
