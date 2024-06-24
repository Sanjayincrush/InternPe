import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('Arial', 40, 'bold'), background='white', foreground='blue')
label.pack(anchor='center')

# Call the update_time function to display the time and update it every second
update_time()

# Run the Tkinter event loop
root.mainloop()
