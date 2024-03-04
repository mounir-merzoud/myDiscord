import mariadb

def connect_to_database():
    try:
        connection = mariadb.connect(
            user='mounir-merzoudy',
            password='Mounir-1992',
            host='82.165.185.52',
            port=3306,
            database='mounir-merzoud_myDiscord'
        )
        return connection
    except mariadb.Error as e:
        print(f"Erreur de connexion à la base de données : {e}")
        return None
