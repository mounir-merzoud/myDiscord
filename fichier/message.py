import tkinter as tk

def send_message():
    message = message_input.get("1.0", "end").strip()
    if message:
        print("Message envoyé :", message)
        message_input.delete("1.0", "end")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Envoyer un message")

# Créer le champ de saisie pour le message
message_input = tk.Text(root, height=5)
message_input.pack(padx=10, pady=10)

# Créer le bouton d'envoi du message
send_button = tk.Button(root, text="Envoyer", command=send_message)
send_button.pack(padx=10, pady=10)

# Lancer la boucle principale
root.mainloop()
