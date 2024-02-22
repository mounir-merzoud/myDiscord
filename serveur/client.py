import socket
import socket
import threading
import tkinter.scrolledtext
from tkinter import simpledialog

HOST ="192.168.136.1"
port =9090

class Client:
    def ___init__(self , host , port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        msg = tkinter.Tk()
        msg.withdraw()
        self.surnom = simpledialog.askstring("surnom", "donnez votre surnom s'il vous plait" ,parent=msg)
        self.qui_done = False
        self.runnig = True
        gui_thread = threading.Thread(target=self.gui_loop)
        recevoir_thread = threading.Thread(target=self.recevoir)
        gui_thread.start()
        recevoir_thread.start()
    def gui_loop(self):
        self.win = tkinter.TK()
        self.win.config(bg = "cyan")
        self.chat_label = tkinter.label(self.win, text="Chat",bg="cyan")
        self.chat_label.configure(font="arial 12")
        self.chat_label.pak(padx=20 , pady=5)

        self.text_area = tkinter.scrolledtext(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")
        self.msg_label = tkinter.Label(self.win , text="Message", bg="cyan")
        self.msg_label.config(font ="arial 12")
        self.msg_label.pack(padx = 20, pady=5)
        self.saisit = tkinter.Text(self.win, height=3)
        self.saisit.pack(padx= 20, pady= 5)
        self.btn_envoie = tkinter.Button(self.win, text="Envoyer", command=self.ecrire)
        self.btn_envoie.config(font="arial 12")
        self.btn_envoie.pack(padx=20 , pady=5)
        self.gui_done=True
        self.win.protocol("WM_DELETE_WINDOW" ,self.stop)
        self.win.minloop()
    def ecrire(self):
        message = f"(self.surnom) : {self.saisit.get('1.0' , 'end')}"
        self.saisit.delete('1.0' , 'end')
    def stop(self):
        self.running =False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def recevoir(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if message == 'surnom':
                    self.sock.send(self.surnom.encode("utf-8"))
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")
                        self.text_area.insert("end", message)
                        self.text_area.yview("end")
                        self.text_area.config(state= "disabled")

            except ConnectionAbortedError:
                break
            except:
                print("Erreur")
                self.sock.close()
                break
client = Client()
