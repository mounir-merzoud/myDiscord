import tkinter.scrolledtext
import tkinter as tk
from tkinter import Tk, Label, Text, Button, Toplevel, Frame, Entry, END
from tkinter import PhotoImage
from ttkthemes import ThemedStyle 
from PIL import Image, ImageTk
from client import Client  # Importer la classe Client depuis le fichier client.py

def enregistrer_message(message):
    with open("historique_chat.txt", "a") as file:
        file.write(message + "\n")

def main():
    win = Tk()
    win.geometry("600x400")
    win.title("Chat App")

    style = ThemedStyle(win)
    style.set_theme("equilux")

    chat_label = Label(win, text="SALON")
    chat_label.configure(font="Arial 12", background=style.lookup('TLabel', 'background'), foreground=style.lookup('TLabel', 'foreground'))
    chat_label.pack(padx=20, pady=5)

    text_area = tkinter.scrolledtext.ScrolledText(win)
    text_area.pack(padx=20, pady=5)
    text_area.config(state="disabled")

    msg_label = Label(win, text="Message")
    msg_label.configure(font="Arial 12", background=style.lookup('TLabel', 'background'), foreground=style.lookup('TLabel', 'foreground'))
    msg_label.pack(padx=20, pady=5)

    input_field = Text(win, height=3)
    input_field.pack(padx=20, pady=5)

    send_button = Button(win, text="Envoyer", command=send_message)
    send_button.configure(font="Arial 12", background="#0000FF", foreground="white")
    send_button.pack(padx=20, pady=5)

    # Créer une instance de la classe Client pour démarrer le chat
    client = Client("10.10.95.89", 9090)

    win.mainloop()

def send_message():
    pass

if __name__ == "__main__":
    main()
