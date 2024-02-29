from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mariadb



def clear():
    emailEntry.delete(0, END)
    NomEntry.delete(0, END)
    MotDePasseEntry.delete(0, END)
    ConfirmerEntry.delete(0, END)
    check.set(0)
def connect_database():
    if emailEntry.get() == '' or NomEntry.get() == '' or MotDePasseEntry.get() == '' or ConfirmerEntry.get() == '':
        messagebox.showerror('Error', 'Tous les champs sont requis')
    elif MotDePasseEntry.get() != ConfirmerEntry.get():
        messagebox.showerror('Error', 'Non concordance des mots de passe')
    elif check.get() == 0:
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
            messagebox.showerror('Error','Database connectivity Issue, Please Try Again') 
            return
        try:   
            query='select * from user where username=%s'
            mycursor.execute(query,(NomEntry.get(),))

            row=mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Username Already exists') 
            else:
                query= 'insert into user (email, prenom, mot_de_passe) values(%s,%s,%s)'     
                mycursor.execute(query,(emailEntry.get(), NomEntry.get(), MotDePasseEntry.get()))
                con.commit()
                messagebox.showinfo('Succès', 'Inscription réussie')
        except mariadb.Error as e:
            messagebox.showerror('Error', 'Erreur lors de l\'insertion des données : {}'.format(e))
        finally:
            con.close()
            clear()
            userup_window.destroy()
            import User

def login_page():
    userup_window.destroy()
    import User

userup_window = Tk()
userup_window.title('Userup Page')
userup_window.resizable(False, False)
background = ImageTk.PhotoImage(file='images/bg.jpg')

bgLable = Label(userup_window, image=background)
bgLable.grid()

frame = Frame(userup_window, bg='white')
frame.place(x=580, y=100)

heading = Label(frame, text='Create un compte', font=('Comic Sans MS', 20, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text='Email', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
emailEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

NomLabel = Label(frame, text='Nom et Prénom', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
NomLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
NomEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
NomEntry.grid(row=4, column=0, sticky='w', padx=25)

MotDePasseLabel = Label(frame, text='Mot de passe', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
MotDePasseLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
MotDePasseEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
MotDePasseEntry.grid(row=6, column=0, sticky='w', padx=25)

ConfirmerLabel = Label(frame, text='Confirmer mot de passe ', font=('Comic Sans MS', 10, 'bold'), bg='white', fg='firebrick1')
ConfirmerLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
ConfirmerEntry = Entry(frame, width=30, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
ConfirmerEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
termsandconditions = Checkbutton(frame, text='I agree to the Terms & conditions', font=('Comic Sans MS', 10, 'bold'), fg='firebrick1', bg='white', activebackground='white', activeforeground='firebrick1',
                                 cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=11)

signupButton = Button(frame, text='Signup', font=('Comic Sans MS', 16, 'bold'), bd=0, bg='firebrick1', fg='white', activebackground='firebrick1', activeforeground='white',
                      width=17, command=connect_database)
signupButton.grid(row=10, column=0, padx=10)

Alreadyaccount = Label(frame, text='Y a pas un compt ?', font=('Comic Sans MS', 9, 'bold'), bg='white', fg='firebrick1')
Alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton = Button(frame, text='Log in', font=('Comic Sans MS', 9, 'bold'), bg='white', fg='blue', bd=0, cursor='hand2',
                     activebackground='white', activeforeground='blue', command=login_page)
loginButton.place(x=170, y=404)

userup_window.mainloop()



