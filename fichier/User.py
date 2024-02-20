from tkinter import *
from PIL import ImageTk

#Functionality Part
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
#bgLabel.place(x=0, y=0)
bgLabel.pack() # position automatiquely

heading=Label(login_window, text='Utilisateur', font=('Comic Sans MS', 23, 'bold'), bg='white', fg='firebrick1')
heading.place(x=610, y=120)

usernameEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=580, y=200)
usernameEntry.insert(0, 'Nom ou Email')

usernameEntry.bind('<FocusIn>',user_enter)

frame1=Frame(login_window, width=250, height=2,bg='firebrick1') #.place(x=580, y=222)
frame1.place(x=580, y=222)


passwordEntry=Entry(login_window, width=25, font=('Comic Sans MS', 11, 'bold'), bd=0, fg='firebrick1')
passwordEntry.place(x=580, y=260)
passwordEntry.insert(0, 'Mot de pass')

passwordEntry.bind('<FocusIn>',password_enter)


frame2=Frame(login_window, width=250, height=2,bg='firebrick1') #.place(x=580, y=222)
frame2.place(x=580, y=282)
openeye=PhotoImage(file='images/openeye.png')
eyeButton=Button(login_window, image=openeye,bd=0, bg='white', activebackground='white', cursor='hand2',command=hide)
eyeButton.place(x=800, y=255)

forgetButton=Button(login_window, text='Mot de pass oublier ?',bd=0, bg='white', activebackground='white'
                    , cursor='hand2', font=('Comic Sans MS', 8, 'bold'), fg='firebrick1', activeforeground='black')
forgetButton.place(x=715, y=295)
loginButton=Button(login_window,text='se connecter', font=('Comic Sans MS', 16, 'bold'), fg='white'
                   , bg='firebrick1', activeforeground='black', activebackground='white', cursor='hand2',bd=0, width=19)
loginButton.place(x=578, y=350)

login_window.mainloop()