# Description: Handles pygame events
# Author: Jacob Maughan

# Lib Imports
import pygame

# Local Imports
from Enums import GameState

class EventHandler():
    def __init__(self, controlsData, camera, game):
        # Super Initilization
        self.controlsData = controlsData
        self.camera = camera
        self.game = game
        
        # Initilize Vars
        self.gameState = None

    def tick(self):
        # Check for pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()
            elif event.type == pygame.KEYDOWN:
                # Universal Key Handling
                if event.key == self.controlsData['force-quit']:
                    self.game.stop()
                
                # Per-State Key Handling
                if self.gameState == GameState.GAME:
                    pass
            elif event.type == pygame.KEYUP:
                # Universal Key Handling
                if event.key == self.controlsData['force-quit']:
                    pass

                # Per-State Key Handling
                if self.gameState == GameState.GAME:
                    pass