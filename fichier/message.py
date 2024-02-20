import tkinter as tk
from tkinter import scrolledtext, Button, Toplevel
import customtkinter as ctk

# Liste manuelle d'emojis
emojis_list = ['😀', '😃', '😄', '😁', '😆', '😅', '😂', '🤣', '😊', '😇', '🙂', '🙃', '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😋', '😛', '😝', '😜', '🤪', '🤨', '🧐', '🤓', '😎', '🤩', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🤔', '🤭', '🤫', '🤥', '😶', '😐', '😑', '😬', '🙄', '😯', '😦', '😧', '😮', '😲', '🥱', '😴', '🤤', '😪', '😵', '🤐', '🥴', '🤢', '🤮', '🤧', '😷', '🤒', '🤕', '🤑', '🤠', '😈', '👿', '👹', '👺', '🤡', '💩', '👻', '💀', '☠', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']

def send_message():
    message = message_input.get("1.0", "end").strip()
    if message:
        # Ajouter des emojis au message
        message_with_emojis = message
        message_list.insert(tk.END, message_with_emojis)
        message_input.delete("1.0", tk.END)

def insert_emoji(emoji_char):
    message_input.insert(tk.END, emoji_char)

def show_emojis():
    emojis_window = Toplevel(root)
    emojis_window.title("Choisir un emoji")

    for emoji_char in emojis_list:
        emoji_button = Button(emojis_window, text=emoji_char, command=lambda emoji=emoji_char: insert_emoji(emoji))
        emoji_button.pack(side=tk.LEFT, padx=5, pady=5)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Message")

# Créer la liste des messages avec la possibilité de faire défiler
message_list = scrolledtext.ScrolledText(root, width=50, height=20)
message_list.pack(padx=10, pady=10)

# Créer le champ de saisie pour le message
message_input = ctk.CustomText(root, height=5)
message_input.pack(padx=10, pady=5)

# Créer le bouton d'envoi du message
send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack(padx=10, pady=5)

# Créer le bouton pour les emojis
emojis_button = tk.Button(root, text="Emojis", command=show_emojis)
emojis_button.pack(padx=10, pady=5)

# Lancer la boucle principale
root.mainloop()






