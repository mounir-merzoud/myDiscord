from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import Toplevel
import mariadb

"""
def forget_pass():
    def change_password():
        if usernom_entry.get()=='' or newpassword_entry.get()=='' or Confirmi_passentry.get()=='':
           messagebox.showerror('Error','All fileds are required', parent=window)
        elif newpassword_entry.get()!= Confirmi_passentry.get():
            messagebox.showerror('Error', 'Password and confirm password are not matching', parent=window)
        else:
            try:
                con=mariadb.connect(user='mounir-merzoudy',
                                        password='Mounir-1992',
                                        host='82.165.185.52',
                                        port=3306,
                                        database='mounir-merzoud_myDiscord')
                mycursor = con.cursor()
                #query = 'use mounir-merzoud_myDiscord' 
                #mycursor.execute(query)
                query = 'select * from user where username=%s and mot_de_passe=%s'
                mycursor.execute(query, (usernom_entry.get()))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Incorrect Username', parent=window)
                else:
                    query = 'update user set username=%s where mot_de_passe=%s'
                    mycursor.execute(query,(newpassword_entry.get(),usernom_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success', 'Password is reset, please login with with new password', parent=window)
                    window.destroy()
            except mariadb.Error as error:
                messagebox.showerror('Error', str(error), parent=window)        

"""

def forget_pass():
    def change_password():
        if usernom_entry.get()=='' or newpassword_entry.get()=='' or Confirmi_passentry.get()=='':
           messagebox.showerror('Error','All fileds are required', parent=window)
        elif newpassword_entry.get()!= Confirmi_passentry.get():
            messagebox.showerror('Error', 'Password and confirm password are not matching', parent=window)
        else:
            try:
                con=mariadb.connect(user='mounir-merzoudy',
                                        password='Mounir-1992',
                                        host='82.165.185.52',
                                        port=3306,
                                        database='mounir-merzoud_myDiscord')
                mycursor = con.cursor()
            except mariadb.Error as error:
                messagebox.showerror('Error', str(error), parent=window) 
                return    
            #query = 'use mounir-merzoud_myDiscord' 
            #mycursor.execute(query)
            query = 'select * from user where username=%s'
            mycursor.execute(query, (usernom_entry.get(),))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query = 'update user set mot_de_passe=%s where username=%s'
                mycursor.execute(query, (newpassword_entry.get(), usernom_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with with new password', parent=window)
                window.destroy()
     
       
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

    newpasswordlabel=Label(window, text='Nouveau mot de passe', font=('Comic Sans MS', 11, 'bold'), bg='white', fg='orchid1')
    newpasswordlabel.place(x=470, y=210)
    newpassword_entry=Entry(window, width=25,fg='magenta2', font=('Comic Sans MS', 11, 'bold'), bd=0)
    newpassword_entry.place(x=470, y=240)
    Frame(window, width=250, height=2,bg='orchid1').place(x=470, y=260)

    Confirmi_passlabel=Label(window, text='Confirmer le mot de passe', font=('Comic Sans MS', 11, 'bold'), bg='white', fg='orchid1')
    Confirmi_passlabel.place(x=470, y=290)
    Confirmi_passentry=Entry(window, width=25,fg='magenta2', font=('Comic Sans MS', 11, 'bold'), bd=0)
    Confirmi_passentry.place(x=470, y=320)
    Frame(window, width=250, height=2,bg='orchid1').place(x=470, y=340)

    submitButton=Button(window,text='Envoyer',bd=0, bg='magenta2', fg='white', font=('Comic Sans MS', 16, 'bold'), 
                width=19, activeforeground='magenta2', activebackground='white', cursor='hand2', command=change_password)
    submitButton.place(x=470, y=390)



    window.mainloop()
    