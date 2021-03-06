# Description: Handles pygame events
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import GameState
from Enums import Direction

class EventHandler():
    def __init__(self, controlsData, camera, devTools, game):
        # Super Initilization
        self.controlsData = controlsData
        self.camera = camera
        self.devTools = devTools
        self.game = game
        
        # Initilize Vars
        self.gameState = None

    def tick(self, entityHandler):
        # Check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            elif event.type == pygame.KEYDOWN:
                # Universal Key Handling
                if self.devTools.active:
                    self.devTools.keyPressed = event.key
                    if event.key == self.controlsData['dev-tools-up']:
                        self.devTools.changeSelection(Direction.UP)
                    elif event.key == self.controlsData['dev-tools-down']:
                        self.devTools.changeSelection(Direction.DOWN)
                    elif event.key == self.controlsData['dev-tools-select']:
                        self.devTools.select()
                    if self.devTools.selections[3][3]:
                        if event.key == self.controlsData['up']:
                            self.camera.velY = -1
                        elif event.key == self.controlsData['down']:
                            self.camera.velY = 1
                        elif event.key == self.controlsData['left']:
                            self.camera.velX = -1
                        elif event.key == self.controlsData['right']:
                            self.camera.velX = 1
                    if self.devTools.selections[4][3]:
                        if event.key == self.controlsData['dev-editor-up']:
                            self.devTools.editorMove(Direction.UP)
                        elif event.key == self.controlsData['dev-editor-down']:
                            self.devTools.editorMove(Direction.DOWN)
                        elif event.key == self.controlsData['dev-editor-left']:
                            self.devTools.editorMove(Direction.LEFT)
                        elif event.key == self.controlsData['dev-editor-right']:
                            self.devTools.editorMove(Direction.RIGHT)
                        elif event.key == self.controlsData['dev-editor-enter']:
                            self.devTools.editorEnter()
                        elif event.key == self.controlsData['dev-editor-delete']:
                            self.devTools.editorDelete()
                        elif event.key == self.controlsData['dev-editor-layer-toggle']:
                            self.devTools.editorToggleLayer()
                        elif event.key == self.controlsData['dev-editor-collision-toggle']:
                            self.devTools.editorToggleCollision()
                        elif event.key == self.controlsData['dev-editor-save-map']:
                            self.devTools.editorSaveMap()
                if event.key == self.controlsData['dev-tools']:
                    self.devTools.toggleActive()
                
                
                # Per-State Key Handling
                if self.gameState == GameState.GAME:
                    if not self.devTools.selections[3][3]:
                        if event.key == self.controlsData['up']:
                            entityHandler.getEntityByID('player').move(Direction.UP, True)
                        elif event.key == self.controlsData['down']:
                            entityHandler.getEntityByID('player').move(Direction.DOWN, True)
                        elif event.key == self.controlsData['left']:
                            entityHandler.getEntityByID('player').move(Direction.LEFT, True)
                        elif event.key == self.controlsData['right']:
                            entityHandler.getEntityByID('player').move(Direction.RIGHT, True)
            elif event.type == pygame.KEYUP:
                # Universal Key Handling
                if event.key == self.controlsData['dev-tools']:
                    pass
                if self.devTools.active:
                    if self.devTools.selections[3][3]:
                        if event.key == self.controlsData['up']:
                            self.camera.velY = 0
                        elif event.key == self.controlsData['down']:
                            self.camera.velY = 0
                        elif event.key == self.controlsData['left']:
                            self.camera.velX = 0
                        elif event.key == self.controlsData['right']:
                            self.camera.velX = 0

                # Per-State Key Handling
                if self.gameState == GameState.GAME:
                    if not self.devTools.selections[3][3]:
                        if event.key == self.controlsData['up']:
                            entityHandler.getEntityByID('player').move(Direction.UP, False)
                        elif event.key == self.controlsData['down']:
                            entityHandler.getEntityByID('player').move(Direction.DOWN, False)
                        elif event.key == self.controlsData['left']:
                            entityHandler.getEntityByID('player').move(Direction.LEFT, False)
                        elif event.key == self.controlsData['right']:
                            entityHandler.getEntityByID('player').move(Direction.RIGHT, False)