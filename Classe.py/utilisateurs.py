import tkinter as tk
import mariadb

class UserListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Liste des utilisateurs")
        self.create_user_list()

    def create_user_list(self):
        # Connexion à la base de données
        try:
            connection = mariadb.connect(
                user='mounir-merzoudy',
                password='Mounir-1992',
                host='82.165.185.52',
                port=3306,
                database='mounir-merzoud_myDiscord'
            )
            cursor = connection.cursor()

            # Exécution de la requête pour récupérer les utilisateurs
            cursor.execute("SELECT id, username, email FROM user")
            users = cursor.fetchall()

            # Afficher les utilisateurs sous forme de boutons
            for user in users:
                user_button = tk.Button(self.root, text=user[1], command=lambda u=user: self.show_user_info(u))
                user_button.pack()

            connection.close()

        except mariadb.Error as e:
            print(f"Erreur de connexion à la base de données: {e}")

    def show_user_info(self, user):
        # Afficher les informations de l'utilisateur
        print("ID:", user[0])
        print("Nom d'utilisateur:", user[1])
        print("Email:", user[2])

if __name__ == "__main__":
    root = tk.Tk()
    app = UserListApp(root)
    root.mainloop()
