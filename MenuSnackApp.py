import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.config(background="#FDE2E4")
root.title("Menu - Stand de Concession")
root.geometry("400x600")

font_title = ("Brush Script MT", 32, "bold")
font_items = ("Helvetica", 14, "bold")
font_buttons = ("Helvetica", 12)
button_bg = "#FFB6C1"
button_fg = "white"

menu_items = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 32.00,
    "Burger": 30.00,
    "Fries": 15.00,
    "Nuggets": 15.00,
    "Soda": 18.00,
    "Limonade": 18.00,
}

selected_items = []

def add_to_cart(item):
  selected_items.append(item)
  messagebox.showinfo("Ajouté", f"{item} a été ajouté au panier.") 

def show_total():
    total = sum(menu_items[item] for item in selected_items)
    if selected_items:
        items_list = "\n".join(selected_items)
        messagebox.showinfo("Total", f"Articles sélectionnés :\n\n\n{items_list}\n\nTotal : {total:.2f} MAD")
    else:
        messagebox.showwarning("Panier vide", "Vous n'avez sélectionné aucun article.")

def reset_cart():
    selected_items.clear()
    messagebox.showinfo("Réinitialisé", "Le panier a été réinitialisé.")

tk.Label(
    root, text="MENU RESTAURANT", font=font_title, bg="#FDE2E4", fg="#E75480"
).pack(pady=20)

frame_items = tk.Frame(root, bg="#FDE2E4")
frame_items.pack(pady=10)

for item in menu_items:
    btn = tk.Button(
        frame_items,
        text=f"{item} - {menu_items[item]:.2f} MAD",
        font=font_items,
        bg=button_bg,
        fg=button_fg,
        command=lambda i=item: add_to_cart(i),
        relief="flat",
        width=25,
    )
    btn.pack(pady=5)

tk.Button(
    root,
    text="Afficher le Total",
    font=font_buttons,
    bg="#FF69B4",
    fg="white",
    command=show_total,
    relief="raised",
).pack(pady=20)

tk.Button(
    root,
    text="Réinitialiser le Panier",
    font=font_buttons,
    bg="#FF1493",
    fg="white",
    command=reset_cart,
    relief="raised",
).pack(pady=10)

root.mainloop()