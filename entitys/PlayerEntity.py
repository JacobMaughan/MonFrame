# Description: The player entity
# Author: Jacob Maughan

# Lib Imports
from pygame import Rect

# Local Imports
from Enums import Direction
from Enums import PlayerState
from SpriteSheetHandler import SpriteSheetHandler
from AnimationHandler import AnimationHandler

class PlayerEntity():
    def __init__(self):
        self.rect = Rect(0, 0, 16 * 4, 32 * 4)
        self.collideOffsetX = 18
        self.collideOffsetY = 90
        self.collideRect = Rect(self.rect.x + self.collideOffsetX, self.rect.y + self.collideOffsetY, 30, 10)

        self.ID = 'player'
        self.velX = 0
        self.velY = 0
        self.speed = 5
        self.direction = Direction.UP
        self.moveKeys = [False, False, False, False]
        self.debug = False

        self.state = PlayerState.IDLE

        self.spriteSheet = SpriteSheetHandler('./assets/art/character.png')
        self.sprites = self.spriteSheet.getImageArray(16, 32, self.rect.width, self.rect.height)

        self.verticalSprites = [2, 0, 3, 1]
        self.horizontalSprites = [1, 2, 3, 0]
        self.walkingSprites = []
        for i in range(len(self.verticalSprites)):
            for o in range(len(self.horizontalSprites)):
                self.walkingSprites.append(self.sprites[self.verticalSprites[i]][self.horizontalSprites[o]])
        
        self.walkingAnimation = AnimationHandler(self.walkingSprites, 4, 10, True)

    def tick(self, tickCount):
        if self.state == PlayerState.IDLE:
            if self.walkingAnimation.active: self.walkingAnimation.deActivate()
            if not self.velX == 0 or not self.velY == 0:
                self.state = PlayerState.WALKING
        if self.state == PlayerState.WALKING:
            if not self.walkingAnimation.active: self.walkingAnimation.activate()
            self.walkingAnimation.tick(tickCount, direction = self.direction)
            self.rect.x += self.velX * self.speed
            self.rect.y += self.velY * self.speed
            if self.velX == 0 and self.velY == 0:
                self.state = PlayerState.IDLE
        
        self.collideRect.x = self.rect.x + self.collideOffsetX
        self.collideRect.y = self.rect.y + self.collideOffsetY
        
    def render(self, window, cameraRect):
        if self.state == PlayerState.IDLE:
            if self.direction == Direction.UP:
                window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.sprites[2][0])
            elif self.direction == Direction.DOWN:
                window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.sprites[0][0])
            elif self.direction == Direction.LEFT:
                window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.sprites[3][0])
            elif self.direction == Direction.RIGHT:
                window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.sprites[1][0])
        elif self.state == PlayerState.WALKING:
            window.drawSprite(self.rect.x - cameraRect.x, self.rect.y - cameraRect.y, self.walkingAnimation.activeSprite)
        if self.debug:
            window.drawRect((self.collideRect.x - cameraRect.x, self.collideRect.y - cameraRect.y, self.collideRect.width, self.collideRect.height), (255, 0, 255))
    
    def move(self, direction, pressed):
        if pressed:
            self.setVel(direction)
            if self.direction == Direction.UP:
                self.moveKeys[0] = True
            elif self.direction == Direction.DOWN:
                self.moveKeys[1] = True
            elif self.direction == Direction.LEFT:
                self.moveKeys[2] = True
            elif self.direction == Direction.RIGHT:
                self.moveKeys[3] = True
        else:
            if direction == Direction.UP:
                self.moveKeys[0] = False
                self.setVel(None)
                if self.moveKeys[1] == True:
                    self.setVel(Direction.DOWN)
                elif not self.moveKeys[2] == self.moveKeys[3]:
                    if self.moveKeys[2] == True:
                        self.setVel(Direction.LEFT)
                    elif self.moveKeys[3] == True:
                        self.setVel(Direction.RIGHT)
            elif direction == Direction.DOWN:
                self.moveKeys[1] = False
                self.setVel(None)
                if self.moveKeys[0] == True:
                    self.setVel(Direction.UP)
                elif not self.moveKeys[2] == self.moveKeys[3]:
                    if self.moveKeys[2] == True:
                        self.setVel(Direction.LEFT)
                    elif self.moveKeys[3] == True:
                        self.setVel(Direction.RIGHT)
            elif direction == Direction.LEFT:
                self.moveKeys[2] = False
                self.setVel(None)
                if self.moveKeys[3] == True:
                    self.setVel(Direction.RIGHT)
                elif not self.moveKeys[0] == self.moveKeys[1]:
                    if self.moveKeys[0] == True:
                        self.setVel(Direction.UP)
                    elif self.moveKeys[1] == True:
                        self.setVel(Direction.DOWN)
            elif direction == Direction.RIGHT:
                self.moveKeys[3] = False
                self.setVel(None)
                if self.moveKeys[2] == True:
                    self.setVel(Direction.LEFT)
                elif not self.moveKeys[0] == self.moveKeys[1]:
                    if self.moveKeys[0] == True:
                        self.setVel(Direction.UP)
                    elif self.moveKeys[1] == True:
                        self.setVel(Direction.DOWN)

    def setVel(self, direction):
        if direction == None:
            self.velX = 0
            self.velY = 0
        else:
            self.direction = direction
            if direction == Direction.UP:
                self.velY = -1
                self.velX = 0
            elif direction == Direction.DOWN:
                self.velY = 1
                self.velX = 0
            elif direction == Direction.LEFT:
                self.velX = -1
                self.velY = 0
            elif direction == Direction.RIGHT:
                self.velX = 1
                self.velY = 0
    
    def collide(self, objects):
        for object in objects:
            if object.hasCollision:
                if self.direction == Direction.UP:
                    self.rect.y += self.speed
                    self.move(Direction.UP, False)
                elif self.direction == Direction.DOWN:
                    self.rect.y -= self.speed
                    self.move(Direction.DOWN, False)
                elif self.direction == Direction.LEFT:
                    self.rect.x += self.speed
                    self.move(Direction.LEFT, False)
                elif self.direction == Direction.RIGHT:
                    self.rect.x -= self.speed
                    self.move(Direction.RIGHT, False)