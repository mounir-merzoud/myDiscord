import socket
import threading
import tkinter as Tk
from tkinter import simpledialog, Label, Text, Button, Toplevel, Frame, Entry, END
from tkinter import PhotoImage
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import mariadb

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.login_window = None
        self.openeye = None
        self.start_login()

    def start_login(self):
        self.login_window = Tk()
        self.login_window.geometry('990x660+50+50')
        self.login_window.resizable(0,0)
        self.login_window.title('Login Page')

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

    def google_login(self):
        print("Google login clicked")

    def signup_page(self):
        self.login_window.destroy()
        import userup

    def login(self):
        self.authenticate()
        self.login_window.destroy()

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
                    self.start_chat(cursor)
                    self.show_user_list(cursor)
                else:
                    print("Erreur d'authentification.")
        finally:
            connection.close()

    def start_chat(self, cursor):
        self.gui_done = False
        self.running = True
        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)
        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Chat App")

        self.left_frame = Frame(self.win, bg="blue", width=150)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)

        self.users_button = Button(self.left_frame, text="Utilisateurs", command=self.open_users_window, bg="red")
        self.users_button.pack(fill="x", pady=5)

        # Autres parties de l'interface de chat...

        self.win.mainloop()

    def open_users_window(self):
        pass

if __name__ == "__main__":
    HOST = "10.10.95.89"
    PORT = 9090
    client = Client(HOST, PORT)
