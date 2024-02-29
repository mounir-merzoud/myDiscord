import tkinter as tk
from tkinter import Text, Button

# Fonction pour envoyer un message
def envoyer_message():
    message = champ_message.get("1.0", "end")  # Récupérer le message du champ de texte
    champ_reception.insert("end", f"Vous: {message}")  # Ajouter le message dans la zone d'affichage des messages reçus
    champ_message.delete("1.0", "end")  # Effacer le champ de saisie

# Créer une instance de la classe Tk
fenetre = tk.Tk()

# Définir le titre de la fenêtre
fenetre.title("Salon")

# Définir les dimensions de la fenêtre (largeur x hauteur)
fenetre.geometry("800x700")  # Ajustement des dimensions de la fenêtre

# Définir la couleur de fond de la fenêtre
fenetre.configure(bg="pink")

# Créer un cadre bleu pour l'entête
entete_cadre = tk.Frame(fenetre, bg="blue", height=100)
entete_cadre.pack(fill="x")  # Remplir horizontalement

# Créer un cadre vert pour le salon
cadre_des_salon = tk.Frame(fenetre, bg="green", width=300, height=600)
cadre_des_salon.pack(padx=10, pady=10, side="left", anchor="sw")

# Champ pour afficher les messages reçus
champ_reception = Text(cadre_des_salon, height=25, width=50)
champ_reception.grid(row=0, column=0, padx=10, pady=10)

# Créer un cadre blanc pour le formulaire
formulaire_cadre = tk.Frame(fenetre, bg="white", width=200, height=80)
formulaire_cadre.place(x=10, y=600)  # Utilisation de la méthode place pour positionner le cadre

# Champ de texte pour saisir le message
champ_message = Text(formulaire_cadre, height=5, width=50)
champ_message.grid(row=0, column=0, padx=10, pady=10)  # Utilisation de la disposition de grille

# Bouton d'envoi
bouton_envoi = Button(formulaire_cadre, text="Envoyer", command=envoyer_message)
bouton_envoi.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Utilisation de la disposition de grille et aligné à droite

# Boucle principale pour que la fenêtre reste ouverte
fenetre.mainloop()
