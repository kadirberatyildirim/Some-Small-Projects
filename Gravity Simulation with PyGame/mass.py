#!/usr/bin/env python

import pygame

planetPictures = []
for i in list(range(1, 9)):
    planetPictures.append(pygame.image.load('Images/Planet' + str(i) + '.png'))
    
meteorPictures = []
for i in list(range(1, 9)):
    meteorPictures.append(pygame.image.load('Images/Meteor' + str(i) + '.png'))
    
class Mass(object):
    def __init__(self, currentPos, velocity, typeOfMass = "Planet", scale = [10, 10], massPicture = 0):
        self.currentPos, self.velocity, self.type, self.scale, self.massPicture = currentPos, velocity, typeOfMass, scale, massPicture
        
    def draw(self, win):
        self.calcNextPos()
        if self.type == "Planet":
            win.blit(pygame.transform.scale(planetPictures[self.massPicture], self.scale), (self.currentPos))
            self.currentPos = self.nextPos
        else:
            win.blit(pygame.transform.scale(meteorPictures[self.massPicture], self.scale), (self.currentPos))
            self.currentPos = self.nextPos
        
    def calcNextPos(self):
#===============================================================================G constant and central mass should be given
        G = 6.674 * 10**(-11)
        M = 1.989 * 10**30
#===============================================================================Distance to the central mass needs to be calculated
        x = (800 - self.currentPos[0]) * 10**39
        y = (450 - self.currentPos[1]) * 10**39
        r = (x**2 + y**2)**0.5
#===============================================================================Acceleration needs to be calculated
        accx = G * M * x / r**(3/2)
        accy = G * M * y / r**(3/2)
        self.acceleration = [accx, accy]
#===============================================================================
        x = self.currentPos[0] + self.velocity[0] + 0.5 * self.acceleration[0]
        y = self.currentPos[1] + self.velocity[1] + 0.5 * self.acceleration[1]
        self.nextPos = [x, y]
#===============================================================================Velocity needs to be updated for the next loop
        self.velocity[0] = self.velocity[0] + self.acceleration[0]
        self.velocity[1] = self.velocity[1] + self.acceleration[1]
        
    def massInfo(self):
        return ("Mass type: {}, Initial position: {}, Initial velocity: {}, Scale: {}, Picture #: {}".format(self.type, str(self.currentPos), str(self.velocity), str(self.scale), str(self.massPicture)))
    