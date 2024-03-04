import tkinter as tk
import mariadb

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("MyChat")
        self.master.configure(bg="salmon")

        # Dimensions spécifiques pour chaque cadre
        self.channel_frame_width = 300
        self.messages_frame_width = 400
        self.users_frame_width = 300

        # Connexion à la base de données
        self.connection = mariadb.connect(user='mounir-merzoudy',
                                          password='Mounir-1992',
                                          host='82.165.185.52',
                                          port=3306,
                                          database='mounir-merzoud_myDiscord')

        # Cadre principal
        self.main_frame = tk.Frame(self.master, bg="salmon")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Liste des salons à gauche
        self.channel_frame = tk.Frame(self.main_frame, bg="salmon", width=self.channel_frame_width)
        self.channel_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        self.channels_label = tk.Label(self.channel_frame, text="Salons", bg="salmon")
        self.channels_label.pack()

        self.channels_listbox = tk.Listbox(self.channel_frame, bg="salmon", selectmode=tk.SINGLE)
        self.channels_listbox.pack(fill=tk.BOTH, expand=True)

        # Charger la liste des salons depuis la base de données
        self.load_channels()

        self.selected_channel = None  # Pour stocker le salon sélectionné

        # Cadre pour afficher les messages
        self.messages_frame = tk.Frame(self.main_frame, bg="white", width=self.messages_frame_width)
        self.messages_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Cadre pour afficher la liste des utilisateurs
        self.users_frame = tk.Frame(self.main_frame, bg="lightblue", width=self.users_frame_width)
        self.users_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Zone de saisie des messages
        self.entry_frame = tk.Frame(self.main_frame, bg="salmon")
        self.entry_frame.pack(fill=tk.X)

        self.message_entry = tk.Entry(self.entry_frame, bg="white")
        self.message_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        send_button = tk.Button(self.entry_frame, text="Envoyer", bg="lightblue", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

        # Lier la sélection d'un canal à la fonction de mise à jour des messages
        self.channels_listbox.bind("<<ListboxSelect>>", self.update_messages)

        # Charger la liste des utilisateurs
        self.load_users()

    def load_channels(self):
        # Charger les salons depuis la base de données
        cursor = self.connection.cursor()
        cursor.execute("SELECT nom FROM salon")
        salons = cursor.fetchall()
        for salon in salons:
            self.channels_listbox.insert(tk.END, salon[0])
        cursor.close()

    def send_message(self):
        if self.selected_channel is not None:
            message = self.message_entry.get()

            # Afficher le message dans le cadre des messages
            message_label = tk.Label(self.messages_frame, text=message, bg="white")
            message_label.pack(anchor="w")

            # Enregistrer le message dans le fichier correspondant au salon
            with open(f"{self.selected_channel}.txt", "a") as file:
                file.write(message + "\n")

            # Effacer la zone de saisie
            self.message_entry.delete(0, tk.END)

    def update_messages(self, event):
        selected_index = self.channels_listbox.curselection()
        if selected_index:
            self.selected_channel = self.channels_listbox.get(selected_index)
            self.messages_frame.destroy()
            self.messages_frame = tk.Frame(self.main_frame, bg="white", width=self.messages_frame_width)
            self.messages_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.load_messages()

    def load_messages(self):
        # Charger les messages depuis le fichier correspondant au salon sélectionné
        if self.selected_channel:
            try:
                with open(f"{self.selected_channel}.txt", "r") as file:
                    for line in file:
                        message_label = tk.Label(self.messages_frame, text=line.strip(), bg="white")
                        message_label.pack(anchor="w")
            except FileNotFoundError:
                pass

    def load_users(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT username FROM user")
        users = cursor.fetchall()
        for user in users:
            # Créer une étiquette cliquable pour chaque utilisateur
            user_label = tk.Label(self.users_frame, text=user[0], bg="lightblue", cursor="hand2")
            user_label.bind("<Button-1>", lambda event, user=user[0]: self.start_private_chat(user))
            user_label.pack(anchor="w")
        cursor.close()

    def start_private_chat(self, user):
        # Code pour démarrer une discussion privée avec l'utilisateur sélectionné
        print(f"Démarrer une discussion privée avec {user}")

def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
