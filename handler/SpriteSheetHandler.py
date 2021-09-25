# Description: Handles spritesheets
# Author: Jacob Maughan

# Lib Imports
import pygame

class SpriteSheetHandler():
    def __init__(self, sheet):
        # Init
        self.spriteSheet = pygame.image.load(sheet).convert()
    
    # Get specific sprite from loaded sprite sheet
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
        image.set_colorkey((0, 0, 0))
        return image
    
    # Get array of sprites from sprite sheet sprites[y][x]
    def getImageArray(self, width, height, scaleWidth, scaleHeight):
        sprites = [[]]
        spriteY = 0
        y = 0
        while spriteY < self.spriteSheet.get_height():
            spriteX = 0
            x = 0
            while spriteX < self.spriteSheet.get_width():
                sprites[y].append(self.getImage(spriteX, spriteY, width, height))
                sprites[y][x] = pygame.transform.scale(sprites[y][x], (scaleWidth, scaleHeight))
                spriteX += width
                x += 1
            sprites.append([])
            spriteY += height
            y += 1
        return sprites