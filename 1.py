import socket
from threading import Thread

def Send(client):
    while True:
        msg = input("->")
        msg = msg.encode("utf_8")
        client.send(msg)

def Reception(client):
    while True:
        requete_client = client.recv(500)
        requete_client = requete_client.decode('utf_8')
        print(requete_client)
        if not requete_client : # si on la connexion 
            print("Close")
            break


Host = "10.10.89.53"
Port = 9090
# création du Socket 
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket.bind((Host, Port))
socket.listen(1)

# Le script s'arrête jusqu'à une connection 
client, ip = socket.accept()
print("Le client d'ip", ip , "s'est connecté")

envoi = Thread(target=Send,args=[client])  # Correction ici : target au lieu de traget
recep = Thread(target=Reception,args=[client])  # Correction ici : target au lieu de traget

envoi.start()
recep.start()

client.close()
socket.close()
