import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# -----------------------------
# Password Generation
# -----------------------------
def generate_password():
    chars = ""

    if upper_var.get():
        chars += string.ascii_uppercase

    if lower_var.get():
        chars += string.ascii_lowercase

    if number_var.get():
        chars += string.digits

    if symbol_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showerror("Error", "Select at least one character type.")
        return

    try:
        length = int(length_entry.get())

        if length <= 0:
            raise ValueError

    except:
        messagebox.showerror("Error", "Enter a valid password length.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    check_strength(password)


# -----------------------------
# Password Strength
# -----------------------------
def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")

    elif score <= 4:
        strength_label.config(text="Strength: Medium", fg="orange")

    else:
        strength_label.config(text="Strength: Strong", fg="lightgreen")


# -----------------------------
# Copy Password
# -----------------------------
def copy_password():

    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    pyperclip.copy(password)

    messagebox.showinfo("Copied", "Password copied to clipboard.")


# -----------------------------
# GUI
# -----------------------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("600x550")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title.pack(pady=20)

# Length

tk.Label(
    root,
    text="Password Length",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 11)
).pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Checkboxes

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(
    root,
    text="Uppercase Letters",
    variable=upper_var,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333"
).pack()

tk.Checkbutton(
    root,
    text="Lowercase Letters",
    variable=lower_var,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333"
).pack()

tk.Checkbutton(
    root,
    text="Numbers",
    variable=number_var,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333"
).pack()

tk.Checkbutton(
    root,
    text="Symbols",
    variable=symbol_var,
    bg="#1e1e1e",
    fg="white",
    selectcolor="#333333"
).pack()

# Generate Button

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
generate_btn.pack(pady=15)

# Password Output

password_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
password_entry.pack(pady=10)

# Strength Label

strength_label = tk.Label(
    root,
    text="Strength: -",
    bg="#1e1e1e",
    fg="white",
    font=("Arial", 14, "bold")
)
strength_label.pack(pady=10)

# Copy Button

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold")
)
copy_btn.pack(pady=10)

root.mainloop()