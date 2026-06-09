import tkinter as tk
from tkinter import messagebox
import requests

# -------------------------------
# Weather Function
# -------------------------------
history = []

def save_history(city):
    history.append(city)

    if len(history) > 5:
        history.pop(0)

    history_label.config(
        text="Recent Searches:\n" + "\n".join(history)
    )


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Enter a city name")
        return

    try:
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url, timeout=10)
        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        humidity = current["humidity"]
        wind = current["windspeedKmph"]
        condition = current["weatherDesc"][0]["value"]

        result.config(
            text=f"""
Temperature: {temp} °C

Humidity: {humidity} %

Wind Speed: {wind} km/h

Condition: {condition}
"""
        )

        save_history(city)

    except Exception:
        messagebox.showerror(
            "Error",
            "Unable to fetch weather data"
        )


# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("600x600")
root.configure(bg="#1e1e1e")

title = tk.Label(
    root,
    text="Weather Application",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=20)

tk.Label(
    root,
    text="City Name",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e1e"
).pack()

city_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
city_entry.pack(pady=10)

btn = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    fg="lightgreen",
    bg="#1e1e1e",
    font=("Arial", 13),
    justify="left"
)
result.pack(pady=20)

history_label = tk.Label(
    root,
    text="Recent Searches:",
    fg="white",
    bg="#1e1e1e",
    font=("Arial", 10),
    justify="left"
)
history_label.pack(pady=10)

footer = tk.Label(
    root,
    text="Powered by wttr.in",
    fg="gray",
    bg="#1e1e1e",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()