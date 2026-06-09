import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "bmi_history.csv"

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

        save_record(weight, height, bmi, category)

    except:
        messagebox.showerror(
            "Invalid Input",
            "Enter valid height and weight values."
        )

def save_record(weight, height, bmi, category):
    data = pd.DataFrame(
        [[weight, height, bmi, category]],
        columns=["Weight", "Height", "BMI", "Category"]
    )

    if os.path.exists(FILE_NAME):
        data.to_csv(FILE_NAME, mode="a",
                    header=False, index=False)
    else:
        data.to_csv(FILE_NAME, index=False)

def show_history():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo(
            "History",
            "No records found."
        )
        return

    history = pd.read_csv(FILE_NAME)

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")

    text = tk.Text(history_window,
                   width=60,
                   height=20)

    text.pack()

    text.insert(tk.END, history.to_string())

def show_graph():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo(
            "Graph",
            "No records available."
        )
        return

    data = pd.read_csv(FILE_NAME)

    plt.figure(figsize=(8,5))
    plt.plot(data.index + 1,
             data["BMI"],
             marker="o")

    plt.title("BMI Trend")
    plt.xlabel("Record Number")
    plt.ylabel("BMI")
    plt.grid(True)

    plt.show()

root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Weight (kg)",
    fg="white",
    bg="#1e1e1e"
).pack()

weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(
    root,
    text="Height (m)",
    fg="white",
    bg="#1e1e1e"
).pack()

height_entry = tk.Entry(root)
height_entry.pack(pady=5)

tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#4CAF50",
    fg="white"
).pack(pady=15)

tk.Button(
    root,
    text="View History",
    command=show_history
).pack(pady=5)

tk.Button(
    root,
    text="Show Graph",
    command=show_graph
).pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    fg="yellow",
    bg="#1e1e1e"
)

result_label.pack(pady=20)

root.mainloop()