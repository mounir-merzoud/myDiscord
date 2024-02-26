
import mariadb
import mysql.connector
from tkinter import *
from PIL import ImageTk

class User(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('790x850')
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
        self.usernameEntry.place(x=190, y=390)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>',self.user_enter)

        #self.frame1 = Frame(self, width=250, height=2,bg='firebrick1') 
        #self.frame1.place(x=250, y=460)

        self.passwordEntry = Entry(self, width=25, font=('Comic Sans MS', 11, 'bold'), bd=1.4, fg='navy', bg="light Sky Blue")
        self.passwordEntry.place(x=190, y=430)
        self.passwordEntry.insert(0, 'Mot de pass')
        self.passwordEntry.bind('<FocusIn>',self.password_enter)

        self.openeye = PhotoImage(file='images/openeye.png')
        self.eyeButton = Button(self, image=self.openeye, bd=0, activebackground='white', cursor='hand2',command=self.hide)
        self.eyeButton.place(x=410, y=430)

        self.forgetButton = Button(self, text='Mot de pass oublier ?', bd=0, activebackground='white',bg="light Sky Blue"
                            , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='navy', activeforeground='black')
        self.forgetButton.place(x=190, y=470)

        self.loginButton = Button(self, text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='navy'
                       , bg='light Sky Blue', activeforeground='white', activebackground='black', cursor='hand2',bd=2, width=25)
        self.loginButton.place(x=190, y=510)

        self.signupLabel = Label(self, text='Ne pas de compte ?', font=('Comic Sans MS',12,'bold'), fg='navy', bg="light Sky Blue")
        self.signupLabel.place(x=190, y=590)

        self.newaccountButton = Button(self, text='Inscréption', font=('Comic Sans MS', 10, 'bold underline'), fg='navy'
                           , bg='light Sky Blue', activeforeground='black', activebackground='white', cursor='hand2')
        self.newaccountButton.place(x=415, y=590)

        
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


