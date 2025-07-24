import random
import time

while True:
    # Simulate soil moisture sensor values (0–1023)
    sensor_value = random.randint(300, 800)
    print(f"Soil moisture: {sensor_value}")
    time.sleep(2)  # update every 2 seconds
