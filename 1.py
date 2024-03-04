from tkinter import * 

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

# Fonction pour charger et afficher l'image de profil
def load_profile_image():
    global profile_image_label
    profile_image_label = Label(window, bg="#444654")
    profile_image_label.place(x=20, y=100)
    # Chargez votre image de profil et attribuez-la à profile_image_path
    profile_image_path = "images/icons8-discord-50 (1).png"
    profile_image = PhotoImage(file=profile_image_path)
    profile_image_label.config(image=profile_image)
    profile_image_label.image = profile_image  # Gardez une référence à l'image pour éviter la suppression par le garbage collector

load_profile_image()

window.mainloop()


