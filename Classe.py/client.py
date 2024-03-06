import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import mariadb
from userup import UserUp
import re
import json
import pyaudio
import wave

PRIMARY_COLOR = "#FA8072"  # Salmon
SECONDARY_COLOR = "#FFA07A"  # Salmon plus foncé
BACKGROUND_COLOR = "#FDF5E6"  # Couleur salmon claire
TEXT_COLOR = "#000000"  # Noir
BUTTON_COLOR = "#E9967A"  # Salmon3

HOST = "10.10.106.14"
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
        self.users = []  # Liste des utilisateurs connectés
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        gui_thread.start()
        receive_thread.start()
# Méthode pour boucler l'interface utilisateur
    def gui_loop(self):
        self.win = tk.Tk()
        self.win.geometry("800x600")  # Définir les dimensions de la fenêtre principale
        self.win.title("Chat App")
        self.win.configure(bg=BACKGROUND_COLOR)

        # Création du cadre bleu à gauche
        self.left_frame = tk.Frame(self.win, bg=BACKGROUND_COLOR, width=150)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        # Création du cadre à droite
        self.right_frame = tk.Frame(self.win, bg=BACKGROUND_COLOR, width=150)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        # Boutons dans le cadre bleu
        ttk.Button(self.left_frame, text="Utilisateurs", style="Discord.TButton", command=self.show_users).pack(fill="x", pady=5)
        ttk.Button(self.left_frame, text="Option", style="Discord.TButton").pack(fill="x", pady=5)
        ttk.Button(self.left_frame, text="Informations", style="Discord.TButton").pack(fill="x", pady=5)
        ttk.Button(self.left_frame, text="Déconnexion", style="Discord.TButton", command=self.logout_user).pack(fill="x", pady=5)

        # Label pour le salon
        tk.Label(self.right_frame, text="SALON", bg=PRIMARY_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14, "bold")).pack(padx=20, pady=5)

        # Zone de texte pour afficher les messages
        self.text_area = scrolledtext.ScrolledText(self.right_frame, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12))
        self.text_area.pack(fill="both", expand=True, padx=20, pady=5)
        self.text_area.config(state="disabled")

        # Frame pour la saisie de texte et le bouton
        input_button_frame = tk.Frame(self.right_frame, bg=BACKGROUND_COLOR)
        input_button_frame.pack(side="bottom", fill="x", padx=20, pady=5)

        # Label pour le champ de message
        tk.Label(input_button_frame, text="Message", bg=PRIMARY_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12, "bold")).pack(side="left", padx=(20, 5))

        # Zone de saisie de texte
        self.input_field = tk.Text(input_button_frame, height=3, bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12))
        self.input_field.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # Bouton pour envoyer le message
<<<<<<< HEAD:serveur/client.py
        ttk.Button(input_button_frame, text="envoye", style="Discord.TButton", command=self.send_message).pack(side="left", padx=(0, 10), pady=(0, 10))
        ttk.Button(input_button_frame, text="Emoji", style="Discord.TButton", command=self.send_emoji).pack(side="left", padx=(0, 10), pady=(0, 10))
        ttk.Button(input_button_frame, text="Enregistrer Message Vocal", style="Discord.TButton", command=self.record_voice_message).pack(side="left", padx=(0, 10), pady=(0, 10))
=======
        ttk.Button(input_button_frame, text="➡️", style="Discord.TButton", command=self.send_message).pack(side="left", padx=(0, 20))
>>>>>>> fd97029fdae30ea704739e5d83967f74ed37ba03:Classe.py/client.py

        # Bouton pour sélectionner un emoji avec un emoji
        ttk.Button(input_button_frame, text="😃", style="Discord.TButton", command=self.send_emoji).pack(side="left", padx=(4, 30))

        # Bouton pour enregistrer un message vocal avec un emoji
        ttk.Button(input_button_frame, text="🎙️", style="Discord.TButton", command=self.record_voice_message).pack(side="left", padx=(10, 20))
        # Liste des utilisateurs connectés
        self.user_listbox = tk.Listbox(self.left_frame, bg=PRIMARY_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12))
        self.user_listbox.pack(fill="both", expand=True, padx=20, pady=5)

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

    def send_emoji(self):
        try:
            with open("imoji.json", "r", encoding="utf-8") as file:  # Correction du nom du fichier
                emojis_data = json.load(file)
        except Exception as e:
            print("Une erreur s'est produite lors du chargement du fichier imoji.json :", e)
            return
        
        emojis = emojis_data["emojis"]

        # Création d'une nouvelle fenêtre pour la sélection d'emoji
        emoji_window = tk.Toplevel(self.win)
        emoji_window.title("Sélectionnez un emoji")

        # Ajout de boutons pour chaque emoji dans la fenêtre
        for emoji in emojis:
            ttk.Button(emoji_window, text=emoji, command=lambda e=emoji: self.send_selected_emoji(e)).pack(padx=5, pady=5)

    def send_selected_emoji(self, emoji):
        self.input_field.insert("end", emoji)

    def show_users(self):
        connection = mariadb.connect(user='mounir-merzoudy',
                                     password='Mounir-1992',
                                     host='82.165.185.52',
                                     port=3306,
                                     database='mounir-merzoud_myDiscord')

        try:
            with connection.cursor() as cursor:
                sql = "SELECT username FROM `user`"
                cursor.execute(sql)
                users = cursor.fetchall()

                # Effacer la liste des utilisateurs actuels
                self.user_listbox.delete(0, tk.END)

                # Mettre à jour la liste des utilisateurs
                for user in users:
                    self.users.append(user[0])
                    self.user_listbox.insert(tk.END, user[0])

        finally:
            connection.close()

    def send_message(self):
        message = f"{self.username} : {self.input_field.get('1.0', 'end')}"
        # Recherche des mentions d'utilisateurs
        mentions = re.findall(r"@(\w+)", message)
        # Remplacer les mentions par des tags spéciaux
        for mention in mentions:
            if mention in self.users:
                message = message.replace(f"@{mention}", f"<@{mention}>")
            else:
                messagebox.showerror("Erreur", f"L'utilisateur '{mention}' n'est pas connecté.")
                return

        self.input_field.delete('1.0', 'end')
        self.sock.send(message.encode("utf-8"))
        enregistrer_message(message)

    def record_voice_message(self):
        frames = []
        try:
            print("Enregistrement vocal commencé...")
            while True:
                data = self.stream.read(1024)
                frames.append(data)
        except KeyboardInterrupt:
            print("Enregistrement vocal terminé.")
            filename = "voice_message.wav"
            wf = wave.open(filename, 'wb')
            wf.setnchannels(1)
            wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            wf.setframerate(44100)
            wf.writeframes(b''.join(frames))
            wf.close()

            # Envoyer le fichier audio au serveur ou effectuer toute autre action nécessaire

    def stop(self):
            self.running = False
            self.win.destroy()
            self.sock.close()
            exit(0)

    def receive(self):
<<<<<<< HEAD:serveur/client.py
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
=======
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
>>>>>>> fd97029fdae30ea704739e5d83967f74ed37ba03:Classe.py/client.py

if __name__ == "__main__":
    # Initialisation du client
    client = Client(HOST, PORT)
