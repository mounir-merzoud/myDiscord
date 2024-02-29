from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mariadb


class UserUp:
    def __init__(self):
        self.userup_window = Tk()
        self.userup_window.title('Userup Page')
        self.userup_window.resizable(False, False)
        self.background = ImageTk.PhotoImage(file='images/bg.jpg')

        self.bg_label = Label(self.userup_window, image=self.background)
        self.bg_label.grid()

        self.frame = Frame(self.userup_window, bg='white')
        self.frame.place(x=580, y=100)

        self.heading = Label(self.frame, text='Create un compte', font=('Comic Sans MS', 20, 'bold'), bg='white', fg='firebrick1')
        self.heading.grid(row=0, column=0, padx=10, pady=10)

        self.email_label = Label(self.frame, text='Email', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
        self.email_label.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
        self.email_entry = Entry(self.frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
        self.email_entry.grid(row=2, column=0, sticky='w', padx=25)


        self.NomLabel = Label(self.frame, text='Nom et Prénom', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
        self.NomLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
        self.NomEntry = Entry(self.frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
        self.NomEntry.grid(row=4, column=0, sticky='w', padx=25)

        self.MotDePasseLabel = Label(self.frame, text='Mot de passe', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
        self.MotDePasseLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
        self.MotDePasseEntry = Entry(self.frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
        self.MotDePasseEntry.grid(row=6, column=0, sticky='w', padx=25)

        self.ConfirmerLabel = Label(self.frame, text='Confirmer mot de passe ', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
        self.ConfirmerLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
        self.ConfirmerEntry = Entry(self.frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
        self.ConfirmerEntry.grid(row=8, column=0, sticky='w', padx=25)

        self.check = IntVar()
        self.termsandconditions = Checkbutton(self.frame, text='I agree to the Terms & conditions', font=('Comic Sans MS', 10, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
                                              cursor='hand2', variable=self.check)
        self.termsandconditions.grid(row=9, column=0, pady=10, padx=11)

        self.signup_button = Button(self.frame, text='Signup', font=('Comic Sans MS', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white',
                                    width=17, command=self.connect_database)
        self.signup_button.grid(row=10, column=0, padx=10)

        self.Alreadyaccount = Label(self.frame, text='Y a pas un compt ?', font=('Comic Sans MS', 9, 'bold'), bg='white', fg='firebrick1')
        self.Alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

        self.login_button = Button(self.frame, text='Log in', font=('Comic Sans MS', 9, 'bold'), bg='white', fg='blue', bd=0, cursor='hand2',
                                   activebackground='white', activeforeground='blue', command=self.login_page)
        self.login_button.place(x=170, y=404)

        self.userup_window.mainloop()
    def clear(self):
        self.email_entry.delete(0, END)
        self.NomEntry.delete(0, END)
        self.MotDePasseEntry.delete(0, END)
        self.ConfirmerEntry.delete(0, END)
        self.check.set(0)

    def connect_database(self):
        if self.email_entry.get() == '':
            messagebox.showerror('Error', 'Tous les champs sont requis')
        elif self.check.get() == 0:
            messagebox.showerror('Error', 'Veuillez accepter les termes et conditions')    
        else:    
            try:
                con = mariadb.connect(user='mounir-merzoudy',
                                        password='Mounir-1992',
                                        host='82.165.185.52',
                                        port=3306,
                                        database='mounir-merzoud_myDiscord')
                mycursor = con.cursor()
            except mariadb.Error as e:
                messagebox.showerror('Error', 'Database connectivity Issue, Please Try Again')
                return
            try:
                query = 'SELECT * FROM user WHERE username=%s'
                mycursor.execute(query, (self.email_entry.get(),))
                row = mycursor.fetchone()
                if row is not None:
                    messagebox.showerror('Error', 'Username Already exists')
                else:
                    query = 'INSERT INTO user (email, prenom, mot_de_passe) VALUES (%s, %s, %s)'
                    mycursor.execute(query, (self.email_entry.get(), self.NomEntry.get(), self.MotDePasseEntry.get()))
                    con.commit()
                    messagebox.showinfo('Succès', 'Inscription réussie')
            except mariadb.Error as e:
                messagebox.showerror('Error', 'Erreur lors de l\'insertion des données : {}'.format(e))
            finally:
                con.close()
                self.clear()
    def login_page(self):
        self.userup_window.destroy()  
        import User

if __name__ == "__main__":
    #root = Tk()
    user_up = UserUp()