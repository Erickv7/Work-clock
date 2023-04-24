import tkinter as tk
from tkinter import ttk
import time
import threading
import winsound

# Function to update the timer display
def update_timer(minutes, seconds):
    timer_display.configure(text=f"{minutes:02d}:{seconds:02d}")

# Function to handle the timer counting
def timer():
    minutes, seconds = 0, 0
    while running:
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 10:
            # Play a notification sound
            winsound.PlaySound('waves_sound.wav', 0)
            minutes, seconds = 0, 0

        update_timer(minutes, seconds)
        time.sleep(1)
        seconds += 1

# Function to start the timer
def start_timer():
    global running
    running = True
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

# Function to stop the timer and reset it to zero
def stop_timer():
    global running
    running = False
    update_timer(0, 0)

# Create the main tkinter window
root = tk.Tk()
root.title("Chronometer")
root.iconbitmap("alarm_clock.ico")

# Set the style for the tkinter interface
style = ttk.Style()
style.configure("TButton", font=("Arial", 20))
style.configure("TLabel", font=("Arial", 40), background="white")

# Create the timer display
timer_display = ttk.Label(root, text="00:00")
timer_display.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

# Create the start button
start_button = ttk.Button(root, text="Start", command=start_timer)
start_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Create the stop button
stop_button = ttk.Button(root, text="Finish", command=stop_timer)
stop_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

running = False

# Run the tkinter main loop
root.mainloop()
