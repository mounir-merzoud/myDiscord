import socket  
import threading  
import tkinter.scrolledtext  
from tkinter import simpledialog, Tk, Label, Text, Button, Toplevel, Frame
from ttkthemes import ThemedStyle  
import mariadb  

HOST = "10.10.101.10"
PORT = 9090

# Fonction pour enregistrer les messages dans un fichier
def enregistrer_message(message):
    with open("historique_chat.txt", "a") as file:
        file.write(message + "\n")

# Définition de la classe Client
class Client:
    def __init__(self, host, port, username, password):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.msg = Tk()
        self.msg.withdraw()
        self.username = username  # Stocker le nom d'utilisateur dans un attribut de classe
        self.password = password 
        self.authenticate()


    def authenticate(self):
        
        connection = mariadb.connect(user='mounir-merzoudy',
                                     password='Mounir-1992',
                                     host='82.165.185.52',
                                     port=3306,
                                     database='mounir-merzoud_myDiscord')

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `user` WHERE `username`=%s AND `mot_de_passe`=%s"
                cursor.execute(sql, (self.username, self.password))
                user = cursor.fetchone()
                if user:
                    print("Authentification réussie.")
                    self.start_chat()
                    self.show_user_list(cursor)
                else:
                    print("Erreur d'authentification.")
        finally:
            connection.close()
# Méthode pour commencer le chat
    def start_chat(self):
        self.gui_done = False  
        self.running = True  
        gui_thread = threading.Thread(target=self.gui_loop)  
        receive_thread = threading.Thread(target=self.receive)  
        gui_thread.start()  
        receive_thread.start()  

    # Méthode pour boucler l'interface utilisateur
    def gui_loop(self):
        self.win = Tk()
        self.win.geometry("600x400")  # Définir les dimensions de la fenêtre principale
        self.win.title("Chat App")

        # Création du cadre bleu à gauche
        self.left_frame = Frame(self.win, bg="blue", width=150)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        # Boutons dans le cadre bleu
        self.users_button = Button(self.left_frame, text="Utilisateurs", command=self.open_users_window, bg="red")
        self.users_button.pack(fill="x", pady=5)

        self.option_button = Button(self.left_frame, text="Option", command=self.open_option_window, bg="red")
        self.option_button.pack(fill="x", pady=5)

        self.info_button = Button(self.left_frame, text="Informations", command=self.open_info_window, bg="red")
        self.info_button.pack(fill="x", pady=5)

        self.logout_button = Button(self.left_frame, text="Déconnexion", command=self.logout, bg="red")
        self.logout_button.pack(fill="x", pady=5)

        

        # Création du style thématisé
        style = ThemedStyle(self.win)
        style.set_theme("equilux")  # Appliquer le thème equilux
    
        # Label pour le salon
        self.chat_label = Label(self.win, text="SALON")
        self.chat_label.configure(font="Arial 12", background=style.lookup('TLabel', 'background'), foreground=style.lookup('TLabel', 'foreground'))
        self.chat_label.pack(padx=20, pady=5)

        # Zone de texte pour afficher les messages
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        # Label pour le champ de message
        self.msg_label = Label(self.win, text="Message")
        self.msg_label.configure(font="Arial 12", background=style.lookup('TLabel', 'background'), foreground=style.lookup('TLabel', 'foreground'))
        self.msg_label.pack(padx=20, pady=5)
# Champ de texte pour entrer le message
        self.input_field = Text(self.win, height=3)
        self.input_field.pack(padx=20, pady=5)

        # Bouton pour envoyer le message
        self.send_button = Button(self.win, text="Envoyer", command=self.send_message)
        self.send_button.configure(font="Arial 12", background="#0000FF", foreground="white")
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop) 

        # Charger et afficher le contenu du fichier historique_chat.txt
        with open("historique_chat.txt", "r") as file:
            historique_content = file.read()
            self.text_area.config(state="normal")
            self.text_area.insert("end", historique_content)
            self.text_area.yview("end")
            self.text_area.config(state="disabled")

        self.win.mainloop()  

   

    # Méthode pour envoyer un message
    def send_message(self):
        message = f"{self.username} : {self.input_field.get('1.0', 'end')}"
        self.input_field.delete('1.0', 'end')
        self.sock.send(message.encode("utf-8"))  
        enregistrer_message(message)  

    # Méthode pour arrêter le client
    def stop(self):
        self.running = False  
        self.win.destroy()  
        self.sock.close()  
        exit(0)
# Méthode pour recevoir des messages
    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)  
                if message == b'surnom':
                    self.sock.send(self.username.encode("utf-8"))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert("end", message.decode())
                        self.text_area.yview("end")
                        self.text_area.config(state="disabled")
                        enregistrer_message(message.decode())  
            except ConnectionAbortedError:
                break  
            except:
                print("Erreur")  
                self.sock.close()  
                break  

    # Méthode pour afficher la liste des utilisateurs dans une fenêtre séparée
    def show_user_list(self, cursor):
        user_list_window = Toplevel()
        user_list_window.title("Liste des utilisateurs")
        user_list_window.geometry("300x300")  # Définir les dimensions de la fenêtre de la liste des utilisateurs

        # Récupérer la liste des utilisateurs depuis la base de données
        cursor.execute("SELECT username FROM user")
        users = cursor.fetchall()

        # Afficher les utilisateurs dans un tableau
        for i, user in enumerate(users, start=1):
            if user[0] != self.username:  # Ne pas afficher l'utilisateur connecté lui-même
                user_label = Label(user_list_window, text=user[0])
                user_label.grid(row=i, column=0, padx=10, pady=5)

    # Méthodes pour ouvrir les fenêtres des différentes fonctionnalités
    def open_users_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre des utilisateurs
    
    def open_option_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre des options
    
    def open_info_window(self):
        pass  # Remplir cette méthode pour afficher la fenêtre d'informations

    def logout(self):
        pass  # Remplir cette méthode pour gérer la déconnexion

if __name__ == "__main__":
    # Initialisation du client
    client = Client(HOST, PORT)
    