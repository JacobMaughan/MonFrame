# Description: The dev tools handler
# Author: Jacob Maughan

# Sys Imports
from math import floor
from math import ceil

# Lib Imports
from pygame import Rect
from pygame.sprite import Sprite

# Local Imports
from Enums import Direction
from Enums import GameState
from SpriteObject import SpriteObject
from TileObject import TileObject
from SpriteSheetHandler import SpriteSheetHandler

class DevTools():
    def __init__(self, game, window, camera, entityHandler, objectHandler):
        self.game = game
        self.window = window
        self.camera = camera
        self.entityHandler = entityHandler
        self.objectHandler = objectHandler

        self.active = False
        self.rect = Rect(self.window.width / 2 - 8, self.window.height / 2 - 8, 16, 16)
        self.selections = [[20, 20, 'Force Quit', False], [20, 50, 'Key Logger', False], [20, 80, 'Speed', False], [20, 110, 'Free Cam', False], [20, 140, 'Map Editor', False]]
        self.currentSelection = 0
        self.keyPressed = ''
        self.spriteSheet = SpriteSheetHandler('./assets/art/overworld.png')
        self.spriteSheetArray = self.spriteSheet.getImageArray(16, 16, 16, 16)
        self.spriteSheetArrayForTile = self.spriteSheet.getImageArray(16, 16, 16 * 4, 16 * 4)
        self.spriteSelecter = Rect(self.window.width - len(self.spriteSheetArray[0]) * 16, 0, 16, 16)
        self.selectedSprite = None
        self.currentLayer = 0
        self.hasCollision = False

        self.levelName = 'new_map'

    def tick(self):
        if self.selections[4][3]:
            if not self.objectHandler.collide(self.spriteSelecter) == []:
                for object in self.objectHandler.collide(self.spriteSelecter):
                    if object.ID == 'sprite':
                        self.selectedSprite = object

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
            if self.selections[3][3]:
                if self.selections[4][3]:
                    self.window.drawSprite(self.rect.x, self.rect.y, self.selectedSprite.sprite)
                else:
                    self.window.drawRect(self.rect, (255, 0, 0))
            if self.selections[4][3]:
                self.window.drawRect(self.spriteSelecter, (255, 0, 255))
                self.window.drawText(20, 450, 'Layer:' + str(self.currentLayer), (255, 0, 255))
                self.window.drawText(20, 480, 'Collision:' + str(self.hasCollision), (255, 0, 255))
    
    def toggleActive(self):
        self.active = not self.active
    
    def changeSelection(self, direction):
        if direction == Direction.UP:
            if self.currentSelection == 0: self.currentSelection = len(self.selections) - 1
            else: self.currentSelection -= 1
        elif direction == Direction.DOWN:
            if self.currentSelection == len(self.selections) - 1: self.currentSelection = 0
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
        if self.currentSelection == 3:
            if self.selections[4][3]:
                self.selections[3][3] = True
        if self.currentSelection == 4:
            self.selections[3][3] = True
            if self.selections[4][3]:
                self.game.gameState = GameState.MAP_EDITOR
                for y in range(len(self.spriteSheetArray)):
                    for x in range(len(self.spriteSheetArray[y])):
                        self.objectHandler.addObject(SpriteObject(x * 16 + self.window.width - len(self.spriteSheetArray[y] * 16), y * 16, 16, x, y, self.spriteSheetArray[y][x]))
            else:
                self.game.gameState = GameState.GAME
                for object in self.objectHandler.getObjectsByID('sprite'):
                    self.objectHandler.removeObject(object)
    
    def editorMove(self, direction):
        if direction == Direction.UP:
            if self.spriteSelecter.y == 0: self.spriteSelecter.y = len(self.spriteSheetArray) * 16
            else: self.spriteSelecter.y -= 16
        elif direction == Direction.DOWN:
            if self.spriteSelecter.y == len(self.spriteSheetArray) * 16: self.spriteSelecter.y = 0
            else: self.spriteSelecter.y += 16
        elif direction == Direction.LEFT:
            if self.spriteSelecter.x == self.window.width - len(self.spriteSheetArray[0]) * 16: self.spriteSelecter.x = self.window.width - 16
            else: self.spriteSelecter.x -= 16
        elif direction == Direction.RIGHT:
            if self.spriteSelecter.x == self.window.width - 16: self.spriteSelecter.x = self.window.width - len(self.spriteSheetArray[0]) * 16
            else: self.spriteSelecter.x += 16
    
    def editorEnter(self):
        x = floor(self.window.width / 2 + self.camera.rect.x)
        y = floor(self.window.height / 2 + self.camera.rect.y)
        x = floor(x / (16 * 4)) * 16 * 4
        y = floor(y / (16 * 4)) * 16 * 4
        
        objects = self.objectHandler.collide(Rect(self.rect.x + self.camera.rect.x, self.rect.y + self.camera.rect.y, self.rect.width, self.rect.height))
        if len(objects) == 1:
            if objects[0].ID == 'tile' and objects[0].layer == self.currentLayer:
                objects[0].spriteX = self.selectedSprite.spriteX
                objects[0].spriteY = self.selectedSprite.spriteY
                objects[0].sprite = self.spriteSheetArrayForTile[objects[0].spriteY][objects[0].spriteX]
                objects[0].hasCollision = self.hasCollision
            else:
                self.objectHandler.addObject(TileObject(x, y, 16 * 4, self.selectedSprite.spriteX, self.selectedSprite.spriteY, self.spriteSheetArrayForTile[self.selectedSprite.spriteY][self.selectedSprite.spriteX], self.hasCollision, self.currentLayer))
        elif len(objects) == 2:
            if objects[0].ID == 'tile' and objects[1].ID == 'tile':
                for object in objects:
                    if object.layer == self.currentLayer:
                        object.spriteX = self.selectedSprite.spriteX
                        object.spriteY = self.selectedSprite.spriteY
                        object.sprite = self.spriteSheetArrayForTile[object.spriteY][object.spriteX]
                        object.hasCollision = self.hasCollision
        else:
            self.objectHandler.addObject(TileObject(x, y, 16 * 4, self.selectedSprite.spriteX, self.selectedSprite.spriteY, self.spriteSheetArrayForTile[self.selectedSprite.spriteY][self.selectedSprite.spriteX], self.hasCollision, self.currentLayer))

    def toggleLayer(self):
        if self.currentLayer == 1: self.currentLayer = 0
        elif self.currentLayer == 0: self.currentLayer = 1
        else: self.currentLayer = 0
    
    def toggleCollision(self):
        self.hasCollision = not self.hasCollision
    
    def saveMap(self):
        tiles = []
        for object in self.objectHandler.objects:
            if object.ID == 'tile':
                tiles.append({"x": object.rect.x, "y": object.rect.y, "spriteX": object.spriteX, "spriteY": object.spriteY, "collision": object.hasCollision, "layer": object.layer})
        map = {
            self.levelName: {
                "tiles": tiles,
                "signs": [],
                "triggers": []
            }
        }
        self.game.mapData.update(map)
        self.game.saveMap()