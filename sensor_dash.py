import tkinter as tk
from tkinter import messagebox
import random

class ConveyorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conveyor Belt Simulation")
        self.counter = 0
        self.motor_on = True

        # Labels
        self.status_label = tk.Label(master, text="System Ready", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.counter_label = tk.Label(master, text="Pieces Counted: 0", font=("Arial", 14))
        self.counter_label.pack(pady=10)

        # Button to simulate piece detection
        self.detect_button = tk.Button(master, text="Detect Piece", command=self.detect_piece,
                                       font=("Arial", 12), bg="lightblue")
        self.detect_button.pack(pady=20)

    def detect_piece(self):
        if not self.motor_on:
            return

        if random.random() < 0.7:
            self.counter += 1
            self.status_label.config(text="Piece Detected!")
            self.counter_label.config(text=f"Pieces Counted: {self.counter}")
        else:
            self.status_label.config(text="No Piece Detected.")

        if self.counter >= 100:
            self.motor_on = False
            self.status_label.config(text="⚠️ Conveyor Stopped!")
            messagebox.showinfo("System", "100 pieces reached. Conveyor stopped.")

# Main window
root = tk.Tk()
app = ConveyorApp(root)
root.mainloop()
