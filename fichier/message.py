import tkinter as tk
from tkinter import ttk
import json
import pyaudio
import wave
import socket
import os

# Configuration du socket client
SERVER_ADDRESS = '82.165.185.52'  # Adresse IP du serveur
SERVER_PORT = 3306  # Port sur lequel le serveur écoute

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Chemin du mémo vocal
memo_audio_path = None

# Charger les emojis à partir du fichier JSON en spécifiant l'encodage
with open('imoji.json', 'r', encoding='utf-8') as file:
    emojis_data = json.load(file)

emojis = emojis_data['emojis']

memo_audio_path = None  # Ajoutez cette ligne avant la fonction send_message() pour initialiser la variable

def send_message():
    global memo_audio_path 
    message = message_input.get("1.0", "end").strip()
    if message:
        # Insérer le message dans la zone de texte
        message_list.config(state=tk.NORMAL)
        message_list.insert(tk.END, f"You: {message}\n", "sent_message")
        
        # S'il y a un mémo vocal enregistré, l'ajouter à la zone de texte
        if memo_audio_path:
            message_list.insert(tk.END, f"Memo vocal: {memo_audio_path}\n", "sent_message")
        
        message_list.config(state=tk.DISABLED)
        
        # Envoyer le message et le mémo vocal au serveur
        send_data_to_server(message, memo_audio_path)
        
        # Réinitialiser la variable memo_audio_path correctement
        memo_audio_path = None  
        
        # Effacer le contenu de la zone de saisie
        message_input.delete("1.0", tk.END)


# Fonction pour insérer un emoji dans la zone de saisie de message
def insert_emoji(emoji):
    message_input.insert(tk.END, emoji)

# Fonction pour enregistrer un mémo vocal
def record_audio():
    global memo_audio_path
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "memo.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Enregistrement audio...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Enregistrement terminé.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    # Mettre à jour le chemin du mémo vocal
    memo_audio_path = WAVE_OUTPUT_FILENAME

# Fonction pour envoyer les données (message et mémo vocal) au serveur
def send_data_to_server(message, audio_path):
    try:
        client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
        
        # Envoyer le message
        client_socket.sendall(message.encode())
        
        # Si un mémo vocal est enregistré, l'envoyer
        if audio_path:
            with open(audio_path, "rb") as audio_file:
                audio_data = audio_file.read()
                client_socket.sendall(audio_data)
                print("Le mémo vocal a été envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi des données au serveur : {e}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Message")

# Définir le style de la fenêtre et des widgets
root.configure(bg='blue')  # Couleur de fond rose

# Définir les styles personnalisés
root.style = ttk.Style()
root.style.theme_create("custom", parent="clam", settings={
    "TButton": {"configure": {"background": "navy", "foreground": "white", "font": ("Helvetica", 12)}},
    "TLabel": {"configure": {"foreground": "white", "font": ("Helvetica", 12), "background": "navy"}},
    "TFrame": {"configure": {"background": "medium blue"}},
    "TText": {"configure": {"background": "navy", "foreground": "white", "font": ("Helvetica", 12)}},
})
root.style.theme_use("custom")

# Cadre pour la zone de message
message_frame = ttk.Frame(root)
message_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Zone de texte pour les messages
message_list = tk.Text(message_frame, bg='navy', fg='white', font=('Helvetica', 12), state=tk.DISABLED)
message_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barre de défilement pour la zone de texte
scrollbar = ttk.Scrollbar(message_frame, command=message_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
message_list.config(yscrollcommand=scrollbar.set)

# Cadre pour la saisie de message
input_frame = ttk.Frame(root)
input_frame.pack(padx=10, pady=10, fill=tk.BOTH)

# Zone de texte pour la saisie de message
message_input = tk.Text(input_frame, height=3, bg='navy', fg='white', font=('Helvetica', 12))
message_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Bouton pour envoyer le message
send_button = ttk.Button(input_frame, text="Envoyer", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

# Bouton pour enregistrer un mémo vocal
record_button = ttk.Button(input_frame, text="Enregistrer Mémo Vocal", command=record_audio)
record_button.pack(side=tk.LEFT, padx=5)

# Bouton pour afficher la liste d'emojis
def show_emojis():
    emojis_window = tk.Toplevel(root)
    emojis_window.title("Choisir Emoji")
    emojis_window.configure(bg='navy')

    emojis_frame = ttk.Frame(emojis_window)
    emojis_frame.pack(padx=10, pady=10)

    for emoji in emojis:  # Utiliser la liste des emojis chargés à partir du fichier JSON
        emoji_button = ttk.Button(emojis_frame, text=emoji, command=lambda e=emoji: insert_emoji(e))
        emoji_button.pack(side=tk.LEFT, padx=5, pady=5)

emoji_button = ttk.Button(input_frame, text="Afficher Emojis", command=show_emojis)
emoji_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
