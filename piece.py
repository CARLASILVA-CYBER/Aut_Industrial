import time

# Variables
counter = 0               # Piece counter
MAX_PIECES = 100          # Limit of pieces
motor_running = True      # Motor state

def optical_sensor():
    """
    Simulates the detection of a piece by an optical sensor.
    For this demo, we assume a piece is always detected in each cycle.
    """
    return True

def main():
    global counter, motor_running

    print("🔄 Conveyor belt system started.\n")
    while motor_running:
        time.sleep(0.3)  # Simulates the delay between pieces arriving

        if optical_sensor():
            counter += 1
            print(f"📦 Piece detected. Total pieces counted: {counter}")

        if counter >= MAX_PIECES:
            motor_running = False
            print("\n🛑 100 pieces reached! Stopping the motor automatically.")

    print("\n✅ System shut down.\n")

if __name__ == "__main__":
    main()
