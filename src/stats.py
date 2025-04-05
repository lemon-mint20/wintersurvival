import pygame
import time

class Stats():
    def __init__(self, screen, sd, sg, welt):
        """Statusanzeige"""
        self.screen = screen
        self.sd = sd
        self.sg = sg
        self.welt = welt
        
        self.rect_color = (100,100,100)
        self.text_color = (230,230,230)
        self.msg_color = (100,250,100)
        self.font = pygame.font.SysFont(None, 20)
        self.foodimg = pygame.image.load("assets/snickers.png")
        self.foodrect = self.foodimg.get_rect(center=(450,20))

        self.startZeit = time.time()
        self.prep_energie()
        self.prep_strecke()
        self.prep_nahrung()
        self.prep_feuer()
        self.prep_message()

    def prep_energie(self):
        """Turn the energy into a rendered image."""
        energie_str = str(self.sd.energie)
        self.energie_img = self.font.render('Energie: %s' % energie_str, True, self.text_color, self.rect_color)
        # Display the energie at the top left of the screen
        self.energie_rect = self.energie_img.get_rect(center=(100,25))

    def prep_strecke(self):
        """Strecke, die der Spieler hinter sich hat"""
        strecke_str = str(self.sd.strecke)
        self.strecke_img = self.font.render('Strecke: %s' % strecke_str, True, self.text_color, self.rect_color)
        self.strecke_rect = self.strecke_img.get_rect(center=(250,25))

    def prep_nahrung(self):
        """Turn the foodcount into a rendered image"""
        nahrung_str = str(self.sd.inventar['Nahrung'])
        self.nahrung_img = self.font.render(nahrung_str,True, self.text_color, self.rect_color)
        self.nahrung_rect = self.nahrung_img.get_rect(center=(550,18))

    def prep_feuer(self):
        """Turn the firecount into a rendered image"""
        feuer_str = str(self.sd.inventar['Feuer'])
        self.feuer_img = self.font.render('Feuer: %s' % feuer_str,True, self.text_color, self.rect_color)
        self.feuer_rect = self.feuer_img.get_rect(center=(450,55))

    def prep_message(self):
        """Nachricht wird eingeblendet""" #msg: messages
        self.msg_kalt = self.font.render('Es ist kalt. Mach Feuer. (key: f)',True, self.msg_color, self.rect_color)
        self.msg_rect = self.msg_kalt.get_rect(topleft=(620,30))
        self.msg_hunger = self.font.render('Du hast hunger. Iss ein Snickers. (key: e)',True, self.msg_color, self.rect_color)
        self.msg_rect = self.msg_hunger.get_rect(topleft=(620,30))
        #self.msg_weltende = self.font.render('',True, self.msg_color, self.rect_color)
        #self.msg_rect = self.msg_weltende.get_rect(center=(620,30))

        #später einfügen: 'weltende erreicht'
    def check_spielerDaten(self,sg,sd,welt):
        if sg.moving_right or sg.moving_left or sg.moving_up or sg.moving_down:
            sd.strecke += 1
            sd.energie -= 0.5
            self.prep_strecke()
            self.prep_energie()
        elif sd.energie < 800 and welt.nacht == True:
            sd.kalt = True
            sd.hunger = True
        else:
            sd.kalt = False
            if sd.energie < 1300:
                sd.hunger = True
                sd.kalt = False
            else:
                sd.hunger = False

    def blit(self):
        pygame.draw.rect(self.screen, self.rect_color, (0, 0, 1000, 70))
        self.screen.blit(self.foodimg, self.foodrect)
        self.screen.blit(self.energie_img, self.energie_rect)
        self.screen.blit(self.strecke_img, self.strecke_rect)
        self.screen.blit(self.nahrung_img, self.nahrung_rect)
        self.screen.blit(self.feuer_img, self.feuer_rect)
        #self.screen.blit(self.msg_weltende, self.msg_rect)
        if self.sd.kalt:
            self.screen.blit(self.msg_kalt, self.msg_rect)
        elif self.sd.hunger:
            self.screen.blit(self.msg_hunger, self.msg_rect)
