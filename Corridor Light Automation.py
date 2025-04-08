import tkinter as tk
import time

class CorridorLightSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Corridor Light Automation")

        self.lamp_on = False
        self.last_motion_time = None
        self.timer_duration = 10  # seconds

        # GUI Elements
        self.status_label = tk.Label(master, text="System Ready", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.lamp_label = tk.Label(master, text="💡 Lamp is OFF", font=("Arial", 14), fg="gray")
        self.lamp_label.pack(pady=10)

        self.motion_button = tk.Button(master, text="Simulate Motion", command=self.simulate_motion,
                                       font=("Arial", 12), bg="lightgreen")
        self.motion_button.pack(pady=20)

        # Check timer every second
        self.update_lamp_state()

    def simulate_motion(self):
        self.lamp_on = True
        self.last_motion_time = time.time()
        self.status_label.config(text="📡 Motion Detected!")
        self.lamp_label.config(text="💡 Lamp is ON", fg="orange")

    def update_lamp_state(self):
        if self.lamp_on and self.last_motion_time:
            elapsed = time.time() - self.last_motion_time
            if elapsed >= self.timer_duration:
                self.lamp_on = False
                self.last_motion_time = None
                self.status_label.config(text="⏱️ No motion detected for 10 seconds.")
                self.lamp_label.config(text="💡 Lamp is OFF", fg="gray")

        elif not self.lamp_on:
            self.lamp_label.config(text="💡 Lamp is OFF", fg="gray")

        # Repeat every second
        self.master.after(1000, self.update_lamp_state)

# Run the GUI
root = tk.Tk()
app = CorridorLightSystem(root)
root.mainloop()
