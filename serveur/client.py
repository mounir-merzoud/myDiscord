import socket  
import threading  
import tkinter.scrolledtext  
from tkinter import Tk, Label, Text, Button, Toplevel, Frame
from ttkthemes import ThemedStyle 
import mariadb  
from userup import UserUp

HOST = "10.10.104.142"
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
        self.username = username 
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
                else:
                    print("Erreur d'authentification.")
        finally:
            connection.close()

    def start_chat(self):
        self.gui_done = False  
        self.running = True  
        gui_thread = threading.Thread(target=self.gui_loop)  
        receive_thread = threading.Thread(target=self.receive)  
        gui_thread.start()  
        receive_thread.start()  

    # Méthode pour boucler l'interface utilisateur
    # Méthode pour boucler l'interface utilisateur
    def gui_loop(self):
        self.win = Tk()
        self.win.geometry("600x400")  # Définir les dimensions de la fenêtre principale
        self.win.title("Chat App")

        # Création du cadre bleu à gauche
        self.left_frame = Frame(self.win, bg="#34495e", width=150)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        self.right_frame = Frame(self.win, bg="#34495e", width=150)
        self.right_frame.pack(side="right", fill="y", padx=20, pady=20)

        # Appliquer le thème à droite
        style_right = ThemedStyle(self.right_frame)
        style_right.set_theme("equilux")

        # Boutons dans le cadre bleu
        Button(self.left_frame, text="Utilisateurs", bg="salmon", fg="white", width=15).pack(fill="x", pady=5)
        Button(self.left_frame, text="Option", bg="salmon", fg="white", width=15).pack(fill="x", pady=5)
        Button(self.left_frame, text="Informations", bg="salmon", fg="white", width=15).pack(fill="x", pady=5)
        Button(self.left_frame, text="Déconnexion", bg="salmon", fg="white", width=15, command=self.logout_user).pack(fill="x", pady=5)

        # Création du style thématisé
        style = ThemedStyle(self.win)
        style.set_theme("equilux")  # Appliquer le thème equilux

        # Label pour le salon
        Label(self.win, text="SALON", bg="#34495e", fg="white").pack(padx=20, pady=5)

        # Zone de texte pour afficher les messages
        self.text_area = tkinter.scrolledtext.ScrolledText(self.win, bg="salmon")
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        # Label pour le champ de message
        Label(self.win, text="Message", bg="#34495e", fg="white").pack(padx=20, pady=5)
        self.input_field = Text(self.win, height=3, bg="salmon")
        self.input_field.pack(padx=20, pady=5)

        # Bouton pour envoyer le message
        Button(self.win, text="Envoyer", command=self.send_message, bg="salmon", fg="white").pack(padx=20, pady=5)

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
    def logout_user(self):
        self.win.destroy()  
        self.sock.close()  
        UserUp()
if __name__ == "__main__":
    # Initialisation du client
    client = Client(HOST, PORT)


    