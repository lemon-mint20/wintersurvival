import pygame
import time
import shelve

file = shelve.open('mydata')
settings = {'width': 15000, 'height': 15000, 'duration': 300}
file['settings'] = settings
print('Startwerte:',list(file.values()))

class WeltSetting():
       def __init__(self):
           """Initialize the world's settings."""
           self.world_width = file['settings']['width']
           self.world_height = file['settings']['height']
           self.dauer = file['settings']['duration']#die Dauer von Tag und Nacht
          # self.tag = file['settings']['Tag'] #Anzahl der Tage
           self.n_Haus = None #wie viele Häuser spawnen sollen
           self.n_Baum = None #wie viele Bäume spawnen sollen
           self.start_x = None #ab wo sollen guiObjekte spawnwn
           self.start_y = None ##ab wo sollen guiObjekte spawnwn
           self.end_x = None #bis wo sollen guiObjekte spawnwn
           self.end_y = None ##bis wo sollen guiObjekte spawnwn
           
           self.farbe = (250,250,250)
           self.startZeit = time.time()
           self.nacht = False
           self.spanne = None
           self.day = 0 #wie viele Tage man lebt

       def update(self):
           """Tageszeit wechselt regelmäßig"""
           nacht = False
           aktuell = time.time()
           spanne = round(aktuell) - round(self.startZeit)
           if spanne == self.dauer and self.nacht == False: #spanne: Dauer von Tag,Nacht
              self.farbe = (100,100,180) #nacht
              self.startZeit = time.time()
              self.nacht = True
           elif spanne == self.dauer:
              self.farbe = (230,230,250) #tag
              self.startZeit = time.time()
              self.day += 1
              self.nacht = False
              
       def berechne(self):
              file = shelve.open('mydata')
              file['settings']
              print('NeueWerte:',list(file.values()))
              self.n_Haus = round((self.world_width * self.world_height)/4000000)
              self.n_Baum = round((self.world_width * self.world_height)/100000)
              self.start_x = round(-(self.world_width)/2)
              self.start_y = round(-(self.world_height)/2)
              self.end_x = round(self.world_width - (self.world_width/2))
              self.end_y = round(self.world_height - (self.world_height/2))
              print('Bäume:',self.n_Baum, ' Häuser:',self.n_Haus)
              file.close()
                                   
