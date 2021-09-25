# Desciption: Handles the map creation
# Author: Jacob Maughan

# Local Imports
from SpriteSheetHandler import SpriteSheetHandler
from TileObject import TileObject

class MapHandler():
    def __init__(self, mapData, objectHandler):
        self.mapData = mapData
        self.objectHandler = objectHandler

        self.scaleFactor = 4

        self.spriteSheet = SpriteSheetHandler('./assets/art/overworld.png')
        self.spriteSheetArray = self.spriteSheet.getImageArray(16, 16, 16 * self.scaleFactor, 16 * self.scaleFactor)

    def loadMap(self, mapName):
        mapToLoad = self.mapData[mapName]
        triggers = mapToLoad['triggers']
        for tile in mapToLoad['tiles']:
            self.objectHandler.addObject(TileObject(tile['x'], tile['y'], 16 * self.scaleFactor, tile['spriteX'], tile['spriteY'], self.spriteSheetArray[tile['spriteY']][tile['spriteX']], tile['collision'], tile['layer']))