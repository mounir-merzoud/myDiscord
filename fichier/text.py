#!/usr/bin/env python3
"""Server for multithreaded ( asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import mysql.connector

utilisateur = {}
addresses = {} HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

db = mysql.connector.connect(
    host='localhost',
    user=' username',
    password='motdepasse123',
    database='mounir-merzoud_mydiscord'
)

cursor = db.cursor()

def accept_incoming_connections():
    """Sets up handling for incoming utilisateeur"""
    while True:
        utilisateur, utilisateur_address = SERVER.accept()
        print("%s:%s connicxion." % utilisateur_address)
        utilisateur.send(bytes("Greeting from the cave" + "Now type your name and press enter!", "utf8"))
        addresses[utilisateur] = utilisateur_address
        Thread(target=handle_utilisateur, args=(utilisateur,)).start()

def handle_utilisateur(utilisateur):
    """handles a single client connection."""     
    pass  