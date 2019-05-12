import pygame
from pygame.locals import *
from random import randrange
from math import *
#from classes import Roles
import time

pygame.init()


class DISPLAY():
    """Tout ce qui concerne l'affichage.
       All that concern the display.     """

    def __init__(self):
        self.width  = 1280
        self.height = 720
        self.fps    = 60
        self.stopALL = False
        self.fullscreen = True


        self.win = None
        self.mask = None

        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)


        self.perfectlyScratchyFont = pygame.font.Font("Fonts/perfectly scratchy.ttf", 26)
        self.theHauntedMazeFont = pygame.font.Font("Fonts/The Haunted Maze - TTF.ttf", 26)
        self.RemoveDemoFont = pygame.font.Font("Fonts/Remove DEMO.otf", 26)

        '''
        file = open('Coords.txt', 'r+')
        self.DATA = file.readlines()
        file.close()'''
        pass

    def collide(self, point, wall):
        Px, Py = point
        intersections = 0
        for i in range(0,len(wall)):
            x,y = wall[i]
            if i == len(wall)-1:
                x1, y1 = wall[0]
            else:
                x1,y1 = wall[i+1]

            if x1 == x:
                x1 += 0.00001
            a = (y1-y) / (x1-x)
            b = y - (a*x)
            c = Py
            intersect = False
            if (Px <= x or Px <= x1) and a != 0:
                X = (c-b)/a

                if Px <= X:
                    if y > y1:
                        if y1 <= c and c <= y:
                            intersect = True
                    if y < y1:
                        if y <= c and c <= y1:
                            intersect = True
                pass

            if intersect is True:
                intersections += 1
            pass
        modulo = intersections % 2
        if modulo == 1:
            return True
        else:
            return False


    pass
display = DISPLAY()




display.win = pygame.display.set_mode((display.width, display.height))





