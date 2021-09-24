# Description: The player entity
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

class PlayerEntity():
    def __init__(self):
        self.rect = Rect(0, 0, 50, 50)

        self.ID = 'player'
        self.velX = 0
        self.velY = 0
        self.speed = 5

    def tick(self, tickCount):
        self.rect.x += self.velX * self.speed
        self.rect.y += self.velY * self.speed
    
    def render(self, window, cameraRect):
        window.drawRect((self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.rect.width, self.rect.height), (0, 255, 0))