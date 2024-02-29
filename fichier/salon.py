import tkinter as tk  # Importation du module tkinter pour créer des interfaces graphiques
from tkinter import ttk  # Importation de ttk (themed Tkinter) pour des widgets stylisés
import mariadb  # Importation du module mariadb pour la connexion à la base de données MariaDB

id_salon = "1"

class SalonApp:  # Définition d'une classe SalonApp pour l'application de salon de discussion
    def __init__(self, parent):  # Initialisation de la classe SalonApp avec le parent de l'application
        self.parent = parent  # Attribution du parent de l'application
        self.initialize_gui()  # Initialisation de l'interface graphique de l'application

    def initialize_gui(self):  # Méthode pour initialiser l'interface graphique de l'application
        self.root = self.parent  # Attribution de la fenêtre principale à l'attribut root
        self.root.title("Salon")  # Définition du titre de la fenêtre principale

        self.nom_du_salon_label = ttk.Label(self.root, text="Bienvenue sur le Salon", font=("Helvetica", 16))  # Création d'une étiquette pour le titre du salon
        self.nom_du_salon_label.pack(pady=10)  # Placement de l'étiquette dans la fenêtre principale avec un espacement

        self.root.configure(bg='LightSalmon')  # Configuration de la couleur de fond de la fenêtre principale

        self.root.style = ttk.Style()  # Création d'un objet de style pour personnaliser les widgets
        self.root.style.theme_create("custom", parent="clam", settings={  # Création d'un thème personnalisé
            "TButton": {"configure": {"background": "Salmon3", "foreground": "white", "font": ("Helvetica", 12)}},  # Configuration des boutons
            "TLabel": {"configure": {"foreground": "white", "font": ("Helvetica", 12), "background": "Salmon3"}},  # Configuration des étiquettes
            "TFrame": {"configure": {"background": "LightSalmon"}},  # Configuration des cadres
            "TText": {"configure": {"background": "Salmon3", "foreground": "white", "font": ("Helvetica", 12)}}  # Configuration des zones de texte
        })
        self.root.style.theme_use("custom")  # Utilisation du thème personnalisé pour les widgets de la fenêtre principale

        self.message_frame = ttk.Frame(self.root)  # Création d'un cadre pour afficher les messages
        self.message_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Placement du cadre avec un espacement et une expansion

        self.message_list = tk.Text(self.message_frame, bg='Salmon3', fg='white', font=('Helvetica', 12), state=tk.DISABLED)  # Création d'une zone de texte pour afficher les messages
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Placement de la zone de texte dans le cadre avec expansion

        self.scrollbar = ttk.Scrollbar(self.message_frame, command=self.message_list.yview)  # Création d'une barre de défilement pour la zone de texte
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Placement de la barre de défilement à droite du cadre

        self.message_list.config(yscrollcommand=self.scrollbar.set)  # Configuration de la barre de défilement pour contrôler le défilement de la zone de texte

        self.input_frame = ttk.Frame(self.root)  # Création d'un cadre pour la saisie de message
        self.input_frame.pack(padx=10, pady=10, fill=tk.BOTH)  # Placement du cadre avec un espacement

        self.message_input = tk.Text(self.input_frame, height=3, bg='Salmon3', fg='white', font=('Helvetica', 12))  # Création d'une zone de texte pour la saisie de message
        self.message_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Placement de la zone de texte dans le cadre avec expansion

        self.send_button = ttk.Button(self.input_frame, text="🚀", command=self.send_message)  # Création d'un bouton pour envoyer le message
        self.send_button.pack(side=tk.LEFT, padx=5)  # Placement du bouton dans le cadre avec un espacement à gauche

        self.record_button = ttk.Button(self.input_frame, text="🎤", command=self.record_audio)  # Création d'un bouton pour enregistrer un mémo vocal
        self.record_button.pack(side=tk.LEFT, padx=5)  # Placement du bouton dans le cadre avec un espacement à gauche

        self.emoji_button = ttk.Button(self.input_frame, text="😎", command=self.show_emojis)  # Création d'un bouton pour afficher les emojis
        self.emoji_button.pack(side=tk.LEFT, padx=5)  # Placement du bouton dans le cadre avec un espacement à gauche

    def send_message(self):  # Méthode pour envoyer un message
        message = self.message_input.get("1.0", "end").strip()  # Récupération du message saisi dans la zone de texte
        if message:  # Vérification si le message n'est pas vide
            self.message_list.config(state=tk.NORMAL)  # Activation de la modification de la zone de texte
            self.message_list.insert(tk.END, f"You: {message}\n", "sent_message")  # Insertion du message dans la zone de texte
            self.message_list.config(state=tk.DISABLED)  # Désactivation de la modification de la zone de texte
            self.message_input.delete("1.0", tk.END)  # Effacement du contenu de la zone de saisie

    def record_audio(self):  # Méthode pour enregistrer un mémo vocal
        # Ajoutez ici le code pour enregistrer un mémo vocal
        pass  # Placeholder pour le code d'enregistrement audio

    def show_emojis(self):  # Méthode pour afficher les emojis
        # Ajoutez ici le code pour afficher les emojis
        pass  # Placeholder pour le code d'affichage des emojis

    def fetch_data_from_database(self, nom_du_salon):  # Méthode pour récupérer les données depuis la base de données
        try:  # Gestion des exceptions pour les erreurs de base de données
            connection = mariadb.connect(user='mounir-merzoudy',  # Connexion à la base de données avec les informations d'identification
                                     password='Mounir-1992',
                                     host='82.165.185.52',
                                     port=3306,
                                     database='mounir-merzoud_myDiscord')
            cursor = connection.cursor()  # Création d'un curseur pour exécuter des requêtes SQL

            sql = f"SELECT * FROM salon WHERE nom_du_salon = '{nom_du_salon}'"  # Requête SQL pour sélectionner les données du salon spécifié
            cursor.execute(sql)  # Exécution de la requête SQL
            rows = cursor.fetchall()  # Récupération de toutes les lignes de résultats

            for row in rows:  # Parcours des lignes de résultats
                # Traitez les données récupérées ici
                pass  # Placeholder pour le traitement des données récupérées

            cursor.close()  # Fermeture du curseur
            connection.close()  # Fermeture de la connexion à la base de données

        except mariadb.Error as e:  # Gestion des erreurs de base de données
            print(f"Erreur lors de la récupération des données depuis la base de données : {e}")

if __name__ == "__main__":  # Point d'entrée du programme
    root = tk.Tk()  # Création de la fenêtre principale
    app = SalonApp(root)  # Création de l'instance de l'application SalonApp avec la fenêtre principale comme parent
    app.fetch_data_from_database("sport")  # Appel de la méthode pour récupérer les données du salon "sport"
    root.mainloop()  # Lancement de la boucle principale pour afficher l'interface graphique