pygame.display.set_caption("Les loup-Garous de Thiercelieux")
icon = pygame.image.load("TEXTURES/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
clock.tick(display.fps)
pygame.key.set_repeat(400, 30)
pygame.mouse.set_visible(True)

if display.fullscreen == False:
    win = pygame.display.set_mode((display.width, display.height))
else:
    win = pygame.display.set_mode((display.width, display.height), FULLSCREEN)








def menu():
    win = display.win

    def Rules():
        ''' Affiche les règles du jeu '''
        win = display.win

        locate_BoutonDroit = 'TEXTURES/ICONS/arrow right.png'
        locate_BoutonGauche = 'TEXTURES/ICONS/arrow left.png'
        locate_BoutonRetour = 'TEXTURES/ICONS/retour.png'
        locate_slides = [
        'TEXTURES/Règles/Règles-1.png',
        'TEXTURES/Règles/Règles-2.png',
        'TEXTURES/Règles/Règles-3.png',
        'TEXTURES/Règles/Règles-4.png' ]

        slides = []
        for i in range(0,4):
            image = pygame.image.load(locate_slides[i])
            modified = pygame.transform.smoothscale(image, (display.height, display.height))
            slides.append( modified )
            pass
        slidesposx = (display.width/2) - (display.height/2)
        slidesposy = 0

        class RightButton():
            ''' Classe sur le bouton Droit. '''
            def __init__(self):
                self.factor = 1 # facteur d'agrandissement de l'image
                self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
                self.thisNoMod = pygame.image.load(locate_BoutonDroit) # image brute
                self.w = 64 # largeur de l'image
                self.h = 64 # hauteur
                self.this = pygame.transform.scale(self.thisNoMod, (self.w*self.factor, self.h*self.factor)) # image agrandie
                self.initx = (display.width - 50) # position initiale (centre)
                self.inity = (display.height/2) #
                self.x = self.initx - (self.w*self.factor/2) # position x de l'image
                self.y = self.inity - (self.h*self.factor/2) # position y
                pass
        rightButton = RightButton()

        class LeftButton():
            ''' Classe sur le bouton Gauche. '''
            def __init__(self):
                self.factor = 1 # facteur d'agrandissement de l'image
                self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
                self.thisNoMod = pygame.image.load(locate_BoutonGauche) # image brute
                self.w = 64 # largeur de l'image
                self.h = 64 # hauteur
                self.this = pygame.transform.scale(self.thisNoMod, (self.w*self.factor, self.h*self.factor)) # image agrandie
                self.initx = 50 # position initiale (centre)
                self.inity = (display.height/2) #
                self.x = self.initx - (self.w*self.factor/2) # position x de l'image
                self.y = self.inity - (self.h*self.factor/2) # position y
                pass
        leftButton = LeftButton()

        class ReturnButton():
            ''' Classe sur le bouton Gauche. '''
            def __init__(self):
                self.factor = 1 # facteur d'agrandissement de l'image
                self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
                self.thisNoMod = pygame.image.load(locate_BoutonRetour) # image brute
                self.w = 512/4 # largeur de l'image
                self.h = 316/4 # hauteur
                self.this = pygame.transform.scale(self.thisNoMod, (int(self.w*self.factor), int(self.h*self.factor))) # image agrandie
                self.initx = 30 + (self.w/2) # position initiale (centre)
                self.inity = display.height - (self.h/2) - 10 #
                self.x = self.initx - (self.w*self.factor/2) # position x de l'image
                self.y = self.inity - (self.h*self.factor/2) # position y
                pass
        returnButton = ReturnButton()

        slide = 0
        stop = False
        while stop is not True:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # ---------Gestion de l'agrandissement des boutons--------- #
            # Pour rightButton :
            rightButton.factor = 1 + ( (sin(rightButton.sub)**2)*0.2 )
            if (mouse_x >= rightButton.x and mouse_x <= rightButton.x+rightButton.w and
               mouse_y >= rightButton.y and mouse_y <= rightButton.y+rightButton.h)    :
                if rightButton.sub <= (pi/2):
                    rightButton.sub += pi/60
            else:
                if rightButton.sub >= 0:
                    rightButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
            if rightButton.sub >= (pi/2):
                rightButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
            rightButton.x = rightButton.initx - (rightButton.w*rightButton.factor/2)
            rightButton.y = rightButton.inity - (rightButton.h*rightButton.factor/2)
            rightButton.this = pygame.transform.scale(rightButton.thisNoMod, (int(rightButton.w*rightButton.factor), int(rightButton.h*rightButton.factor)))

            # Pour leftButton :
            leftButton.factor = 1 + ( (sin(leftButton.sub)**2)*0.2 )
            if (mouse_x >= leftButton.x and mouse_x <= leftButton.x+leftButton.w and
               mouse_y >= leftButton.y and mouse_y <= leftButton.y+leftButton.h)    :
                if leftButton.sub <= (pi/2):
                    leftButton.sub += pi/60
            else:
                if leftButton.sub >= 0:
                    leftButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
            if leftButton.sub >= (pi/2):
                leftButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
            leftButton.x = leftButton.initx - (leftButton.w*leftButton.factor/2)
            leftButton.y = leftButton.inity - (leftButton.h*leftButton.factor/2)
            leftButton.this = pygame.transform.scale(leftButton.thisNoMod, (int(leftButton.w*leftButton.factor), int(leftButton.h*leftButton.factor)))

            # Pour returnButton :
            returnButton.factor = 1 + ( (sin(returnButton.sub)**2)*0.2 )
            if (mouse_x >= returnButton.x and mouse_x <= returnButton.x+returnButton.w and
               mouse_y >= returnButton.y and mouse_y <= returnButton.y+returnButton.h)    :
                if returnButton.sub <= (pi/2):
                    returnButton.sub += pi/60
            else:
                if returnButton.sub >= 0:
                    returnButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
            if returnButton.sub >= (pi/2):
                returnButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
            returnButton.x = returnButton.initx - (returnButton.w*returnButton.factor/2)
            returnButton.y = returnButton.inity - (returnButton.h*returnButton.factor/2)
            returnButton.this = pygame.transform.scale(returnButton.thisNoMod, (int(returnButton.w*returnButton.factor), int(returnButton.h*returnButton.factor)))
            # ---------                  FIN                  --------- #


            win.fill(display.BLACK)
            win.blit(slides[slide], (slidesposx, slidesposy))
            win.blit(rightButton.this, (rightButton.x, rightButton.y))
            win.blit(leftButton.this, (leftButton.x, leftButton.y))
            win.blit(returnButton.this, (returnButton.x, returnButton.y))
            pygame.display.flip()
            clock.tick(display.fps)

            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:	#Si clic gauche
                        if (mouse_x >= returnButton.x and mouse_x <= returnButton.x+returnButton.w and
                           mouse_y >= returnButton.y and mouse_y <= returnButton.y+returnButton.h)    :
                            stop = True
                            pass
                        if (mouse_x >= rightButton.x and mouse_x <= rightButton.x+rightButton.w and
                           mouse_y >= rightButton.y and mouse_y <= rightButton.y+rightButton.h)    :
                            if slide < 3:
                                slide += 1
                            pass
                        if (mouse_x >= leftButton.x and mouse_x <= leftButton.x+leftButton.w and
                           mouse_y >= leftButton.y and mouse_y <= leftButton.y+leftButton.h)    :
                            if slide > 0:
                                slide -= 1
                            pass
                if event.type == KEYDOWN:
                    if event.key == K_F11: # Gestion fullscreen
                        display.fullscreen = not display.fullscreen
                        if display.fullscreen == False:
                            win = pygame.display.set_mode((display.width, display.height))
                        else:
                            win = pygame.display.set_mode((display.width, display.height), FULLSCREEN)
                            pass
                        pass
                    if event.key == K_RIGHT:
                        if slide < 3:
                            slide += 1
                    if event.key == K_LEFT :
                        if slide > 0:
                            slide -= 1
                    pass
            pass
        pass
    '''Fin Rules'''

    locate_splash = 'TEXTURES/Splashscreen.png'
    locate_fond = 'TEXTURES/fond_menu.jpg'
    locate_BoutonJouer = 'TEXTURES/Bouton Jouer.png'
    locate_BoutonQuitter = 'TEXTURES/ICONS/annuler blanc.png'
    locate_BoutonInfo = 'TEXTURES/ICONS/signet blanc.png'

    pygame.display.set_caption("Les loup-Garous de Thiercelieux - Accueuil")
    fond = pygame.image.load(locate_fond)
    fond_transformed = pygame.transform.smoothscale(fond, (display.width, display.height))
    splash = pygame.image.load(locate_splash)
    splash_transformed = pygame.transform.smoothscale(splash, (display.width, display.height))
    mask = pygame.Surface((display.width, display.height))



    # Dégradé visuel au noir
    i = 0
    stop = False
    while stop is not True:
        i += pi/40
        if i >= pi/2:
            stop = True
        else:
            fond_transformed.set_alpha(sin(i)*150)
            pass

        win.fill(display.BLACK)
        win.blit(fond_transformed, (0,0))
        pygame.display.flip()
        clock.tick(120)
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                   stop = True
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                stop = True
                display.stopALL = True
                pass
        pass
    fond_transformed.set_alpha(150)




    class PlayButton():
        ''' Classe sur le bouton de jeu. '''
        def __init__(self):
            self.factor = 1 # facteur d'agrandissement de l'image
            self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
            self.thisNoMod = pygame.image.load(locate_BoutonJouer) # image brute
            self.w = 250 # largeur de l'image
            self.h = 263 # hauteur
            self.this = pygame.transform.scale(self.thisNoMod, (self.w*self.factor, self.h*self.factor)) # image agrandie
            self.initx = (display.width /2) # position initiale (centre)
            self.inity = (display.height/2) #          ''
            self.x = self.initx - (self.w*self.factor/2) # position x de l'image
            self.y = self.inity - (self.h*self.factor/2) # position y
            pass
    playButton = PlayButton()

    class ExitButton():
        ''' Classe sur le bouton servant à quitter. '''
        def __init__(self):
            self.factor = 1 # facteur d'agrandissement de l'image
            self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
            self.thisNoMod = pygame.image.load(locate_BoutonQuitter) # image brute
            self.w = 100 # largeur de l'image
            self.h = 100 # hauteur
            self.this = pygame.transform.scale(self.thisNoMod, (self.w*self.factor, self.h*self.factor)) # image agrandie
            self.initx = display.width - (self.w/2) # position initiale (centre)
            self.inity = self.h/2 #                              ''
            self.x = self.initx - (self.w*self.factor/2) # position x de l'image
            self.y = self.inity - (self.h*self.factor/2) # position y
            pass
    exitButton = ExitButton()

    class InfoButton():
        ''' Classe sur le bouton de jeu. '''
        def __init__(self):
            self.factor = 1 # facteur d'agrandissement de l'image
            self.sub = 0 # sous facteur, image de sinus pour adoucir l'agrandissement de l'image.
            self.thisNoMod = pygame.image.load(locate_BoutonInfo) # image brute
            self.w = 120 # largeur de l'image
            self.h = 120 # hauteur
            self.this = pygame.transform.scale(self.thisNoMod, (self.w*self.factor, self.h*self.factor)) # image agrandie
            self.initx = 30 + (self.w/2) # position initiale (centre)
            self.inity = display.height - (self.h/2) - 10 #
            self.x = self.initx - (self.w*self.factor/2) # position x de l'image
            self.y = self.inity - (self.h*self.factor/2) # position y
            pass
    infoButton = InfoButton()

    file = open('Coords.txt', 'w')

    pointList = []
    write = None
    stop = False

    while stop is not True:

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # ---------Gestion de l'agrandissement des boutons--------- #
        # Pour playButton :
        playButton.factor = 1 + ( (sin(playButton.sub)**2)*0.2 )
        if (mouse_x >= playButton.x and mouse_x <= playButton.x+playButton.w and
           mouse_y >= playButton.y and mouse_y <= playButton.y+playButton.h)    :
            if playButton.sub <= (pi/2):
                playButton.sub += pi/60
        else:
            if playButton.sub >= 0:
                playButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
        if playButton.sub >= (pi/2):
            playButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
        playButton.x = playButton.initx - (playButton.w*playButton.factor/2)
        playButton.y = playButton.inity - (playButton.h*playButton.factor/2)
        playButton.this = pygame.transform.scale(playButton.thisNoMod, (int(playButton.w*playButton.factor), int(playButton.h*playButton.factor)))

        # Pour exitButton :
        exitButton.factor = 1 + ( (sin(exitButton.sub)**2)*0.2 )
        if (mouse_x >= exitButton.x and mouse_x <= exitButton.x+exitButton.w and
           mouse_y >= exitButton.y and mouse_y <= exitButton.y+exitButton.h)    :
            if exitButton.sub <= (pi/2):
                exitButton.sub += pi/60
        else:
            if exitButton.sub >= 0:
                exitButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
        if exitButton.sub >= (pi/2):
            exitButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
        exitButton.x = exitButton.initx - (exitButton.w*exitButton.factor/2)
        exitButton.y = exitButton.inity - (exitButton.h*exitButton.factor/2)
        exitButton.this = pygame.transform.scale(exitButton.thisNoMod, (int(exitButton.w*exitButton.factor), int(exitButton.h*exitButton.factor)))
        # Pour infoButton :
        infoButton.factor = 1 + ( (sin(infoButton.sub)**2)*0.2 )
        if (mouse_x >= infoButton.x and mouse_x <= infoButton.x+infoButton.w and
           mouse_y >= infoButton.y and mouse_y <= infoButton.y+infoButton.h)    :
            if infoButton.sub <= (pi/2):
                infoButton.sub += pi/60
        else:
            if infoButton.sub >= 0:
                infoButton.sub -= pi/60 # on rétrécit l'image jusqu'à sa taille normale
        if infoButton.sub >= (pi/2):
            infoButton.sub = (pi/2) # on empèche qu'il ne revienne plus bas au maximum (sinon cela le fait vibrer.)
        infoButton.x = infoButton.initx - (infoButton.w*infoButton.factor/2)
        infoButton.y = infoButton.inity - (infoButton.h*infoButton.factor/2)
        infoButton.this = pygame.transform.scale(infoButton.thisNoMod, (int(infoButton.w*infoButton.factor), int(infoButton.h*infoButton.factor)))
        # ---------                  FIN                  --------- #



        win.fill(display.BLACK)
        win.blit(fond_transformed, (0,0))
        win.blit(playButton.this, (playButton.x, playButton.y))
        win.blit(exitButton.this, (exitButton.x, exitButton.y))
        win.blit(infoButton.this, (infoButton.x, infoButton.y))
        pygame.display.flip()
        clock.tick(display.fps)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:	#Si clic gauche
                    if (mouse_x >= playButton.x and mouse_x <= playButton.x+playButton.w and
                       mouse_y >= playButton.y and mouse_y <= playButton.y+playButton.h)    :
                        stop = True
                        pass
                    if (mouse_x >= exitButton.x and mouse_x <= exitButton.x+exitButton.w and
                       mouse_y >= exitButton.y and mouse_y <= exitButton.y+exitButton.h)    :
                        display.stopALL = True
                        stop = True
                        file.close()
                        exit()
                        pass
                    if (mouse_x >= infoButton.x and mouse_x <= infoButton.x+infoButton.w and
                       mouse_y >= infoButton.y and mouse_y <= infoButton.y+infoButton.h)    :
                        Rules()
                        pass
            '''if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                display.stopALL = True
                stop = True
                file.close()
                exit()
                pass'''
            if event.type == KEYDOWN:
                if event.key == K_F11: # Gestion fullscreen
                    display.fullscreen = not display.fullscreen
                    if display.fullscreen == False:
                        win = pygame.display.set_mode((display.width, display.height))
                    else:
                        win = pygame.display.set_mode((display.width, display.height), FULLSCREEN)
                        pass
                    pass
                pass
        pass

    file.close()


    # Dégradé visuel Fondu au noir
    i = pi/2
    stop = False
    while stop is not True:
        i -= pi/40
        if i <= 0:
            stop = True
        else:
            fond_transformed.set_alpha(sin(i)*150)
            pass

        win.fill(display.BLACK)
        win.blit(fond_transformed, (0,0))
        pygame.display.flip()
        clock.tick(120)
        for event in pygame.event.get():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if event.type == MOUSEBUTTONDOWN:
                   stop = True
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                stop = True
                display.stopALL = True
                pass
        pass
    fond_transformed.set_alpha(150)
    pass




def play():
    win = display.win
    locate_fond = 'TEXTURES/fond_menu2.jpg'


    fond = pygame.image.load(locate_fond)
    fond_transformed = pygame.transform.scale(fond, (display.width, display.height))



    pygame.display.set_caption("Les loup-Garous de Thiercelieux - Jeu")



    stop = False
    while stop is not True:








        win.blit(fond_transformed, (0,0))
        pygame.display.flip()



        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                stop = True
                pygame.display.set_caption("Les loup-Garous de Thiercelieux - Accueuil")
                pass
            if event.type == KEYDOWN:
                if event.key == K_F11: # Gestion fullscreen
                    display.fullscreen = not display.fullscreen
                    if display.fullscreen == False:
                        win = pygame.display.set_mode((display.width, display.height))
                    else:
                        win = pygame.display.set_mode((display.width, display.height), FULLSCREEN)
                        pass
                    pass
                pass

    pass








display.stopALL = False
while display.stopALL is False:
    menu()
    play()
    pass


''' END '''
