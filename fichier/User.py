import mariadb
import mysql.connector
from tkinter import *
from PIL import ImageTk

class User(Tk):
    def __init__(self):
        super().__init__()

    
        self.geometry('990x860+50+50')
        self.resizable(0.5, 0.5)
        self.title('Login Page')

        # Charger l'image de fond
        self.bgImage = ImageTk.PhotoImage(file='images/Design sans titre.png')

        # Créer un conteneur Frame pour l'image de fond et la centrer
        self.bgContainer = Frame(self, width=990, height=800)
        self.bgContainer.pack_propagate(0)  # Empêcher le redimensionnement du cadre
        self.bgContainer.pack(fill=BOTH, expand=YES)

        # Ajouter l'image de fond dans le conteneur Frame
        self.bgLabel = Label(self.bgContainer, image=self.bgImage)
        self.bgLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.bgLabel = Label(self, image=self.bgImage)
        self.bgLabel.pack()

        #self.heading = Label(self, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), fg='navy',bg="light Sky Blue")
        #self.heading.place(x=380, y=360)

        self.usernameEntry = Entry(self, width=27, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='navy',bg="light Sky Blue")
        self.usernameEntry.place(x=250, y=430)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>',self.user_enter)

        #self.frame1 = Frame(self, width=250, height=2,bg='firebrick1') 
        #self.frame1.place(x=250, y=460)

        self.passwordEntry = Entry(self, width=25, font=('Comic Sans MS', 11, 'bold'), bd=1.4, fg='navy', bg="light Sky Blue")
        self.passwordEntry.place(x=250, y=490)
        self.passwordEntry.insert(0, 'Mot de pass')
        self.passwordEntry.bind('<FocusIn>',self.password_enter)

   

        self.openeye = PhotoImage(file='images/openeye.png')
        self.eyeButton = Button(self, image=self.openeye, bd=0, activebackground='white', cursor='hand2',command=self.hide)
        self.eyeButton.place(x=470, y=490)

        self.forgetButton = Button(self, text='Mot de pass oublier ?', bd=0, activebackground='white',bg="light Sky Blue"
                            , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='navy', activeforeground='black')
        self.forgetButton.place(x=250, y=550)

        self.loginButton = Button(self, text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='navy'
                       , bg='light Sky Blue', activeforeground='white', activebackground='black', cursor='hand2',bd=2, width=25)
        self.loginButton.place(x=310, y=600)

        self.signupLabel = Label(self, text='Ne pas de compte ?', font=('Comic Sans MS',12,'bold'), fg='navy', bg="light Sky Blue")
        self.signupLabel.place(x=250, y=700)

        self.newaccountButton = Button(self, text='Inscréption', font=('Comic Sans MS', 10, 'bold underline'), fg='navy'
                           , bg='light Sky Blue', activeforeground='black', activebackground='white', cursor='hand2')
        self.newaccountButton.place(x=455, y=698)

        
        # Connexion à la base de données:
        try:
            connection = mysql.connector.connect(
                host="plesk.students-laplateforme.io",  # Adresse de votre serveur MySQL
                port="3306",  # Port par défaut de MySQL
                user="mounir",  # Nom d'utilisateur de la base de données MySQL
                password="mounir-1992",  # Mot de passe de la base de données MySQL
                database="kamelia-mohamdi_mydiscord"
            )    
            if connection.is_connected():
                print("Connexion à la base de données réussie!")

        except mariadb.Error as e:
            print(f"Erreur lors de la connexion à la base de données MySQL: {e}")

    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

    def user_enter(self, event):
        if self.usernameEntry.get() == 'Nom ou Email':
            self.usernameEntry.delete(0, END)

    def password_enter(self, event):
        if self.passwordEntry.get() == 'Mot de pass':
            self.passwordEntry.delete(0, END)        

    # Function to be executed when Google button is clicked
    def google_login(self):
        # Add your code here to handle Google login
        print("Google login clicked")

if __name__ == "__main__":
    app = User()
    app.mainloop()
"""
from tkinter import *
from PIL import ImageTk

class User(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('990x660+50+50')
        self.resizable(0,0)
        self.title('Login Page')

        self.bgImage = ImageTk.PhotoImage(file='images/background.jpg')

        self.bgLabel = Label(self, image=self.bgImage)
        self.bgLabel.pack()

        self.heading = Label(self, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), bg='white', fg='firebrick1')
        self.heading.place(x=610, y=50)

        self.usernameEntry = Entry(self, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.usernameEntry.place(x=580, y=130)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>',self.user_enter)

        self.frame1 = Frame(self, width=250, height=2,bg='firebrick1') 
        self.frame1.place(x=580, y=152)

        self.passwordEntry = Entry(self, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
        self.passwordEntry.place(x=580, y=190)
        self.passwordEntry.insert(0, 'Mot de pass')
        self.passwordEntry.bind('<FocusIn>',self.password_enter)

        self.frame2 = Frame(self, width=250, height=2,bg='firebrick1')
        self.frame2.place(x=580, y=212)

        self.openeye = PhotoImage(file='images/openeye.png')
        self.eyeButton = Button(self, image=self.openeye, bd=0, bg='white', activebackground='white', cursor='hand2',command=self.hide)
        self.eyeButton.place(x=800, y=180)

        self.forgetButton = Button(self, text='Mot de pass oublier ?', bd=0, bg='white', activebackground='white'
                            , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', activeforeground='black')
        self.forgetButton.place(x=715, y=225)

        self.loginButton = Button(self, text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white'
                       , bg='firebrick1', activeforeground='black', activebackground='white', cursor='hand2',bd=0, width=19)
        self.loginButton.place(x=578, y=270)

        self.orLabel = Label(self, text='---------- OR ----------', font=('Comic Sans MS',16), fg='firebrick1', bg='white')
        self.orLabel.place(x=583, y=330)

        # Create a clickable Google button
        self.google_logo = PhotoImage(file='images/google.png')
        self.googleButton = Button(self, image=self.google_logo, bd=0, bg='white', activebackground='white', cursor='hand2', command=self.google_login)
        self.googleButton.place(x=680, y=380)

        self.signupLabel = Label(self, text='Ne pas de compte ?', font=('Comic Sans MS',12,'bold'), fg='pale violet red', bg='white')
        self.signupLabel.place(x=575, y=440)

        self.newaccountButton = Button(self, text='Create New', font=('Comic Sans MS', 11, 'bold underline'), fg='black'
                           , bg='white', activeforeground='black', activebackground='white', cursor='hand2',bd=0)
        self.newaccountButton.place(x=727, y=435)

    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

    def user_enter(self, event):
        if self.usernameEntry.get() == 'Nom ou Email':
            self.usernameEntry.delete(0, END)

    def password_enter(self, event):
        if self.passwordEntry.get() == 'Mot de pass':
            self.passwordEntry.delete(0, END)        

    # Function to be executed when Google button is clicked
    def google_login(self):
        # Add your code here to handle Google login
        print("Google login clicked")

if __name__ == "__main__":
    app = User()
    app.mainloop()
"""    

