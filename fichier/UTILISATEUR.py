import tkinter as tk
from PIL import Image, ImageTk
import mariadb

class Utilisateur:
    def __init__(self, id_utilisateur, image, nom, prenom, email, activite):
        self.id_utilisateur = id_utilisateur
        self.image = image
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.activite = activite

    @classmethod
    def charger_tous(cls):
        utilisateurs = []
        try:
            connection = mariadb.connect(
                host="plesk.students-laplateforme.io",
                port=3306,  
                user="mounir",
                password="mounir-1992",
                database="kamelia-mohamdi_mydiscord"
            )

            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user")
            resultats = cursor.fetchall()

            for utilisateur in resultats:
                utilisateurs.append(cls(
                    id_utilisateur=utilisateur['id_utilisateur'],
                    image=utilisateur['image'],
                    nom=utilisateur['nom'],
                    prenom=utilisateur['prenom'],
                    email=utilisateur['email'],
                    activite=utilisateur['activite']
                ))

            return utilisateurs
        except mariadb.Error as error:
            print("Erreur lors de la connexion à la base de données :", error)
            return None
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

# Exemple d'utilisation pour charger tous les utilisateurs depuis la base de données
liste_utilisateurs = Utilisateur.charger_tous()
if liste_utilisateurs:
    for utilisateur in liste_utilisateurs:
        print("Utilisateur chargé avec succès :", utilisateur.nom, utilisateur.prenom)
else:
    print("Impossible de charger les utilisateurs.")
