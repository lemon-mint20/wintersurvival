import pygame
from random import randint

class Haus_gui():

    def __init__(self, screen, sg, welt):
        self.screen = screen
        self.sg = sg
        self.welt = welt

        self.img_haus = pygame.image.load("assets/haus.png")
        self.imHausImg = pygame.image.load("assets/imhaus.png")
        self.hausList = []
        #Bewegungrichtung
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def setHaus(self,welt):
        for i in range(welt.n_Haus):
            self.hausList.append(self.makeHaus())
            self.hausList[i]['x'] = randint(welt.start_x,welt.end_x)
            self.hausList[i]['y'] = randint(welt.start_y,welt.end_y)

    def makeHaus(self):
        self.h = {}
        self.h['hausImg'] = self.img_haus
        self.h['width'] = self.img_haus.get_width()
        self.h['height'] = self.img_haus.get_height()
        self.h['x'] = 0
        self.h['y'] = 0
        self.h['rect'] = pygame.Rect((self.h['x'], self.h['y'], self.h['width'], self.h['height']))
        return self.h

    def update(self):
        """Update the houses position based on the movement flag."""
        for b in range(len(self.hausList)):
            if self.moving_right:
                self.hausList[b]['x'] -= 1
            if self.moving_left:
                self.hausList[b]['x'] += 1
            if self.moving_up:
                self.hausList[b]['y'] += 1
            if self.moving_down:
                self.hausList[b]['y'] -= 1

    def check_collision(self,sg,welt):
        """überprüft, welches Haus der Spieler berührt"""
        for i in range(len(self.hausList)-1,-1,-1):
            self.collisionHaus = self.hausList[i]
            if sg.rect.collidepoint(self.collisionHaus['x'],self.collisionHaus['y']) and welt.nacht == True: #Haus muss unter Spieler sein
            #if sg.rect.constains(self.collisionHaus['rect']:
            #if sg.rect.colliderect(self.collisionHaus['rect']:
                self.screen.blit(self.imHausImg,(250,150))
            else:
                pygame.draw.rect(self.screen, (0,0,0), (0, 0, 1, 1))
                
    def blit(self):
        for i in self.hausList:
            self.h['Rect'] = pygame.Rect((i['x'],i['y'],i['width'],i['height'] ))
            self.screen.blit(self.img_haus,self.h['Rect'])
