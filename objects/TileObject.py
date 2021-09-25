# Description: The tile object
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

class TileObject():
    def __init__(self, x, y, size, spriteX, spriteY, sprite, hasCollision, layer):
        self.rect = Rect(x, y, size, size)
        self.spriteX = spriteX
        self.spriteY = spriteY
        self.sprite = sprite
        self.hasCollision = hasCollision
        self.layer = layer

        self.ID = 'tile'

    def tick(self):
        pass

    def render(self, window, cameraRect):
        window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.sprite)