# Description: Handles the pygame window
# Author: Jacob Maughan

# Lib Imports
import pygame
from pygame import freetype

class Window():
    def __init__(self, version):
        # Initialize windows vars & create window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width, self.height = self.screen.get_size()

        # Set window settings
        pygame.display.set_caption('MonFrame - ' + version)
        #pygame.display.set_icon('./assets/art/icon.png')
        pygame.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))

        # Create font/fonts
        self.font = pygame.freetype.SysFont('Arial', 30)

    # Fill entire screen
    def fillScreen(self, color):
        self.screen.fill(color)

    # Draw a rectangle to the screen
    def drawRect(self, rect, color):
        pygame.draw.rect(self.screen, color, rect)

    # Draw a sprite to the screen
    def drawSprite(self, x, y, sprite):
        self.screen.blit(sprite, (x, y))
    
    # Draw text to the screen
    def drawText(self, x, y, text, color):
        self.font.render_to(self.screen, (x, y), text, color)