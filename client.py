import socket
from threading import Thread

def Send(socket):
    while True:
        msg = input('->')
        msg = msg.encode('utf-8')
        socket.send(msg)

def Reception(socket):
    while True:
        requete_server = socket.recv(500)
        requete_server = requete_server.decode('utf-8')
        print(requete_server)

Host = "10.10.89.53"
Port = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

envoi = Thread(target=Send, args=[socket])  # Correction ici : target au lieu de traget
recep = Thread(target=Reception, args=[socket])  # Correction ici : target au lieu de traget

envoi.start()
recep.start()




    
