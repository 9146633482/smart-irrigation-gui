import random
import time

CROP_THRESHOLD = 600  # irrigation threshold

def should_irrigate(moisture, rain_expected=False):
    return (moisture < CROP_THRESHOLD) and not rain_expected

def set_led(state):
    if state:
        print("[LED ON] Irrigation valve is OPEN")
    else:
        print("[LED OFF] Irrigation valve is CLOSED")

while True:
    # Simulate soil moisture sensor values
    moisture = random.randint(300, 800)
    rain_expected = random.choice([False, False, True])  # 1/3 chance of rain

    print(f"Moisture: {moisture}, Rain Expected: {rain_expected}")

    if should_irrigate(moisture, rain_expected):
        set_led(True)
    else:
        set_led(False)

    print("-" * 40)
    time.sleep(2)
