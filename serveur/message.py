import tkinter as tk
from tkinter import ttk, filedialog
import json
import pyaudio
import wave
import socket

class ChatApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Message")
        self.master.configure(bg='LightSalmon')

        self.SERVER_ADDRESS = '82.165.185.52'
        self.SERVER_PORT = 3306
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.memo_audio_path = None

        with open('imoji.json', 'r', encoding='utf-8') as file:
            self.emojis_data = json.load(file)
        self.emojis = self.emojis_data['emojis']

        # Définissez une variable booléenne pour suivre si le thème a été créé
        self.theme_created = False

        self.setup_ui()

    def setup_ui(self):
        if not self.theme_created:
            # Créez le thème uniquement s'il n'existe pas déjà
            self.style = ttk.Style()
            self.style.theme_create("custom", parent="clam", settings={
                "TButton": {"configure": {"background": "salmon3", "foreground": "white", "font": ("Helvetica", 12)}},
                "TLabel": {"configure": {"foreground": "white", "font": ("Helvetica", 12), "background": "salmon3"}},
                "TFrame": {"configure": {"background": "LightSalmon"}},
                "TText": {"configure": {"background": "salmon3", "foreground": "white", "font": ("Helvetica", 12)}},
            })
            self.style.theme_use("custom")

            # Mettez à jour la variable booléenne pour indiquer que le thème a été créé
            self.theme_created = True

        message_frame = ttk.Frame(self.master)
        message_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.message_list = tk.Text(message_frame, bg='salmon3', fg='white', font=('Helvetica', 12), state=tk.DISABLED)
        self.message_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(message_frame, command=self.message_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.message_list.config(yscrollcommand=scrollbar.set)

        input_frame = ttk.Frame(self.master)
        input_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.message_input = tk.Text(input_frame, height=3, bg='salmon3', fg='white', font=('Helvetica', 12))
        self.message_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        send_button = ttk.Button(input_frame, text="🚀", command=self.send_message)
        send_button.pack(side=tk.LEFT, padx=5)

        record_button = ttk.Button(input_frame, text="🎤", command=self.record_audio)
        record_button.pack(side=tk.LEFT, padx=5)

        photo_button = ttk.Button(input_frame, text="📷", command=self.send_photo)
        photo_button.pack(side=tk.LEFT, padx=5)

        video_button = ttk.Button(input_frame, text="🎥", command=self.send_video)
        video_button.pack(side=tk.LEFT, padx=5)

        emoji_button = ttk.Button(input_frame, text="😎", command=self.show_emojis)
        emoji_button.pack(side=tk.LEFT, padx=5)

    def send_message(self):
        message = self.message_input.get("1.0", "end").strip()
        if message:
            self.message_list.config(state=tk.NORMAL)
            self.message_list.insert(tk.END, f"You: {message}\n", "sent_message")

            if self.memo_audio_path:
                self.message_list.insert(tk.END, f"Memo vocal: {self.memo_audio_path}\n", "sent_message")

            self.message_list.config(state=tk.DISABLED)

            self.send_data_to_server(message, self.memo_audio_path)

            self.memo_audio_path = None
            self.message_input.delete("1.0", tk.END)

    def record_audio(self):
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

        self.memo_audio_path = WAVE_OUTPUT_FILENAME

    def send_data_to_server(self, message, audio_path):
        try:
            self.client_socket.connect((self.SERVER_ADDRESS, self.SERVER_PORT))
            self.client_socket.sendall(message.encode())

            if audio_path:
                with open(audio_path, "rb") as audio_file:
                    audio_data = audio_file.read()
                    self.client_socket.sendall(audio_data)
                    print("Le mémo vocal a été envoyé avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'envoi des données au serveur : {e}")

    def send_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            self.send_generic_file(file_path)

    def send_generic_file(self, file_path):
        try:
            self.client_socket.connect((self.SERVER_ADDRESS, self.SERVER_PORT))
            with open(file_path, "rb") as file:
                file_data = file.read()
                self.client_socket.sendall(file_data)
            print(f"Le fichier {file_path} a été envoyé avec succès.")
        except Exception as e:
            print(f"Erreur lors de l'envoi du fichier au serveur : {e}")

    def send_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.send_generic_file(file_path)

    def show_emojis(self):
        emojis_window = tk.Toplevel(self.master)
        emojis_window.title("😎")
        emojis_window.configure(bg='salmon3')

        emojis_frame = ttk.Frame(emojis_window)
        emojis_frame.pack(padx=10, pady=10)

        for emoji in self.emojis:
            emoji_button = ttk.Button(emojis_frame, text=emoji, command=lambda e=emoji: self.insert_emoji(e))
            emoji_button.pack(side=tk.LEFT, padx=5, pady=5)

    def insert_emoji(self, emoji):
        self.message_input.insert(tk.END, emoji)

def main():
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()

