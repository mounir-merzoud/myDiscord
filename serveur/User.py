from tkinter import *
from PIL import ImageTk

class User(Tk):
    def __init__(self):
        super().__init__()

    def create_gui(self):
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

        self.usernameEntry = Entry(self, width=27, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='navy',bg="light Sky Blue")
        self.usernameEntry.place(x=190, y=390)
        self.usernameEntry.insert(0, 'Nom de utilisateur')
        self.usernameEntry.bind('<FocusIn>',self.user_enter)

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

        self.loginButton = Button(self, text='Se connecter', font=('Comic Sans MS', 16, 'bold'), fg='navy'
                       , bg='light Sky Blue', activeforeground='white', activebackground='black', cursor='hand2',bd=2, width=25, command=self.login)
        self.loginButton.place(x=190, y=510)

        self.newaccountButton = Button(self, text='Inscription', font=('Comic Sans MS', 16, 'bold'), fg='navy'
                       , bg='light Sky Blue', activeforeground='white', activebackground='black', cursor='hand2',bd=2, width=25)
        self.newaccountButton.place(x=190, y=590)

    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        self.eyeButton.config(command=self.hide)

    def user_enter(self, event=None):
        if self.usernameEntry.get() == 'Nom de utilisateur':
            self.usernameEntry.delete(0, END)

    def password_enter(self, event=None):
        if self.passwordEntry.get() == 'Mot de pass':
            self.passwordEntry.delete(0, END) 

    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if username == "votre_nom_utilisateur" and password == "votre_mot_de_passe":
            print("Authentification réussie !")
            # Vous pouvez fermer cette fenêtre et ouvrir la fenêtre principale de chat
        else:
            print("Nom d'utilisateur ou mot de passe incorrect !")

if __name__ == "__main__":
    app = User()
    app.create_gui()
    app.mainloop()



    def hide(self):
        self.openeye.config(file='images/closeye.png')
        self.passwordEntry.config(show='*')
        self.eyeButton.config(command=self.show)

    def show(self):
        self.openeye.config(file='images/openeye.png')
        self.passwordEntry.config(show='')
        
        self.eyeButton.config(command=self.hide)

    def user_enter(self):
        if self.usernameEntry.get() == 'Nom ou Email':
            self.usernameEntry.delete(0, END)

    

    def password_enter(self):
        if self.passwordEntry.get() == 'Mot de pass':
            self.passwordEntry.delete(0, END) 

    # Function to be executed when Google button is clicked
    def google_login(self):
        # Add your code here to handle Google login
        print("Google login clicked")

if __name__ == "__main__":
    app = User()
    app.create_gui()
    app.mainloop()
