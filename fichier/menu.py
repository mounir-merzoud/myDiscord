import tkinter as tk
from tkinter import PhotoImage

# Création de la fenêtre principale
root = tk.Tk()

# Définition de la couleur de fond
couleur_fond = "#FFC0CB"  # Code couleur pour le rose clair (vous pouvez changer cette valeur selon votre préférence)
couleur_titre = "orange"  # Couleur de fond du titre
couleur_bouton = "orange"  # Couleur de fond des boutons
couleur_texte = "blue"  # Couleur du texte en bleu

# Configuration de la couleur de fond de la fenêtre
root.configure(bg=couleur_fond)

# Titre de la fenêtre
root.title("Fenêtre avec fond rose")

# Fonction pour afficher un message lorsqu'un bouton est cliqué
def bouton_clic():
    print("Bouton cliqué!")

# Chargement des images pour les boutons et redimensionnement
image_1 = PhotoImage(file="images/salon.png").subsample(3)  # Redimensionne l'image à un tiers de sa taille d'origine
image_2 = PhotoImage(file="images/utilisateurs.png").subsample(3)
image_3 = PhotoImage(file="images/services-parametres-et-icone-d-engrenage-orange.png").subsample(3)
image_4 = PhotoImage(file="images/deconnexion.png").subsample(3)

# Fonction pour créer un bouton avec son titre
def creer_bouton_titre(image, titre):
    # Création d'un cadre pour le bouton et son titre
    cadre_bouton = tk.Frame(root, bg=couleur_bouton)
    cadre_bouton.pack(side=tk.LEFT, padx=10, pady=10)

    # Création du titre au-dessus du bouton
    titre_label = tk.Label(cadre_bouton, text=titre, font=("new time is roman", 12), bg=couleur_titre, fg=couleur_texte)
    titre_label.pack(fill=tk.X)

    # Création du bouton avec l'image
    bouton = tk.Button(cadre_bouton, image=image, bg=couleur_bouton, command=bouton_clic)
    bouton.pack()

# Titre au-dessus des boutons
titre_principal = tk.Label(root, text="Bienvenue in myDiscord", font=("new time is roman", 20), bg=couleur_titre, fg=couleur_texte)
titre_principal.pack(fill=tk.X, pady=10)

# Création des boutons avec leurs titres
creer_bouton_titre(image_1, "Salon")
creer_bouton_titre(image_2, "Utilisateurs")
creer_bouton_titre(image_3, "Services & Paramètres")
creer_bouton_titre(image_4, "Déconnexion")

# Boucle principale pour afficher la fenêtre
root.mainloop()
