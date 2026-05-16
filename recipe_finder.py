# File Name: recipe_finder.py

import tkinter as tk
from tkinter import messagebox
import requests

# =========================
# FUNCTION TO FIND RECIPE
# =========================

def search_recipe():

    recipe_name = recipe_entry.get()

    if recipe_name.strip() == "":
        messagebox.showwarning("Warning", "Please enter a recipe name")
        return

    try:

        # API URL
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}"

        # Fetch data
        response = requests.get(url)
        data = response.json()

        # Clear old data
        result_text.delete(1.0, tk.END)

        # If recipe found
        if data["meals"]:

            meal = data["meals"][0]

            recipe_details = f"""
🍲 Recipe Name:
{meal['strMeal']}

📂 Category:
{meal['strCategory']}

🌍 Cuisine:
{meal['strArea']}

📝 Instructions:
{meal['strInstructions']}
"""

            result_text.insert(tk.END, recipe_details)

        else:
            result_text.insert(tk.END, "Recipe not found.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# =========================
# MAIN WINDOW
# =========================

root = tk.Tk()
root.title("Recipe Finder")
root.geometry("750x600")
root.config(bg="lightgreen")

# =========================
# TITLE LABEL
# =========================

title_label = tk.Label(
    root,
    text="🍴 Recipe Finder App",
    font=("Arial", 22, "bold"),
    bg="lightgreen"
)

title_label.pack(pady=15)

# =========================
# ENTRY LABEL
# =========================

recipe_label = tk.Label(
    root,
    text="Enter Recipe Name:",
    font=("Arial", 13),
    bg="lightgreen"
)

recipe_label.pack()

# =========================
# ENTRY BOX
# =========================

recipe_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 14)
)

recipe_entry.pack(pady=10)

# =========================
# SEARCH BUTTON
# =========================

search_button = tk.Button(
    root,
    text="Search Recipe",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=search_recipe
)

search_button.pack(pady=10)

# =========================
# TEXT AREA
# =========================

result_text = tk.Text(
    root,
    width=85,
    height=25,
    font=("Arial", 11),
    wrap="word"
)

result_text.pack(pady=10)

# =========================
# RUN APPLICATION
# =========================

root.mainloop()