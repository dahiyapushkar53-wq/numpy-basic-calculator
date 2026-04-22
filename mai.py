import numpy as np
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        numbers = entry.get()
        num_list = list(map(int, numbers.split()))
        arr = np.array(num_list)

        result = f"""
Array: {arr}
Sum: {np.sum(arr)}
Average: {np.mean(arr)}
Max: {np.max(arr)}
Min: {np.min(arr)}
"""
        messagebox.showinfo("Result", result)

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Create window
root = tk.Tk()
root.title("NumPy Calculator")
root.geometry("300x200")

# Input field
label = tk.Label(root, text="Enter numbers:")
label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Button
btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=10)

# Run app
root.mainloop()
