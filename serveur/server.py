
import socket
import threading

<<<<<<< HEAD
HOST ="10.10.99.2"
=======
HOST ="10.10.101.10"

>>>>>>> message
port =9090
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, port))  
server.listen()

clients = []
surnoms = []

def broadcast(message): 
    for client in clients:
        client.send(message)

def handle(client):
    while True :
        try:
            message = client.recv(1024)
            print(f"{surnoms[clients.index(client)]} dit: {message.decode()}")
            broadcast(message)
            pass
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            surnom = surnoms[index]
            surnoms.remove(surnom)
            break

def recevoir():
    while True:
        client, address = server.accept()
        print(f"Connecté avec {str(address)}")
        client.send("SURNOM".encode("utf-8"))
        surnom = client.recv(1024).decode("utf-8")
        surnoms.append(surnom)
        clients.append(client)
        print(f"Le surnom du client est {surnom}")
        broadcast(f"{surnom} connecté au serveur\n".encode("utf-8"))
        client.send("Connecté au serveur ".encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("attente de connexion...")

recevoir()
