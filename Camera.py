# Descrition: Handles the game viewing camera
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

class Camera():
    def __init__(self, window):

        # Initilize Vars
        self.rect = Rect(0, 0, window.width, window.height)
        self.velX = 0
        self.velY = 0
        self.speed = 1
    
    def tick(self):
        self.rect.x += self.velX * self.speed
        self.rect.y += self.velY * self.speed
    
    def moveToObject(self, object):
        self.velX = (object.rect.x - self.rect.x - ((self.rect.width - object.rect.width) / 2)) / 20
        self.velY = (object.rect.y - self.rect.y - ((self.rect.height - object.rect.height) / 2)) / 20
    
    def moveToCoord(self, x, y):
        self.velX = x - self.rect.x / 20
        self.velY = y - self.rect.y / 20
    
    def setToObject(self, object):
        self.rect.x = object.rect.x
        self.rect.y = object.rect.y
    
    def setToCoord(self, x, y):
        self.rect.x = x
        self.rect.y = y