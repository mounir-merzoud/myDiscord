import socket  
import threading  
import tkinter.scrolledtext  
from tkinter import simpledialog, Tk, Label, Text, Button, Toplevel, Frame, Entry, END
from tkinter import PhotoImage
from ttkthemes import ThemedStyle 
from PIL import Image, ImageTk 
import mariadb  

HOST = "10.10.95.89"
PORT = 9090

# Fonction pour enregistrer les messages dans un fichier
def enregistrer_message(message):
    with open("historique_chat.txt", "a") as file:
        file.write(message + "\n")

# Définition de la classe Client
class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.login_window = None  # Pour stocker la fenêtre de connexion
        self.openeye = None  # Pour stocker l'image de l'oeil
        self.start_login()
    
    def start_login(self):
        # Afficher la fenêtre de connexion
        self.login_window = Tk()
        self.login_window.geometry('990x660+50+50')
        self.login_window.resizable(0,0)
        self.login_window.title('Login Page')
        
        # Interface utilisateur de connexion
        bgImage=ImageTk.PhotoImage(file='images/bg.jpg')
        bgLabel=Label(self.login_window, image=bgImage)
        bgLabel.pack()
        
        heading=Label(self.login_window, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), bg='white', fg='firebrick1')
        heading.place(x=610, y=120)
        
        self.usernameEntry=Entry(self.login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.usernameEntry.place(x=580, y=200)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>', self.user_enter)
        
        frame1=Frame(self.login_window, width=250, height=2, bg='firebrick1') 
        frame1.place(x=580, y=222)
        
        self.passwordEntry=Entry(self.login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.passwordEntry.place(x=580, y=260)
        self.passwordEntry.insert(0, 'Mot de passe')
        self.passwordEntry.bind('<FocusIn>', self.password_enter)
        
        frame2=Frame(self.login_window, width=250, height=2, bg='firebrick1')
        frame2.place(x=580, y=282)
        
        self.openeye=PhotoImage(file='images/openeye.png')
        self.eyeButton=Button(self.login_window, image=self.openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=self.hide)
        self.eyeButton.place(x=800, y=255)
        
        forgetButton=Button(self.login_window, text='Mot de passe oublié ?', bd=0, bg='white', activebackground='white',
                            cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', activeforeground='black')
        forgetButton.place(x=715, y=295)
        
        loginButton=Button(self.login_window, text='Se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white', bg='firebrick1',
                           activeforeground='black', activebackground='white', cursor='hand2', bd=0, width=19, command=self.login)
        loginButton.place(x=578, y=350)
        
        # Create a clickable Google button
        google_logo=PhotoImage(file='images/google.png')
        googleButton=Button(self.login_window, image=google_logo, bd=0, bg='white', activebackground='white', cursor='hand2', command=self.google_login)
        googleButton.place(x=680, y=440)
        
        signupLabel=Label(self.login_window, text='Pas encore de compte ?', font=('Comic Sans MS',12,'bold'), fg='firebrick1', bg='white')
        signupLabel.place(x=575, y=500)
        
        newaccountButton=Button(self.login_window, text='Créer un compte', font=('Comic Sans MS', 9, 'bold underline'), fg='black',
                                bg='white', activeforeground='black', activebackground='white', cursor='hand2', bd=0, command=self.signup_page)
        newaccountButton.place(x=727, y=500)
        
        self.login_window.mainloop()

    def user_enter(self, event):
        if self.usernameEntry.get() == 'Nom ou Email':
            self.usernameEntry.delete(0, END)

    def password_enter(self, event):
        if self.passwordEntry.get() == 'Mot de passe':
            self.passwordEntry.delete(0, END)

    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

    # Function to be executed when Google button is clicked
    def google_login(self):
        # Add your code here to handle Google login
        print("Google login clicked")
    def signup_page(self):
        self.login_window.destroy()
        import userup

    # Function to be executed when "Se connecter" button is clicked
    def login(self):
        self.authenticate()
        self.login_window.destroy()  # Ferme la fenêtre de connexion

    # Méthode pour authentifier l'utilisateur
    def authenticate(self):
        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()
        
        connection = mariadb.connect(user='mounir-merzoudy', password='Mounir-1992', host='82.165.185.52',
                                    port=3306, database='mounir-merzoud_myDiscord')

        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM `user` WHERE `username`=%s AND `mot_de_passe`=%s"
                cursor.execute(sql, (self.username, self.password))
                user = cursor.fetchone()
                if user:
                    print("Authentification réussie.")
                    self.start_chat(cursor)  # Passer cursor comme argument
                    self.show_user_list(cursor)
                else:
                    print("Erreur d'authentification.")
        finally:
            connection.close()



    # Méthode pour démarrer le chat
    def start_chat(self, cursor):
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
    