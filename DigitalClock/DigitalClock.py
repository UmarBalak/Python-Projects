import tkinter as tk
import time

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("700x180")
window.configure(bg="black")


# display the date and time
clock_label = tk.Label(window, font=("Arial", 40), fg="cyan", bg="black")
clock_label.pack(pady=20)

# year, day, and month
date_label = tk.Label(window, font=("Arial", 20), fg="cyan", bg="black")
date_label.pack()


# Function to update the date and time
def update_datetime():
    current_datetime = time.strftime("%I hr : %M min : %S sec  %p")
    current_date = time.strftime("%Y   %d   %B")
    clock_label.config(text=current_datetime)
    date_label.config(text=current_date)
    clock_label.after(1000, update_datetime)


update_datetime()

window.mainloop()
