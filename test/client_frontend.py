import tkinter as tk
from tkinter import PhotoImage
from client_backend import ClientBackend

HOST = "10.10.95.89"
PORT = 9090

class ClientFrontend:
    def __init__(self):
        self.client_backend = ClientBackend(HOST, PORT)
        self.create_login_window()

    def create_login_window(self):
        self.login_window = tk.Tk()
        self.login_window.geometry('990x660+50+50')
        self.login_window.resizable(0,0)
        self.login_window.title('Login Page')
        
        # Interface utilisateur de connexion
        bgImage=PhotoImage(file='images/bg.jpg')
        bgLabel=tk.Label(self.login_window, image=bgImage)
        bgLabel.pack()
        
        heading=tk.Label(self.login_window, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), bg='white', fg='firebrick1')
        heading.place(x=610, y=120)
        
        self.usernameEntry=tk.Entry(self.login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.usernameEntry.place(x=580, y=200)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>', self.user_enter)
        
        frame1=tk.Frame(self.login_window, width=250, height=2, bg='firebrick1') 
        frame1.place(x=580, y=222)
        
        self.passwordEntry=tk.Entry(self.login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.passwordEntry.place(x=580, y=260)
        self.passwordEntry.insert(0, 'Mot de passe')
        self.passwordEntry.bind('<FocusIn>', self.password_enter)
        
        frame2=tk.Frame(self.login_window, width=250, height=2, bg='firebrick1')
        frame2.place(x=580, y=282)
        
        self.openeye=PhotoImage(file='images/openeye.png')
        self.eyeButton=tk.Button(self.login_window, image=self.openeye, bd=0, bg='white', activebackground='white', cursor='hand2', command=self.hide)
        self.eyeButton.place(x=800, y=255)
        
        forgetButton=tk.Button(self.login_window, text='Mot de passe oublié ?', bd=0, bg='white', activebackground='white',
                            cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', activeforeground='black')
        forgetButton.place(x=715, y=295)
        
        loginButton=tk.Button(self.login_window, text='Se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white', bg='firebrick1',
                           activeforeground='black', activebackground='white', cursor='hand2', bd=0, width=19, command=self.client_backend.login)
        loginButton.place(x=578, y=350)
        
        # Create a clickable Google button
        google_logo=PhotoImage(file='images/google.png')
        googleButton=tk.Button(self.login_window, image=google_logo, bd=0, bg='white', activebackground='white', cursor='hand2', command=self.client_backend.google_login)
        googleButton.place(x=680, y=440)
        
        signupLabel=tk.Label(self.login_window, text='Pas encore de compte ?', font=('Comic Sans MS',12,'bold'), fg='firebrick1', bg='white')
        signupLabel.place(x=575, y=500)
        
        newaccountButton=tk.Button(self.login_window, text='Créer un compte', font=('Comic Sans MS', 9, 'bold underline'), fg='black',
                                bg='white', activeforeground='black', activebackground='white', cursor='hand2', bd=0, command=self.client_backend.signup_page)
        newaccountButton.place(x=727, y=500)
        
        self.login_window.mainloop()

    def user_enter(self, event):
        if self.usernameEntry.get() == 'Nom ou Email':
            self.usernameEntry.delete(0, tk.END)

    def password_enter(self, event):
        if self.passwordEntry.get() == 'Mot de passe':
            self.passwordEntry.delete(0, tk.END)

    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

if __name__ == "__main__":
    client_frontend = ClientFrontend()
