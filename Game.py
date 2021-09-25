# Description: The main file for a pygame application
# Author: Jacob Maughan

# Sys Imports
from time import time
from sys import path
from os import getcwd

# Lib Imports
import pygame

# Local Imports
path.append(getcwd() + '/handler')
path.append(getcwd() + '/entitys')
path.append(getcwd() + '/objects')
from Enums import GameState
from Json import Json
from Window import Window
from Camera import Camera
from EntityHandler import EntityHandler
from ObjectHandler import ObjectHandler
from MapHandler import MapHandler
from DevTools import DevTools
from EventHandler import EventHandler
from PlayerEntity import PlayerEntity

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Initialize game vars
        self.version = '0.0.1'
        self.running = False
        self.tickSpeed = 60
        self.tickCount = 0
        self.gameState = None

        # Initialize Json Files
        self.controlsFile = Json('./assets/data/controls.json')
        self.controlsData = self.controlsFile.getJson()
        self.mapFile = Json('./assets/data/maps.json')
        self.mapData = self.mapFile.getJson()

        # Initialize Handlers
        self.window = Window(self.version)
        self.camera = Camera(self.window)
        self.entityHandler = EntityHandler()
        self.objectHandler = ObjectHandler()
        self.mapHandler = MapHandler(self.mapData, self.objectHandler)
        self.devTools = DevTools(self, self.window, self.camera, self.entityHandler, self.objectHandler)
        self.eventHandler = EventHandler(self.controlsData, self.camera, self.devTools, self)

    def tick(self):
        # Games logic functions
        if not self.gameState == GameState.MAP_EDITOR:
            self.tickCount += 1
            self.eventHandler.tick(self.entityHandler)
            self.entityHandler.tick(self.tickCount)
            self.objectHandler.tick()
            self.camera.tick()

            self.devTools.tick()

            if self.gameState == GameState.GAME:
                if not self.devTools.selections[3][3]:
                    self.camera.moveToObject(self.entityHandler.getEntityByID('player'))
        else:
            self.tickCount += 1
            self.eventHandler.tick(self.entityHandler)
            self.camera.tick()
            self.devTools.tick()
    
    def render(self):
        # Games render functions
        self.window.fillScreen((255, 255, 255))
        if not self.gameState == GameState.MAP_EDITOR:
            self.entityHandler.render(self.window, self.camera.rect)
            self.objectHandler.render(self.window, self.camera.rect)
            self.devTools.render()
        else:
            for y in range(-50, 50):
                for x in range(-50, 50):
                    if y == 0 and x == 0:
                        self.window.drawRect((x * 16 * 4 + 1 - self.camera.rect.x, y * 16 * 4 + 1 - self.camera.rect.y, 14 * 4, 14 * 4), (0, 255, 0))
                    else:
                        self.window.drawRect((x * 16 * 4 + 1 - self.camera.rect.x, y * 16 * 4 + 1 - self.camera.rect.y, 14 * 4, 14 * 4), (0, 0, 0))
            self.objectHandler.render(self.window, self.camera.rect)
            self.devTools.render()
        pygame.display.update()

    def start(self):
        # Games startup functions
        self.running = True
        self.setGameState(GameState.GAME)
        self.run()

    def stop(self):
        # Games stoppping functions
        self.running = False

    def run(self):
        # Main game loop
        lastTime = time()
        dt = 0
        while self.running:
            dt += (time() - lastTime) * self.tickSpeed
            lastTime = time()
            if dt >= 1:
                dt -= 1
                self.tick()
            self.render()
    
    # Set the gamestate
    def setGameState(self, gameState):
        self.gameState = gameState
        self.eventHandler.gameState = gameState
        if gameState == GameState.GAME:
            self.entityHandler.addEntity(PlayerEntity())
            self.mapHandler.loadMap('level_1')

    # Save the controls file
    def saveControls(self):
        self.controlsFile.saveJson(self.controlsData)

    def saveMap(self):
        self.mapFile.saveJson(self.mapData)

if __name__ == '__main__':
    game = Game()
    game.start()