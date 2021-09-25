# Description: The sprite object
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

class SpriteObject():
    def __init__(self, x, y, size, spriteX, spriteY, sprite):
        self.rect = Rect(x, y, size, size)
        self.spriteX = spriteX
        self.spriteY = spriteY
        self.sprite = sprite
        
        self.ID = 'sprite'
        self.layer = 2

    def tick(self):
        pass

    def render(self, window, cameraRect):
        window.drawSprite(self.rect.x, self.rect.y, self.sprite)