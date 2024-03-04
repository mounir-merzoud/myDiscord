from tkinter import * 

window = Tk()
window.geometry('990x660+50+50')
window.state('zoomed')
window.config(bg="#444654")

# light mode toggle section
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

light_mode = Button(header, text="change background color", bg="#32cfBE", font="Arial 12 bold", command=toggle_bg)
light_mode.place(x=495, y=15)

text = Label(window, text="change BG", font="Arial 14 bold", bg="#444654")
text.place(x=600, y=200)


window.mainloop()

