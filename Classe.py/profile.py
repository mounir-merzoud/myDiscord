from tkinter import *
from tkinter import ttk, messagebox, filedialog
import mariadb

class UserProfileApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('990x660+50+50')
        self.master.config(bg="#444654")

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', background='#32cfBE', font=('Arial', 12, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_sidebar()
        self.create_content()

    def create_header(self):
        self.header = Frame(self.master, bg="#000000")
        self.header.place(x=300, y=0, width="1250", height=60)

        self.light_mode_button = ttk.Button(self.header, text="🌓", style='Custom.TButton', command=self.toggle_bg)
        self.light_mode_button.place(x=495, y=15)

    def create_sidebar(self):
        self.sidebar = Frame(self.master, bg="#6B5CFF")
        self.sidebar.place(x=0, y=0, width=300, height=800)

        self.load_image_button = ttk.Button(self.sidebar, text="Profile Image", style='Custom.TButton', command=self.load_profile_image)
        self.load_image_button.pack(pady=10)

    def create_content(self):
        self.profiles_frame = Frame(self.master, bg="#444654")
        self.profiles_frame.place(x=300, y=100, width=690, height=560)

        self.profile_image_labels = []
        self.name_labels = []
        self.info_labels = []
        self.current_profile_index = [0]

        self.load_profiles()

        self.next_button = ttk.Button(self.master, text="Next", style='Custom.TButton', command=self.next_profile)
        self.next_button.place(x=300, y=630)

        self.previous_button = ttk.Button(self.master, text="Previous", style='Custom.TButton', command=self.previous_profile)
        self.previous_button.place(x=400, y=630)

    def toggle_bg(self):
        current_bg = self.master.cget("bg")
        current_header = self.header.cget("bg")
        current_sidebar = self.sidebar.cget("bg")

        if current_bg == "#444654" and current_header == "#000000" and current_sidebar == "#6B5CFF":
            new_bg = "#ffffff"
            new_header = "#808080"
            new_sidebar = "#ffe4db"
        else:
            new_bg = "#444654"
            new_header = "#000000"
            new_sidebar = "#6B5CFF"

        self.master.config(bg=new_bg)
        self.header.config(bg=new_header)
        self.sidebar.config(bg=new_sidebar)

    def load_profile_image(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select Profile Image", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        for label in self.profile_image_labels:
            label.destroy()
        self.profile_image_labels.clear()

    # Créer une nouvelle étiquette d'image
    profile_image = PhotoImage(file="images/icons8-discord-50.png")
    profile_image_label = Label(profiles_frame, image=profile_image, bg="#444654")
    profile_image_label.image = profile_image
    profile_image_label.grid(row=0, column=0, padx=5, pady=5, rowspan=2)  # Ajustez ici
    profile_image_labels.append(profile_image_label)
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

        load_image_button = ttk.Button(sidebar, text="Profile Image", style='Custom.TButton', command=load_profile_image)
        load_image_button.pack(pady=10)

        profile_image_labels = []
        name_labels = []
        info_labels = []
        current_profile_index = [0]

        def display_profile():
            profile = profile_data[current_profile_index[0]]

            for label in profile_image_labels:
                label.destroy()
            profile_image_labels.clear()

            profile_image = PhotoImage(file="images/icons8-discord-50.png")
            profile_image_label = Label(profiles_frame, image=profile_image, bg="#444654")
            profile_image_label.image = profile_image
            profile_image_label.grid(row=0, column=0, padx=5, pady=5)
            profile_image_labels.append(profile_image_label)

            for label in name_labels:
                label.destroy()
            name_labels.clear()

            name_label = Label(profiles_frame, text=f"{profile[0]} {profile[1]}", font="Arial 20 bold", bg="#444654", fg="white")
            name_label.grid(row=0, column=1, padx=5, pady=5)
            name_labels.append(name_label)

            for label in info_labels:
                label.destroy()
            info_labels.clear()
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
        next_button.place(x=300, y=630)

        previous_button = ttk.Button(window, text="Previous", style='Custom.TButton', command=previous_profile)
        previous_button.place(x=400, y=630)

load_profiles()
window.mainloop()
