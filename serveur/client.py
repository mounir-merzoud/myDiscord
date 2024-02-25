import socket
import threading
import tkinter.scrolledtext
from tkinter import simpledialog, Tk, Label, Text, Button
import pymysql.cursors

HOST = "10.10.90.50"
PORT = 9090

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.msg = Tk()
        self.msg.withdraw()
        self.authenticate()

    def authenticate(self):
        self.username = simpledialog.askstring("Login", "Entrez votre nom d'utilisateur")
        self.password = simpledialog.askstring("Login", "Entrez votre mot de passe", show="*")
        
        # Connexion à la base de données MySQL
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='kamelia',
                                     database='mydiscord',
                                     cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # Recherche de l'utilisateur dans la base de données

                sql = "SELECT * FROM `users` WHERE `username`=%s AND `password`=%s"
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
        # Implémentez la logique du chat ici
        self.gui_done = False
        self.running = True
        gui_thread = threading.Thread(target=self.gui_loop)
        recevoir_thread = threading.Thread(target=self.recevoir)
        gui_thread.start()
        recevoir_thread.start()

    def gui_loop(self):
        self.win = Tk()
        self.win.config(bg="cyan")
        self.chat_label = Label(self.win, text="Chat", bg="cyan")
        self.chat_label.configure(font="arial 12")
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")
        self.msg_label = Label(self.win, text="Message", bg="cyan")
        self.msg_label.config(font="arial 12")
        self.msg_label.pack(padx=20, pady=5)
        self.saisit = Text(self.win, height=3)
        self.saisit.pack(padx=20, pady=5)
        self.btn_envoie = Button(self.win, text="Envoyer", command=self.ecrire)
        self.btn_envoie.config(font="arial 12")
        self.btn_envoie.pack(padx=20, pady=5)
        self.gui_done = True
        self.win.protocol("WM_DELETE_WINDOW", self.stop)
        self.win.mainloop()

    def ecrire(self):
        message = f"{self.username} : {self.saisit.get('1.0', 'end')}"
        self.saisit.delete('1.0', 'end')
        self.sock.send(message.encode("utf-8")) # Envoyer le message via le socket

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def recevoir(self):
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

            except ConnectionAbortedError:
                break
            except:
                print("Erreur")
                self.sock.close()
                break

if __name__ == "__main__":
    # Initialisation du client
    client = Client(HOST, PORT)
