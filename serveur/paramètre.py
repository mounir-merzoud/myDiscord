from tkinter import *
from tkinter import messagebox
import mariadb

class ParametresWindow:
    def __init__(self, user):
        self.user = user
        self.param_window = Toplevel()
        self.param_window.title("Paramètres")
        self.param_window.geometry("400x300")

        self.label_username = Label(self.param_window, text="Nom d'utilisateur:")
        self.label_username.pack()
        self.entry_username = Entry(self.param_window)
        self.entry_username.insert(0, self.user["username"])
        self.entry_username.pack()

        self.label_email = Label(self.param_window, text="Adresse email:")
        self.label_email.pack()
        self.entry_email = Entry(self.param_window)
        self.entry_email.insert(0, self.user["email"])
        self.entry_email.pack()

        self.save_button = Button(self.param_window, text="Enregistrer", command=self.save_changes)
        self.save_button.pack()

    def save_changes(self):
        new_username = self.entry_username.get()
        new_email = self.entry_email.get()
        try:
            con = mariadb.connect(user='mounir-merzoudy',
                                  password='Mounir-1992',
                                  host='82.165.185.52',
                                  port=3306,
                                  database='mounir-merzoud_myDiscord')
            with con.cursor() as cursor:
                sql = "UPDATE `user` SET `username`=%s, `email`=%s WHERE `id`=%s"
                cursor.execute(sql, (new_username, new_email, self.user["id"]))
                con.commit()
                self.user["username"] = new_username
                self.user["email"] = new_email
                messagebox.showinfo("Succès", "Modifications enregistrées avec succès")
        except mariadb.Error as e:
            print(f"Error: {e}")
            messagebox.showerror("Erreur", "Une erreur est survenue lors de l'enregistrement des modifications")
        finally:
            con.close()

# Fonction pour obtenir les informations de l'utilisateur à partir de la base de données
def get_user_info(username):
    try:
        con = mariadb.connect(user='mounir-merzoudy',
                                  password='Mounir-1992',
                                  host='82.165.185.52',
                                  port=3306,
                                  database='mounir-merzoud_myDiscord')
        with con.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `username`=%s"
            cursor.execute(sql, (username,))
            user = cursor.fetchone()
            user_info = {"id": user[0], "username": user[1], "email": user[3]} if user else None
            return user_info
    except mariadb.Error as e:
        print(f"Error: {e}")
    finally:
        con.close()

def open_settings(username):
    # Récupérer les informations de l'utilisateur actuellement connecté
    user_info = get_user_info(username)
    if user_info:
        param_window = ParametresWindow(user_info)
    else:
        messagebox.showerror("Erreur", "Impossible de récupérer les informations de l'utilisateur")

# Fonction pour gérer la connexion de l'utilisateur
def login_user():
    # Vérifier si les champs de saisie sont remplis
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Veuillez remplir tous les champs')
        return
    
    # Connexion à la base de données pour vérifier l'authentification
    try:
        con = mariadb.connect(user='mounir-merzoudy',
                                  password='Mounir-1992',
                                  host='82.165.185.52',
                                  port=3306,
                                  database='mounir-merzoud_myDiscord')
        with con.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `username`=%s AND `mot_de_passe`=%s"
            cursor.execute(sql, (usernameEntry.get(), passwordEntry.get()))
            user = cursor.fetchone()
            if user:
                print("Authentification réussie.")
                messagebox.showinfo('Succès', 'La connexion est établie ')
                open_settings(usernameEntry.get())
            else:
                print("Erreur d'authentification.")
                messagebox.showerror('Error' , 'Nom d\'utilisateur ou mot de passe invalide')
    except mariadb.Error as e:
        print(f"Error: {e}")
        messagebox.showerror("Erreur", "Une erreur est survenue lors de l'authentification")
    finally:
        con.close() 

#GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')

# Ajouter les champs de saisie pour le nom d'utilisateur et le mot de passe
usernameEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
passwordEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1', show='*')
passwordEntry.place(x=580, y=260)

# Ajouter le bouton de connexion
loginButton=Button(login_window,text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white', bg='firebrick1', activeforeground='black', activebackground='white', cursor='hand2',bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

login_window.mainloop()
