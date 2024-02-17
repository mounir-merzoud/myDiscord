import pygame
from pygame.locals import *
import sys

# Initialiser Pygame
pygame.init()

# Définir les couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Définir la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Créer la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Discord')

# Charger l'image de fond
background_img = pygame.image.load('images/_6708713a-2b22-4441-a593-4896158ce7de.jpg')

# Redimensionner l'image de fond à la taille de la fenêtre
background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Charger la police personnalisée
custom_font = pygame.font.Font('images/CFAzteques-Regular.ttf', 46)

font = pygame.font.Font(None, 32)




def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main():
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    while True:
        # Dessiner l'image de fond
        window.blit(background_img, (0, 0))
        
        # Afficher le texte "Welcome" avec la police personnalisée
        draw_text('Welcome', custom_font, BLACK, window, 250, 30)
        draw_text('First Name:', font, BLACK, window, 140, 220)
        draw_text('Last Name:', font, BLACK, window, 140, 270)
        draw_text('Email:', font, BLACK, window, 140, 320)
        draw_text('Password:', font, BLACK, window, 140, 370)

        # Afficher les entrées de texte
        pygame.draw.rect(window, WHITE, (300, 220, 200, 30))
        pygame.draw.rect(window, WHITE, (300, 270, 200, 30))
        pygame.draw.rect(window, WHITE, (300, 320, 200, 30))
        pygame.draw.rect(window, WHITE, (300, 370, 200, 30))

        draw_text(first_name, font, BLACK, window, 155, 55)
        draw_text(last_name, font, BLACK, window, 155, 105)
        draw_text(email, font, BLACK, window, 155, 155)
        draw_text(password, font, BLACK, window, 155, 205)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    # Enregistrer ou connecter l'utilisateur
                    print("First Name:", first_name)
                    print("Last Name:", last_name)
                    print("Email:", email)
                    print("Password:", password)
                elif event.key == K_BACKSPACE:
                    # Supprimer le dernier caractère de l'entrée de texte
                    if email:
                        email = email[:-1]
                    elif password:
                        password = password[:-1]
                    elif first_name:
                        first_name = first_name[:-1]
                    elif last_name:
                        last_name = last_name[:-1]
                else:
                    # Ajouter le caractère à l'entrée de texte
                    if len(email) < 50:
                        email += event.unicode
                    elif len(password) < 50:
                        password += event.unicode
                    elif len(first_name) < 50:
                        first_name += event.unicode
                    elif len(last_name) < 50:
                        last_name += event.unicode

        pygame.display.update()

if __name__ == '__main__':
    main()


font = pygame.font.Font(None, 32)