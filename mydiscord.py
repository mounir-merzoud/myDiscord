import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow  # Importez la classe générée à partir de votre fichier .ui

class MyDiscordApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation de l'interface utilisateur
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connectez ici les signaux et les slots, et ajoutez toute logique nécessaire

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDiscordApp()
    window.show()
    sys.exit(app.exec_())
