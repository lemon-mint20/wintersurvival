import pygame, sys, time
from pygame.locals import *

#pygame.mixer.init()
#pygame.mixer.music.load('Gewitter.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()
#pygame.mixer.init()
#sound = pygame.mixer.Sound('############')
#sound.play()

class HausNacht():
    def __init__(self,screen,hg,sd):
        self.screen = screen
        self.hg = hg
        self.sd = sd
        self.startZeit = time.time()
        self.imHausImg = pygame.image.load('imhaus.png')
        self.x = 0
        self.y = 0

    def blit(self):
        self.screen.blit(self.imHausImg,(200,0))
        
    """
#das hat nicht funktioniert
    def blit(self):
        if self.hg.collision == True:
            self.screen.blit(self.imHausImg,(0,0))
            for b in range(len(self.hg.hausList)):
                self.hg.hausList[b]['x'] += 1
                self.hg.hausList[b]['y'] -= 1
            self.hg.collision = False
    """


