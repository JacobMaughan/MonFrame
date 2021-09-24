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
from Enums import GameState
from Json import Json
from Window import Window
from Camera import Camera
from EventHandler import EventHandler
from EntityHandler import EntityHandler
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

        # Initialize Handlers
        self.window = Window(self.version)
        self.camera = Camera(self.window)
        self.eventHandler = EventHandler(self.controlsData, self.camera, self)
        self.entityHandler = EntityHandler()

    def tick(self):
        # Games logic functions
        self.tickCount += 1
        self.eventHandler.tick()
        self.entityHandler.tick(self.tickCount)
        self.camera.tick()

        if self.gameState == GameState.GAME:
            self.camera.moveToObject(self.entityHandler.getEntityByID('player'))
    
    def render(self):
        # Games render functions
        self.window.fillScreen((255, 255, 255))
        self.entityHandler.render(self.window, self.camera.rect)
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

    # Save the controls file
    def saveControls(self):
        self.controlsFile.saveJson(self.controlsData)

if __name__ == '__main__':
    game = Game()
    game.start()