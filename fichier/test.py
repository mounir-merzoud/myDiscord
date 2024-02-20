import tkinter as tk
from PIL import Image, ImageTk
import mariadb

# Création de la fenêtre principale
root = tk.Tk()
root.title("Salons")  # Titre de la fenêtre

# Personnalisation de la couleur de fond de la fenêtre
root.configure(bg="lightgray")

# Personnalisation de la taille de la fenêtre
root.geometry("760x900")  # Largeur x Hauteur

# Personnalisation de la police de caractères pour les futurs widgets
custom_font = ("Arial", 12)
class Salons:
     def __init__(self, id_utilisateur, image, nom, prenom, email, activite):
        self.id_utilisateur = id_utilisateur
        self.image = image
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.activite = activite
# Connexion à la base de données MariaDB
    try:
        connection = mariadb.connect(
            host="plesk.students-laplateforme.io",
            port=3306,  
            user="mounir",
            password="mounir-1992",
            database="kamelia-mohamdi_mydiscord"


# Lancement de la boucle principale de l'application
root.mainloop()
