# Description: Handles game objects
# Author: Jacob Maughan

class EntityHandler():
    def __init__(self):
        self.entitys = []

    def tick(self, tickCount):
        for entity in self.entitys:
            entity.tick(tickCount)
    
    def render(self, window, cameraRect):
        for entity in self.entitys:
            entity.render(window, cameraRect)
    
    def addEntity(self, entity):
        self.entitys.append(entity)
    
    def removeEntity(self, entity):
        for i in range(len(self.entitys)):
            if self.entitys[i] == entity:
                self.entitys.pop(i)
                return True
        return False
    
    def removeEntityByID(self, ID):
        for i in range(len(self.entitys)):
            if self.entitys[i].ID == ID:
                self.entitys.pop(i)
                return True
        return False
    
    def getEntityByID(self, ID):
        for entity in self.entitys:
            if entity.ID == ID:
                return entity