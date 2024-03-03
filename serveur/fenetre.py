import tkinter as tk
import tkinter.ttk as ttk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("MyChat")
        self.master.geometry("990x660+50+50")
        self.master.configure(bg="salmon")

        # Barre de menu
        self.menu_bar = tk.Menu(self.master)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Paramètres")
        self.settings_menu.add_command(label="Changer de compte")
        self.settings_menu.add_separator()
        self.settings_menu.add_command(label="Déconnexion")
        self.menu_bar.add_cascade(label="Options", menu=self.settings_menu)

        self.master.config(menu=self.menu_bar)

        # Cadre principal
        self.main_frame = tk.Frame(self.master, bg="salmon")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Liste des salons à gauche
        self.channels_label = tk.Label(self.main_frame, text="Salons", bg="salmon")
        self.channels_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.channels_listbox = tk.Listbox(self.main_frame, bg="salmon", selectmode=tk.SINGLE)
        self.channels_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # Ajouter des salons avec des emojis
        self.add_channel("Sport", "⚽")
        self.add_channel("Cuisine", "🍳")
        self.add_channel("Actualités", "📰")

        # Liste d'amis à droite
        self.friends_label = tk.Label(self.main_frame, text="Amis", bg="salmon")
        self.friends_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.friends_listbox = tk.Listbox(self.main_frame, bg="salmon")
        self.friends_listbox.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

        # Liste des canaux au centre
        self.channels_treeview = ttk.Treeview(self.main_frame)
        self.channels_treeview["columns"] = ("Channel", "Users")
        self.channels_treeview.column("#0", width=120, minwidth=120)
        self.channels_treeview.column("Channel", anchor=tk.W, width=200)
        self.channels_treeview.column("Users", anchor=tk.W, width=200)
        self.channels_treeview.heading("#0", text="ID", anchor=tk.W)
        self.channels_treeview.heading("Channel", text="Channel", anchor=tk.W)
        self.channels_treeview.heading("Users", text="Users", anchor=tk.W)
        self.channels_treeview.grid(row=0, column=1, rowspan=2, padx=5, pady=5, sticky="nsew")

        # Redimensionnement automatique des cellules du cadre principal
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

    def add_channel(self, name, emoji):
        self.channels_listbox.insert(tk.END, f"{emoji} {name}")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()

