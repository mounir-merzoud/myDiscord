import socket
import threading
import wave
import pyaudio

HOST = "10.10.106.14"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
surnoms = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            # Si le message commence par "AUDIO:", alors c'est un message vocal
            if message.startswith(b"AUDIO:"):
                # Traitez le message vocal ici (stockage, transmission à d'autres clients, etc.)
                pass
            else:
                print(f"{surnoms[clients.index(client)]} dit: {message.decode()}")
                broadcast(message)
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
        broadcast(f"{surnom} ".encode("utf-8"))
        client.send(" ".encode("utf-8"))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Attente de connexion...")
recevoir()
