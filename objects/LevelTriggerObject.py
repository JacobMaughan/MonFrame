# Description: The trigger object
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

class LevelTriggerObject():
    def __init__(self, x, y, width, height, newMap, player, newX, newY, newDirection, mapHandler):
        self.rect = Rect(x, y, width, height)
        self.player = player
        self.newMap = newMap
        self.newX = newX
        self.newY = newY
        self.newDirection = newDirection
        self.mapHandler = mapHandler

        self.ID = 'levelTrigger'
        self.debug = False

    def tick(self):
        pass

    def render(self, window, cameraRect):
        if self.debug:
            window.drawRect((self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.rect.width, self.rect.height), (255, 0, 0))

    def loadMap(self):
        self.mapHandler.loadMap(self.newLevel)
        self.player.rect.x = self.newX
        self.player.rect.y = self.newY
        self.player.direction = self.newDirection