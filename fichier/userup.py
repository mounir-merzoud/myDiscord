from tkinter import *
from PIL import ImageTk

userup_window=Tk()
userup_window.title('Userup Page')
userup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='images/bg.jpg')

bgLable=Label(userup_window, image=background)
bgLable.grid()

frame=Frame(userup_window, bg='white')
frame.place(x=580, y=100)

heading = Label(frame, text='Create un compte', font=('Comic Sans MS', 20, 'bold'), bg='white', fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel=Label(frame, text='Email', font=('Comic Sans MS', 10, 'bold'), bg='white',fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25)
emailEntry=Entry(frame, width=25, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
emailEntry.grid(row=2,column=0,sticky='w', padx=25)

NomLabel=Label(frame, text='Nom et Prénom', font=('Comic Sans MS', 10, 'bold'), bg='white',fg='firebrick1')
NomLabel.grid(row=3, column=0, sticky='w', padx=25)
NomEntry=Entry(frame, width=25, font=('Comic Sans MS', 10, 'bold'), fg='white', bg='Pink1')
NomEntry.grid(row=4,column=0,sticky='w', padx=25)

userup_window.mainloop()