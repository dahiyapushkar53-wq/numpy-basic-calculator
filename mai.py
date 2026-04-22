import numpy as np
import tkinter as tk
from tkinter import messagebox

# Area names
areas = ["Zone A", "Zone B", "Zone C", "Zone D", "Zone E"]

# Input fields
entries_pop = []
entries_res = []

# Run analysis
def run_analysis():
    try:
        population = []
        resources = []

        # Collect input
        for i in range(len(areas)):
            pop = int(entries_pop[i].get())
            res = int(entries_res[i].get())

            population.append(pop)
            resources.append(res)

        population = np.array(population)
        resources = np.array(resources)

        # Calculate need
        need = np.clip(population - resources, 0, None)

        # Critical zones
        critical = np.where(need > 50)[0]

        # Output display
        output.delete("1.0", tk.END)
        output.insert(tk.END, "📊 Relief Analysis Report\n")
        output.insert(tk.END, "-" * 30 + "\n")

        for i in range(len(areas)):
            output.insert(
                tk.END,
                f"{areas[i]} → Need: {need[i]} units\n"
            )

        output.insert(tk.END, "\n🚨 Critical Zones:\n")

        if len(critical) == 0:
            output.insert(tk.END, "No critical zones\n")
        else:
            for i in critical:
                output.insert(
                    tk.END,
                    f"{areas[i]} needs urgent help!\n"
                )

    except:
        messagebox.showerror("Error", "Please enter valid numbers!")

# GUI setup
root = tk.Tk()
root.title("🌍 Disaster Relief Optimizer")
root.geometry("450x500")
root.configure(bg="#1e1e1e")

# Title
title = tk.Label(
    root,
    text="Relief Resource Analyzer",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

# Headings
tk.Label(frame, text="Area", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=10)
tk.Label(frame, text="Population", fg="white", bg="#1e1e1e").grid(row=0, column=1)
tk.Label(frame, text="Resources", fg="white", bg="#1e1e1e").grid(row=0, column=2)

# Input fields
for i in range(len(areas)):
    tk.Label(frame, text=areas[i], fg="white", bg="#1e1e1e").grid(row=i+1, column=0)

    e1 = tk.Entry(frame, width=10)
    e1.grid(row=i+1, column=1, padx=5, pady=5)
    entries_pop.append(e1)

    e2 = tk.Entry(frame, width=10)
    e2.grid(row=i+1, column=2, padx=5, pady=5)
    entries_res.append(e2)

# Button
btn = tk.Button(
    root,
    text="Run Analysis",
    command=run_analysis,
    bg="cyan",
    fg="black",
    font=("Arial", 10, "bold")
)
btn.pack(pady=10)

# Output box
output = tk.Text(root, height=12, width=50, bg="black", fg="white")
output.pack(pady=10)

root.mainloop()