from tkinter import *
from tkinter import ttk, messagebox, filedialog
import mariadb

window = Tk()
window.geometry('990x660+50+50')
window.state('zoomed')
window.config(bg="#444654")

# Définition du style pour tous les boutons
style = ttk.Style()
style.configure('Custom.TButton', background='#32cfBE', font=('Arial', 12, 'bold'))

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

light_mode = ttk.Button(header, text="🌓", style='Custom.TButton', command=toggle_bg)
light_mode.place(x=495, y=15)

text = Label(window, text="change BG", font="Arial 14 bold", bg="#444654")
text.place(x=600, y=200)

def load_profile_image():
    filename = filedialog.askopenfilename(initialdir="/", title="Select Profile Image", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
    if filename:
        profile_image = PhotoImage(file="images/icons8-discord-50.png")
        profile_image_label = Label(window, image=profile_image, bg="#444654")
        profile_image_label.image = profile_image  # Gardez une référence à l'image pour éviter qu'elle ne soit collectée par le garbage collector
        profile_image_label.place(x=20, y=20)

def load_profiles():
    global profile_image_labels, name_labels, info_labels, current_profile_index

    def fetch_profile_data():
        try:
            con = mariadb.connect(
                user='mounir-merzoudy',
                password='Mounir-1992',
                host='82.165.185.52',
                port=3306,
                database='mounir-merzoud_myDiscord')
            cursor = con.cursor()

            sql = "SELECT * FROM user"
            cursor.execute(sql)
            rows = cursor.fetchall()
            if not rows:
                messagebox.showerror('Error', 'No users found')
                return
            return rows

        finally:
            cursor.close()
            con.close()

    profile_data = fetch_profile_data()
    if profile_data:
        profiles_frame = Frame(window, bg="#444654")
        profiles_frame.place(x=300, y=100, width=690, height=560)

        profile_image_labels = []
        name_labels = []
        info_labels = []
        current_profile_index = [0]

        def display_profile():
            profile = profile_data[current_profile_index[0]]

            # Supprimer les anciennes étiquettes d'image
            for label in profile_image_labels:
                label.destroy()
            profile_image_labels.clear()

            # Créer une nouvelle étiquette d'image
            profile_image = PhotoImage(file="images/icons8-discord-50.png")
            profile_image_label = Label(profiles_frame, image=profile_image, bg="#444654")
            profile_image_label.image = profile_image  # Gardez une référence à l'image pour éviter qu'elle ne soit collectée par le garbage collector
            profile_image_label.grid(row=0, column=0, padx=5, pady=5)
            profile_image_labels.append(profile_image_label)

            # Supprimer les anciennes étiquettes de nom
            for label in name_labels:
                label.destroy()
            name_labels.clear()

            # Créer une nouvelle étiquette de nom
            name_label = Label(profiles_frame, text=f"{profile[0]} {profile[1]}", font="Arial 20 bold", bg="#444654", fg="white")
            name_label.grid(row=0, column=1, padx=5, pady=5)
            name_labels.append(name_label)

            # Supprimer les anciennes étiquettes d'informations
            for label in info_labels:
                label.destroy()
            info_labels.clear()

            # Créer une nouvelle étiquette d'informations
            username_label = Label(profiles_frame, text=f"Username : {profile[0]}", font="Arial 14", bg="#444654", fg="white")
            username_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
            info_labels.append(username_label)

            firstname_label = Label(profiles_frame, text=f"Prename : {profile[1]}", font="Arial 14", bg="#444654", fg="white")
            firstname_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
            info_labels.append(firstname_label)

            email_label = Label(profiles_frame, text=f"Email : {profile[2]}", font="Arial 14", bg="#444654", fg="white")
            email_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            info_labels.append(email_label)

            password_label = Label(profiles_frame, text=f"Password : {profile[3]}", font="Arial 14", bg="#444654", fg="white")
            password_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
            info_labels.append(password_label)

            info_label = Label(profiles_frame, text=f"Information : {profile[5]}", font="Arial 14", bg="#444654", fg="white")
            info_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
            info_labels.append(info_label)

        def next_profile():
            current_profile_index[0] = (current_profile_index[0] + 1) % len(profile_data)
            display_profile()

        def previous_profile():
            current_profile_index[0] = (current_profile_index[0] - 1) % len(profile_data)
            display_profile()

        display_profile()

        next_button = ttk.Button(window, text="Next", style='Custom.TButton', command=next_profile)
        next_button.place(x=500, y=670)

        previous_button = ttk.Button(window, text="Previous", style='Custom.TButton', command=previous_profile)
        previous_button.place(x=400, y=670)

        load_image_button = ttk.Button(profiles_frame, text="Load Profile Image", style='Custom.TButton', command=load_profile_image)
        load_image_button.grid(row=4, column=0, columnspan=2, pady=10)

load_profiles()
window.mainloop()













