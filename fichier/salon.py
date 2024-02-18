import tkinter as tk
from PIL import Image, ImageTk

def connexion():
    email = entry_email.get()
    password = entry_password.get()
    print(f"Email : {email}, Mot de passe : {password}")

def inscription():
    print("Bouton Inscription appuyé")

def mot_de_passe_oublie():
    print("Lien Mot de passe oublié cliqué")

def toggle_password_visibility():
    if entry_password.cget("show") == "":
        entry_password.config(show="*")
    else:
        entry_password.config(show="")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Application moderne")
fenetre.geometry("600x400")

# Chargement de l'image en arrière-plan
image = Image.open("images/_73b77b98-93c2-4df4-8759-4104dec14d3c.jpg")
photo = ImageTk.PhotoImage(image)

# Création d'un label avec une police de caractères moderne et une couleur attrayante
label = tk.Label(fenetre, text="Bienvenue dans Mydiscord", font=("Roboto", 20), fg="#333333", bg="#f0f0f0")
label.pack(pady=20)

# Entrée pour l'email
label_email = tk.Label(fenetre, text="Email :", font=("Roboto", 12), fg="#333333", bg="#f0f0f0")
label_email.pack(pady=5)
entry_email = tk.Entry(fenetre, font=("Roboto", 12))
entry_email.pack(pady=5)

# Entrée pour le mot de passe
label_password = tk.Label(fenetre, text="Mot de passe :", font=("Roboto", 12), fg="#333333", bg="#f0f0f0")
label_password.pack(pady=5)
entry_password = tk.Entry(fenetre, font=("Roboto", 12), show="*")
entry_password.pack(pady=5)

# Boutons Connexion et Inscription
frame_boutons = tk.Frame(fenetre, bg="#f0f0f0")
frame_boutons.pack(pady=10)

bouton_connexion = tk.Button(frame_boutons, text="Connexion", font=("Roboto", 14), bg="#4CAF50", fg="white", relief="flat", command=connexion)
bouton_connexion.pack(side="left", padx=5)

bouton_inscription = tk.Button(frame_boutons, text="Inscription", font=("Roboto", 14), bg="#3498db", fg="white", relief="flat", command=inscription)
bouton_inscription.pack(side="left", padx=5)

# Bouton pour afficher/masquer le mot de passe
bouton_afficher_mot_de_passe = tk.Button(fenetre, text="👁️", font=("Roboto", 12), bg="#f0f0f0", fg="#333333", relief="flat", command=toggle_password_visibility)
bouton_afficher_mot_de_passe.pack(pady=5)

# Lien Mot de passe oublié
lien_mot_de_passe_oublie = tk.Label(fenetre, text="Mot de passe oublié ?", font=("Roboto", 12), fg="#007bff", bg="#f0f0f0", cursor="hand2")
lien_mot_de_passe_oublie.pack(pady=5)
lien_mot_de_passe_oublie.bind("<Button-1>", lambda event: mot_de_passe_oublie())

# Boucle principale de l'application

fenetre.mainloop()

