import pygame
import pygame.font
from stats import Stats as stats
from lose import EndGame

class Spieler_gui():
    """grafische Benutzeroberfläche für Spieler"""
    def __init__(self, screen):
        self.screen = screen
        #lade Bild und fasse in ein Rechteck
        self.image = pygame.image.load('spieler.png')
        self.rect = self.image.get_rect()

        # Position des Spielers beim Start
        self.rect.x = 400
        self.rect.y = 250

        #Bewegungrichtung
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the player's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 10
        if self.moving_left:
            self.rect.x -= 10
        if self.moving_up:
            self.rect.y -= 10
        if self.moving_down:
            self.rect.y += 10

    def blit(self):
        self.screen.blit(self.image, self.rect)


class SpielerDaten():
    def __init__(self, welt):
        self.welt = welt

        self.energie = 1000
        self.strecke = 0
        self.inventar = {'Feuer' : 10, 'Nahrung' : 20}
        self.hunger = False
        self.kalt = False
        # fuer datei gamefunction
        self.eat = False
        self.fire = False

    def update(self,stats):
        if self.eat and self.inventar['Nahrung'] >= 1:
            self.energie += 200
            self.inventar['Nahrung'] -= 1
            stats.prep_nahrung()
            self.eat = False
        if self.fire and self.inventar['Feuer'] >= 1:
            self.energie += 200
            self.inventar['Feuer'] -= 1
            stats.prep_feuer()
            self.fire = False
        if self.energie == 0:
            a = EndGame()
            print('Energie = 0, Verloren')
