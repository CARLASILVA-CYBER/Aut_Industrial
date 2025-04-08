import time
import random

# Initial state
lamp_on = False
last_motion_time = None
timer_duration = 10  # seconds

def motion_detected():
    """
    Simulates motion detection.
    Returns True 30% of the time (adjustable).
    """
    return random.random() < 0.3

def main():
    global lamp_on, last_motion_time

    print("🚶 Corridor lighting system started.\n")

    while True:
        time.sleep(1)  # simulate 1 second per cycle

        if motion_detected():
            print("📡 Motion detected!")
            lamp_on = True
            last_motion_time = time.time()
        else:
            if lamp_on and last_motion_time:
                elapsed = time.time() - last_motion_time
                if elapsed >= timer_duration:
                    lamp_on = False
                    print("💡 Lamp turned OFF after 10 seconds with no motion.")
                    last_motion_time = None

        # Show lamp state
        if lamp_on:
            print("💡 Lamp is ON.")
        else:
            print("🔌 Lamp is OFF.")

if __name__ == "__main__":
    main()
