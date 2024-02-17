import mysql.connector

# Établir la connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kamelia",
    database="myDiscord"
)

# Créer un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter une requête pour récupérer les données de la table Message
cursor.execute("SELECT * FROM Message")
messages = cursor.fetchall()
print("Messages:")
for message in messages: 
    print(message)

# Exécuter une requête pour récupérer les données de la table channels
cursor.execute("SELECT * FROM channels")
channels = cursor.fetchall()
print("\nChannels:")
for channel in channels:
    print(channel)

# Exécuter une requête pour récupérer les données de la table permissions
cursor.execute("SELECT * FROM permissions")
permissions = cursor.fetchall()
print("\nPermissions:")
for permission in permissions:
    print(permission)

# Exécuter une requête pour récupérer les données de la table users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("\nUsers:")
for user in users:
    print(user)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
