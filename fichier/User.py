import mariadb
import mysql.connector
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


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

        self.usernameEntry = Entry(self, width=27, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='navy',bg="light Sky Blue")
        self.usernameEntry.place(x=250, y=390)
        self.usernameEntry.insert(0, 'Nom ou Email')
        self.usernameEntry.bind('<FocusIn>',self.user_enter)

        self.passwordEntry = Entry(self, width=25, font=('Comic Sans MS', 11, 'bold'), bd=1.4, fg='navy', bg="light Sky Blue")
        self.passwordEntry.place(x=250, y=430)
        self.passwordEntry.insert(0, 'Mot de passe')
        self.passwordEntry.bind('<FocusIn>',self.password_enter)

        self.openeye = PhotoImage(file='images/openeye.png')
        self.eyeButton = Button(self, image=self.openeye, bd=0, activebackground='white', cursor='hand2',command=self.hide)
        self.eyeButton.place(x=470, y=430)

        self.forgetButton = Button(self, text='Mot de passe oublié ?', bd=0, activebackground='white',bg="light Sky Blue"
                            , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='navy', activeforeground='black')
        self.forgetButton.place(x=250, y=470)

        self.loginButton = Button(self, text='Se connecter', font=('Comic Sans MS', 16, 'bold'), fg='navy'
                       , bg='light Sky Blue', activeforeground='white', activebackground='black', cursor='hand2',bd=2, width=25, command=self.loginButtonClicked)
        self.loginButton.place(x=310, y=510)

        self.signupLabel = Label(self, text='Pas de compte ?', font=('Comic Sans MS',12,'bold'), fg='navy', bg="light Sky Blue")
        self.signupLabel.place(x=250, y=590)

        self.newaccountButton = Button(self, text='Inscription', font=('Comic Sans MS', 10, 'bold underline'), fg='navy'
                           , bg='light Sky Blue', activeforeground='black', activebackground='white', cursor='hand2')
        self.newaccountButton.place(x=455, y=590)

        # Connexion à la base de données:
        try:
            self.connection = mariadb.connect(user='mounir-merzoudy',
                                     password='Mounir-1992',
                                     host='82.165.185.52',
                                     port=3306,
                                     database='mounir-merzoud_myDiscord')
            if self.connection.is_connected():
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
        if self.passwordEntry.get() == 'Mot de passe':
            self.passwordEntry.delete(0, END)        

    def loginButtonClicked(self):
        username = self.usernameEntry.get()
        mot_de_passe = self.passwordEntry.get()
        cursor = self.connection.cursor()

        # Exécuter la requête pour vérifier les informations de connexion
        cursor.execute("SELECT * FROM user WHERE nom = %s AND mot_de_passe = %s", (username, mot_de_passe))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Connexion réussie", "Vous êtes connecté!")
        else:
            messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect!")

        cursor.close()

    # Function to be executed when Google button is clicked
    def google_login(self):
        # Add your code here to handle Google login
        print("Google login clicked")

if __name__ == "__main__":
    app = User()
    app.mainloop()
