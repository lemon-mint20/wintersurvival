import pygame, sys


def check_events(stats,sg,hg,bg,sd):
    """hier werden alle events überprüft (Tastatur-, Mausbefehle, etc. """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            stats.prep_energie()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                sg.moving_up = True
                hg.moving_up = True
                bg.moving_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                sg.moving_down = True
                hg.moving_down = True
                bg.moving_down = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                sg.moving_left = True
                hg.moving_left = True
                bg.moving_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                sg.moving_right = True
                hg.moving_right = True
                bg.moving_right = True
            elif event.key == pygame.K_e:
                sd.eat = True
            elif event.key == pygame.K_f:
                sd.fire = True
                
        elif event.type == pygame.KEYUP:
            stats.prep_energie()
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                sg.moving_up = False
                hg.moving_up = False
                bg.moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                sg.moving_down = False
                hg.moving_down = False
                bg.moving_down = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                sg.moving_left = False
                hg.moving_left = False
                bg.moving_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                sg.moving_right = False
                hg.moving_right = False
                bg.moving_right = False
        
            
def update_screen(welt,screen,hg,bg,sg,stats):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(welt.farbe)
    sg.blit()
    bg.blit()
    hg.blit()
    stats.blit()
    hg.check_collision(sg,welt)
    pygame.display.flip()

