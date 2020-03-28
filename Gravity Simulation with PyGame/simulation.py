#!/usr/bin/env python

import pygame, random
import mass

class simulate(object):
    def __init__(self, bgPicture, allMass):
        pygame.init() 
        screenWidth = 1600
        screenHeight = 900
        #We define our window as follows...
        win = pygame.display.set_mode((screenWidth, screenHeight))
        pygame.display.set_caption("Gravity Simulation")
        
        clock = pygame.time.Clock()
        
        self.bgPicture = pygame.image.load('Images/Space' + str(bgPicture) + '.jpg')
        centralMassPicture = pygame.image.load('Images/Star1.png')
        
        def redrawSimulationWindow():
            win.blit(pygame.transform.scale(self.bgPicture, (1600, 900)), (0, 0))
            win.blit(pygame.transform.scale(centralMassPicture, (20, 20)), (screenWidth/2 - 10, screenHeight/2 - 10))
            if masses:
                for massy in masses:
                    massy.draw(win)
            pygame.display.update()
        
        masses = allMass
        #==================================================================================Sample Masses
        #masses.append(mass.Mass([800, 50], [10, 0], "Planet"))
        #masses.append(mass.Mass([700, 450], [0, -10]))
        #==================================================================================
        massLoop = 0
        run = True
        while run:
            clock.tick(60)
            
            if massLoop > 0:
                massLoop += 1
            if massLoop > 15:
                massLoop = 0
            
            if masses:
                for massy in masses:
                    if massy.currentPos[0] > screenWidth + 150 or massy.currentPos[0] < -150:
                        masses.pop(masses.index(massy))
                    elif massy.currentPos[1] > screenHeight + 150 or massy.currentPos[1] < -150:
                        masses.pop(masses.index(massy))
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
        #=================================================================================Key Press Events
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_p] and massLoop == 0:
                #masses.append(mass.Mass())
                massLoop = 1
        #=================================================================================
            redrawSimulationWindow()
            
        pygame.quit()