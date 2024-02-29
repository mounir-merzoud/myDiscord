import tkinter as tk
import tkinter.messagebox as messagebox
import mariadb

class AjouterUnSalon:
    def __init__(self, parent):
        self.parent = parent

        # Cadre pour ajouter un nouveau salon
        self.frame_ajout_salon = tk.Frame(parent, padx=10, pady=10)
        self.frame_ajout_salon.pack()

        # Labels et champs de saisie pour les informations du nouveau salon
        self.label_nom_salon = tk.Label(self.frame_ajout_salon, text="Nom du salon :")
        self.label_nom_salon.grid(row=0, column=0, sticky="e")
        self.entry_nom_salon = tk.Entry(self.frame_ajout_salon)
        self.entry_nom_salon.grid(row=0, column=1)

        self.label_fichier_txt = tk.Label(self.frame_ajout_salon, text="Chemin du fichier .txt :")
        self.label_fichier_txt.grid(row=1, column=0, sticky="e")
        self.entry_fichier_txt = tk.Entry(self.frame_ajout_salon)
        self.entry_fichier_txt.grid(row=1, column=1)

        self.label_memo_wav = tk.Label(self.frame_ajout_salon, text="Chemin du fichier .wav :")
        self.label_memo_wav.grid(row=2, column=0, sticky="e")
        self.entry_memo_wav = tk.Entry(self.frame_ajout_salon)
        self.entry_memo_wav.grid(row=2, column=1)

        # Bouton pour ajouter un nouveau salon
        self.bouton_ajouter_salon = tk.Button(self.frame_ajout_salon, text="Ajouter Salon", command=self.ajouter_salon)
        self.bouton_ajouter_salon.grid(row=3, columnspan=2)

    # Fonction pour ajouter un nouveau salon à la base de données
    def ajouter_salon(self):
        nom_salon = self.entry_nom_salon.get()
        fichier_txt = self.entry_fichier_txt.get()
        memo_wav = self.entry_memo_wav.get()

        try:
            # Connexion à la base de données
            connection = mariadb.connect(
                user='mounir-merzoudy',
                password='Mounir-1992',
                host='82.165.185.52',
                port=3306,
                database='mounir-merzoud_myDiscord'
            )

            cursor = connection.cursor()

            # Requête SQL pour insérer un nouveau salon
            sql = "INSERT INTO salon (nom_du_salon, fichier_txt, memo_wav) VALUES (%s, %s, %s)"
            val = (nom_salon, fichier_txt, memo_wav)

            cursor.execute(sql, val)
            connection.commit()

            messagebox.showinfo("Succès", "Le salon a été ajouté avec succès.")

            # Fermeture de la connexion à la base de données
            cursor.close()
            connection.close()

        except mariadb.Error as error:
            print("Erreur lors de l'ajout du salon :", error)
            messagebox.showerror("Erreur", "Erreur lors de l'ajout du salon.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Gestion des salons")

# Utilisation de la classe AjouterUnSalon pour ajouter un salon
ajouter_salon_widget = AjouterUnSalon(root)

root.mainloop()
