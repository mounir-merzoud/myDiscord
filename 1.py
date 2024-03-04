from tkinter import * 
from tkinter import messagebox
import mariadb

window = Tk()
window.geometry('990x660+50+50')
window.state('zoomed')
window.config(bg="#444654")

def toggle_bg():
    current_bg = window.cget("bg")
    current_header = header.cget("bg")
    current_sidebar = sidebar.cget("bg")
    current_text = text.cget("bg")
    current_text_fg = text.cget("fg")

    if current_bg == "#444654" and current_header == "#000000" \
            and current_sidebar == "#6B5CFF" and current_text == "#444654" \
            and current_text_fg == "#000000":
        new_bg = "#ffffff"
        new_header = "#808080"
        new_sidebar = "#ffe4db"
        new_text = "#ffffff"
        new_text_fg = "blue"
    else: 
        new_bg = "#444654"
        new_header = "#000000"
        new_sidebar = "#6B5CFF"
        new_text = "#444654"
        new_text_fg = "#000000"
    window.config(bg=new_bg)
    header.config(bg=new_header)
    sidebar.config(bg=new_sidebar)
    text.config(bg=new_text)
    text.config(fg=new_text_fg)

header = Frame(window, bg="#000000")
header.place(x=300, y=0, width="1250", height=60)

sidebar = Frame(window, bg="#6B5CFF")
sidebar.place(x=0, y=0, width=300, height=800)

light_mode = Button(header, text="🌓", bg="#32cfBE", font="Arial 12 bold", command=toggle_bg)
light_mode.place(x=495, y=15)

text = Label(window, text="change BG", font="Arial 14 bold", bg="#444654")
text.place(x=600, y=200)

def load_profile():
    global profile_image_label, name_label, info_label

    def fetch_profile_data():
        try:
            con = mariadb.connect(
                user='mounir-merzoudy',
                password='Mounir-1992',
                host='82.165.185.52',
                port=3306,
                database='mounir-merzoud_myDiscord')
            cursor = con.cursor()

            sql = "SELECT * FROM user WHERE id = 1"
            cursor.execute(sql)
            row = cursor.fetchone()
            if row is None:
                messagebox.showerror('Error', 'Aucun utilisateur trouvé')
                return
            return row

        finally: 
            cursor.close()
            con.close()

    profile_data = fetch_profile_data()
    if profile_data is not None:
        # Créez un cadre pour le contenu du profil
        profile_frame = Frame(window, bg="#444654")
        profile_frame.place(x=300, y=100, width=690, height=560)

        
        # Affichez la photo de profil
        profile_image = PhotoImage(file=profile_data[4])
        profile_image_label = Label(profile_frame, image=profile_image, bg="#444654")
        profile_image_label.place(x=20, y=20, width=120, height=120)

        # Affichez les informations de l'utilisateur
        name_label = Label(profile_frame, text=f"{profile_data[0]} {profile_data[1]}", font="Arial 20 bold", bg="#444654", fg="white")
        name_label.place(x=20, y=20)

        email_label = Label(profile_frame, text=f"Email : {profile_data[2]}", font="Arial 14", bg="#444654", fg="white")
        email_label.place(x=20, y=60)

        password_label = Label(profile_frame, text=f"Mot de passe : {profile_data[3]}", font="Arial 14", bg="#444654", fg="white")
        password_label.place(x=20, y=100)  

        info_label = Label(profile_frame, text=f"Informations : {profile_data[5]}", font="Arial 14", bg="#444654", fg="white")
        info_label.place(x=160, y=180)
        

load_profile()
window.mainloop()


