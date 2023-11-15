import tkinter as tk


def on_menu_click(menu_item):
    tk.Label.config(text=f"Vous avez cliqué sur {menu_item}")

# Fonction pour changer la vue principale


def change_main_view(view_name):
    main_view_label.config(text=f"Vue principale : {view_name}")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface avec Menu Latéral")

# Cadre principal
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Menu Latéral
menu_frame = tk.Frame(main_frame, width=200, bg="lightgray")
menu_frame.pack(side=tk.LEFT, fill=tk.Y)

# Boutons du Menu Latéral
btn_home = tk.Button(menu_frame, text="Accueil",
                     command=lambda: change_main_view("Accueil"))
btn_page1 = tk.Button(menu_frame, text="Page 1",
                      command=lambda: change_main_view("Page 1"))
btn_page2 = tk.Button(menu_frame, text="Page 2",
                      command=lambda: change_main_view("Page 2"))

btn_home.pack(pady=10)
btn_page1.pack(pady=10)
btn_page2.pack(pady=10)

# Vue Principale
main_view_frame = tk.Frame(main_frame, bg="white")
main_view_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Étiquette pour afficher la vue principale
main_view_label = tk.Label(
    main_view_frame, text="Vue principale : Accueil", font=("Helvetica", 16))
main_view_label.pack(pady=20)

# Étiquette pour afficher le titre
title_label = tk.Label(main_frame, text="Mon Application",
                       font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

# Boucle principale
root.mainloop()
