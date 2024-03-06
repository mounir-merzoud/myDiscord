import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
#from message import ChatApplication

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("MyChat")
        self.master.geometry("990x660+50+50")
        self.master.configure(bg="salmon")

        # Connexion à la base de données
        self.connection = mysql.connector.connect(user='mounir-merzoudy',
                                                  password='Mounir-1992',
                                                  host='82.165.185.52',
                                                  port=3306,
                                                  database='mounir-merzoud_myDiscord')
        
        # Barre de menu
        self.menu_bar = tk.Menu(self.master)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Paramètres")
        self.settings_menu.add_command(label="Changer de compte")
        self.settings_menu.add_separator()
        self.settings_menu.add_command(label="Déconnexion")
        self.menu_bar.add_cascade(label="Options", menu=self.settings_menu)

        self.master.config(menu=self.menu_bar)

        # Cadre principal
        self.main_frame = tk.Frame(self.master, bg="salmon")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Liste des salons à gauche
        self.channels_label = tk.Label(self.main_frame, text="Salons", bg="salmon")
        self.channels_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.channels_listbox = tk.Listbox(self.main_frame, bg="salmon", selectmode=tk.SINGLE)
        self.channels_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Ajouter des salons avec des emojis
        self.add_channel("Sport", "⚽")
        self.add_channel("Cuisine", "🍳")
        self.add_channel("Actualités", "📰")

        # Liste d'amis à droite
        self.friends_label = tk.Label(self.main_frame, text="Amis", bg="salmon")
        self.friends_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.friends_listbox = tk.Listbox(self.main_frame, bg="salmon")
        self.friends_listbox.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
        
        # Lier la fonction à l'événement de clic sur un ami dans la liste
        self.friends_listbox.bind("<Double-1>", self.open_chat_window)

        # Remplir la liste d'amis depuis la base de données
        self.populate_friends_list()

        # Liste des canaux au centre
        self.channels_treeview = ttk.Treeview(self.main_frame)
        self.channels_treeview.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="nsew")

        # Redimensionnement automatique des cellules du cadre principal
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        # Propriété pour stocker la fenêtre de chat actuelle
        self.chat_window = None

    def add_channel(self, name, emoji):
        self.channels_listbox.insert(tk.END, f"{emoji} {name}")

    def populate_friends_list(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT username FROM user")  
        users = cursor.fetchall()
        for user in users:
            self.friends_listbox.insert(tk.END, user[0])
        cursor.close()
        
    def open_chat_window(self, event):
        # Vérifiez d'abord si une fenêtre de chat est déjà ouverte
        if self.chat_window is not None:
            self.chat_window.destroy()

        # Obtenir l'ami sélectionné dans la liste
        selected_friend = self.friends_listbox.get(self.friends_listbox.curselection())

        # Créez une nouvelle fenêtre de chat
        self.chat_window = tk.Toplevel(self.master)
        self.chat_window.title(f"Chat avec {selected_friend}")
        
        # Instanciez la classe ChatApplication avec la nouvelle fenêtre
        app = ChatApplication(self.chat_window)

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()
        if self.chat_window is not None:
            self.chat_window.destroy()
        self.master.destroy()

def main():
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()