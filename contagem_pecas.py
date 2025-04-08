import time
import random

# System variables
counter = 0
motor_on = True

def sensor_detects_piece():
    # Simulates the detection of a piece with 70% chance
    return random.random() < 0.7

print("Conveyor system started...\n")

while motor_on:
    time.sleep(0.5)  # Wait half a second between each sensor reading

    if sensor_detects_piece():
        counter += 1
        print(f"Piece detected! Counter: {counter}")
    else:
        print("No piece detected.")

    if counter >= 100:
        motor_on = False
        print("\n⚠️ 100 pieces reached. Conveyor stopped automatically.")

print("\nSystem shut down.")
