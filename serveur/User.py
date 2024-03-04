from tkinter import *
from tkinter import messagebox
import mariadb
from userup import UserUp
from tkinter import  Tk, Label, Text, Button, Toplevel, Frame
from tkinter import PhotoImage
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from client import Client
from MotDePass import forget_pass

# Définissez votre classe Client ici

def open_chat_window():
    global chat_client
    HOST = "10.10.102.103"
    PORT = 9090
    username = usernameEntry.get()  # Récupérer le nom d'utilisateur
    password = passwordEntry.get()  # Récupérer le mot de passe
    chat_client = Client(HOST, PORT, username, password)  # Passer le nom d'utilisateur et le mot de passe à Client
    login_window.destroy()


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Veuillez remplir tous les champs')
    
    con = mariadb.connect(user='mounir-merzoudy',
                                  password='Mounir-1992',
                                  host='82.165.185.52',
                                  port=3306,
                                  database='mounir-merzoud_myDiscord')
    cursor = con.cursor()
    try:
            with con.cursor() as cursor:
                sql = "SELECT * FROM `user` WHERE `username`=%s AND `mot_de_passe`=%s"
                cursor.execute(sql, (usernameEntry.get(), passwordEntry.get()))
                user = cursor.fetchone()
                if user:
                    print("Authentification réussie.")
                    messagebox.showinfo('Succès', 'La connexion est établie ')
                    open_chat_window() 
                else:
                    print("Erreur d'authentification.")
                    messagebox.showerror('Error' , 'Nom d\'utilisateur ou mot de passe invalide')
    finally:
        con.close() 

def signup_page():
    login_window.destroy()
    user_up = UserUp()

def hide():
    openeye.config(file='images/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='images/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get()=='Nom ou Email':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get()=='Mot de pass':
        passwordEntry.delete(0, END)        



#GUI Part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.pack()

heading=Label(login_window, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=610, y=120)

usernameEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Nom ou Email')
usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window, width=250, height=2,bg='firebrick1') 
frame1.place(x=580, y=222)

passwordEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Mot de pass')
passwordEntry.bind('<FocusIn>',password_enter)

frame2=Frame(login_window, width=250, height=2,bg='firebrick1')
frame2.place(x=580, y=282)

openeye=PhotoImage(file='images/openeye.png')
eyeButton=Button(login_window, image=openeye,bd=0, bg='white', activebackground='white', cursor='hand2',command=hide)
eyeButton.place(x=800, y=255)

forgetButton=Button(login_window, text='Mot de pass oublier ?',bd=0, bg='white', activebackground='white'
                    , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', activeforeground='black' , command=forget_pass)
forgetButton.place(x=715, y=295)

loginButton=Button(login_window,text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white'
                   , bg='firebrick1', activeforeground='black', activebackground='white', cursor='hand2',bd=0, width=19, command=login_user)
loginButton.place(x=578, y=350)

# Create a clickable Google button
google_logo=PhotoImage(file='images/google.png')
googleButton=Button(login_window, image=google_logo, bd=0, bg='white', activebackground='white', cursor='hand2')
googleButton.place(x=650, y=400)

signupLabel=Label(login_window,text='Ne pas de compte ?', font=('Comic Sans MS',12,'bold'), fg='firebrick1', bg='white')
signupLabel.place(x=575, y=500)

newaccountButton=Button(login_window,text='Create New', font=('Comic Sans MS', 9, 'bold underline'), fg='black'
                   , bg='white', activeforeground='black', activebackground='white', cursor='hand2',bd=0, command=signup_page)
newaccountButton.place(x=727, y=500)

login_window.mainloop()










