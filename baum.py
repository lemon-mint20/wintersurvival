import pygame
from random import randint

# screen size: 1000x600
class Baum_gui():
    def __init__(self, screen, sg, welt):
        self.screen = screen
        self.sg = sg
        self.welt = welt

        self.image_baum = pygame.image.load('baum2.png')
        self.baumList = []
        
        #Bewegungrichtung
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def setBaum(self,welt):
        for i in range(welt.n_Baum):
            self.baumList.append(self.makeBaum())
            self.baumList[i]['x'] = randint(welt.start_x,welt.end_x)
            self.baumList[i]['y'] = randint(welt.start_y,welt.end_y)

    def makeBaum(self):
        self.h = {}
        self.h['baumImg'] = self.image_baum
        self.h['width'] = self.image_baum.get_width()
        self.h['height'] = self.image_baum.get_height()
        self.h['x'] = 0
        self.h['y'] = 0
        self.h['rect'] = pygame.Rect((self.h['x'], self.h['y'], self.h['width'], self.h['height']))
        return self.h

    def update(self):
        """Update the trees position based on the movement flag."""
        for b in range(len(self.baumList)):
            if self.moving_right:
                self.baumList[b]['x'] -= 1
            if self.moving_left:
                self.baumList[b]['x'] += 1
            if self.moving_up:
                self.baumList[b]['y'] += 1
            if self.moving_down:
                self.baumList[b]['y'] -= 1

    def blit(self):
        for i in self.baumList:
            self.h['Rect'] = pygame.Rect((i['x'],i['y'],i['width'],i['height'] ))
            self.screen.blit(self.image_baum,self.h['Rect'])
