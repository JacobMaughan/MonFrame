# Description: Handles animations
# Author: Jacob Maughan

# Local Imports
from Enums import Direction

class AnimationHandler():
    def __init__(self, sprites, numFrames, ticksPerFrame, isLooping):
        self.sprites = sprites
        self.numFrames = numFrames
        self.ticksPerFrame = ticksPerFrame
        self.isLooping = isLooping

        self.active = False
        self.lastTick = 0
        self.animationFrame = 0
        self.activeSprite = sprites[0]
    
    def tick(self, tickCount, direction = None):
        if self.active:
            if self.isLooping:
                if direction == None:
                    if self.animationFrame == 0:
                        self.lastTick == tickCount
                        self.animationFrame += 1
                    self.activeSprite = self.sprites[self.animationFrame - 1]
                    if tickCount - self.lastTick == self.ticksPerFrame:
                        self.lastTick = tickCount
                        self.animationFrame = 0
                    if self.animationFrame == self.numFrames + 1:
                        self.animationFrame = 0
                else:
                    if self.animationFrame == 0:
                        self.lastTick = tickCount
                        self.animationFrame += 1
                    if direction == Direction.UP:
                        self.activeSprite = self.sprites[self.animationFrame - 1]
                    elif direction == Direction.DOWN:
                        self.activeSprite = self.sprites[self.numFrames + self.animationFrame - 1]
                    elif direction == Direction.LEFT:
                        self.activeSprite = self.sprites[self.numFrames * 2 + self.animationFrame - 1]
                    elif direction == Direction.RIGHT:
                        self.activeSprite = self.sprites[self.numFrames * 3 + self.animationFrame - 1]
                    if tickCount - self.lastTick == self.ticksPerFrame:
                        self.lastTick = tickCount
                        self.animationFrame += 1
                    if self.animationFrame == self.numFrames + 1:
                        self.animationFrame = 0
            else:
                if direction == None:
                    if self.animationFrame == 0:
                        self.lastTick == tickCount
                        self.animationFrame += 1
                    self.activeSprite = self.sprites[self.animationFrame - 1]
                    if tickCount - self.lastTick == self.ticksPerFrame:
                        self.lastTick = tickCount
                        self.animationFrame = 0
                    if self.animationFrame == self.numFrames + 1:
                        self.deActivate()
                else:
                    if self.animationFrame == 0:
                        self.lastTick = tickCount
                        self.animationFrame += 1
                    if direction == Direction.UP:
                        self.activeSprite = self.sprites[self.animationFrame - 1]
                    elif direction == Direction.DOWN:
                        self.activeSprite = self.sprites[self.numFrames + self.animationFrame - 1]
                    elif direction == Direction.LEFT:
                        self.activeSprite = self.sprites[self.numFrames * 2 + self.animationFrame - 1]
                    elif direction == Direction.RIGHT:
                        self.activeSprite = self.sprites[self.numFrames * 3 + self.animationFrame - 1]
                    if tickCount - self.lastTick == self.ticksPerFrame:
                        self.lastTick = tickCount
                        self.animationFrame += 1
                    if self.animationFrame == self.numFrames + 1:
                        self.deActivate()
    
    def activate(self):
        self.active = True
        self.animationFrame = 0
    
    def deActivate(self):
        self.active = False
        self.animationFrame = 0
