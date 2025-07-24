import tkinter as tk

CROP_THRESHOLD = 600

def should_irrigate(moisture, rain_expected=False):
    return (moisture < CROP_THRESHOLD) and not rain_expected

def update_status(*args):
    moisture = moisture_slider.get()
    rain_expected = rain_var.get() == 1  # 1 = rain, 0 = no rain

    status_text.set(f"Soil Moisture: {moisture}\nRain Expected: {rain_expected}")

    if should_irrigate(moisture, rain_expected):
        canvas.itemconfig(led, fill="green")
    else:
        canvas.itemconfig(led, fill="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Irrigation Simulator - Manual Control")

status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text, font=("Arial", 14))
status_label.pack(pady=10)

# Soil moisture slider (0–1023 like Arduino analog)
moisture_slider = tk.Scale(root, from_=0, to=1023, orient="horizontal",
                           label="Soil Moisture Sensor")
moisture_slider.set(500)
moisture_slider.pack(pady=10)
moisture_slider.bind("<Motion>", update_status)

# Rain expected toggle
rain_var = tk.IntVar()
rain_checkbox = tk.Checkbutton(root, text="Rain Expected", variable=rain_var,
                               command=update_status)
rain_checkbox.pack(pady=5)

canvas = tk.Canvas(root, width=100, height=100)
canvas.pack(pady=10)
led = canvas.create_oval(20, 20, 80, 80, fill="red")

# Initial update
update_status()

root.mainloop()
