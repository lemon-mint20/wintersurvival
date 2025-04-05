import pygame
import shelve

import game_functions as gf
from weltSetting import *
from stats import Stats
from spieler import *
from haus import Haus_gui
from baum import Baum_gui
from imhaus import*

def run_game():
    #Initialisiere alle Klassenobjekte
    pygame.init()
    mainClock = pygame.time.Clock()
    welt = WeltSetting()
    sd = SpielerDaten(welt)
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_icon(pygame.image.load("assets/spieler.png"))
    pygame.display.set_caption('SurvivalGame')
    sg = Spieler_gui(screen)
    hg = Haus_gui(screen, sg, welt)
    bg = Baum_gui(screen, sg, welt)
    stats = Stats(screen, sd, sg, welt)
    welt.berechne()
    hg.setHaus(welt)
    bg.setBaum(welt)
    #start the mainloop for the game
    while True:
        gf.check_events(stats,sg,hg,bg,sd)
        stats.check_spielerDaten(sg,sd,welt)
        #sg.update()
        welt.update()
        hg.update()
        bg.update()
        sd.update(stats)
        gf.update_screen(welt,screen,hg,bg,sg,stats)
        mainClock.tick(25)
        
#run_game() #wird in klasse HomeScreen ausgeführt
