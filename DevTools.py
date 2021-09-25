# Description: The dev tools handler
# Author: Jacob Maughan

# Local Imports
from Enums import Direction

class DevTools():
    def __init__(self, game, window, camera, entityHandler, objectHandler):
        self.game = game
        self.window = window
        self.camera = camera
        self.entityHandler = entityHandler
        self.objectHandler = objectHandler

        self.active = False
        self.selections = [[20, 20, 'Force Quit', False], [20, 50, 'Key Logger', False], [20, 80, 'Speed', False], [20, 110, 'Free Cam', False]]
        self.currentSelection = 0
        self.keyPressed = ''

    def tick(self):
        pass

    def render(self):
        if self.active:
            self.window.drawRect((10, 10, 250, 500), (107, 107, 107))
            for i in range(len(self.selections)):
                if i == self.currentSelection:
                    if self.selections[i][3]:
                        self.window.drawText(self.selections[i][0], self.selections[i][1], self.selections[i][2] + ': Active', (255, 255, 255))
                    else:
                        self.window.drawText(self.selections[i][0], self.selections[i][1], self.selections[i][2], (255, 255, 255))
                else:
                    if self.selections[i][3]:
                        self.window.drawText(self.selections[i][0], self.selections[i][1], self.selections[i][2] + ': Active', (0, 0, 0))
                    else:
                        self.window.drawText(self.selections[i][0], self.selections[i][1], self.selections[i][2], (0, 0, 0))
            if self.selections[1][3]:
                self.window.drawText(20, 480, str(self.keyPressed), (255, 0, 255))
    
    def toggleActive(self):
        self.active = not self.active
    
    def changeSelection(self, direction):
        if direction == Direction.UP:
            if self.currentSelection == 0: self.currentSelection = len(self.selections)
            else: self.currentSelection -= 1
        elif direction == Direction.DOWN:
            if self.currentSelection == len(self.selections): self.currentSelection = 0
            else: self.currentSelection += 1

    def select(self):
        self.selections[self.currentSelection][3] = not self.selections[self.currentSelection][3]
        if self.currentSelection == 0:
            self.game.stop()
        if self.currentSelection == 2:
            if self.selections[2][3]:
                self.camera.speed = 20
                self.entityHandler.getEntityByID('player').speed = 20
            else:
                self.camera.speed = 1
                self.entityHandler.getEntityByID('player').speed = 5
