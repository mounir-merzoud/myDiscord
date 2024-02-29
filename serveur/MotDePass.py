from tkinter import *
from PIL import ImageTk
from tkinter import Toplevel


def forget_pass():
    window = Toplevel()
    window.title('modifier le mot de passe')

    bgPic = ImageTk.PhotoImage(file='images/background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label=Label(window, text='Modifier le mot de passe', font=('Comic Sans MS', 16, 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=470, y=60)

    usernomlabel=Label(window, text='username', font=('Comic Sans MS', 11, 'bold'), bg='white', fg='orchid1')
    usernomlabel.place(x=470, y=130)
    usernom_entry=Entry(window, width=25,fg='magenta2', font=('Comic Sans MS', 11, 'bold'), bd=0)
    usernom_entry.place(x=470, y=160)
    Frame(window, width=250, height=2,bg='orchid1').place(x=470, y=180)

    passwordlabel=Label(window, text='Nouveau mot de passe', font=('Comic Sans MS', 11, 'bold'), bg='white', fg='orchid1')
    passwordlabel.place(x=470, y=210)
    newpassword_entry=Entry(window, width=25,fg='magenta2', font=('Comic Sans MS', 11, 'bold'), bd=0)
    newpassword_entry.place(x=470, y=240)
    Frame(window, width=250, height=2,bg='orchid1').place(x=470, y=260)

    Confirmi_passlabel=Label(window, text='Confirmer le mot de passe', font=('Comic Sans MS', 11, 'bold'), bg='white', fg='orchid1')
    Confirmi_passlabel.place(x=470, y=290)
    Confirmi_passentry=Entry(window, width=25,fg='magenta2', font=('Comic Sans MS', 11, 'bold'), bd=0)
    Confirmi_passentry.place(x=470, y=320)
    Frame(window, width=250, height=2,bg='orchid1').place(x=470, y=340)

    submitButton=Button(window,text='Envoyer',bd=0, bg='magenta2', fg='white', font=('Comic Sans MS', 16, 'bold'), 
                width=19, activeforeground='magenta2', activebackground='white', cursor='hand2')
    submitButton.place(x=470, y=390)



    window.mainloop()