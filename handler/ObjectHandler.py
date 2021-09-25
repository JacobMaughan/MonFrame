# Description: Handles game objects
# Author: Jacob Maughan

class ObjectHandler():
    def __init__(self):
        self.objects = []

    def tick(self):
        for object in self.objects:
            object.tick()
    
    def render(self, window, cameraRect):
        for i in range(3):
            for object in self.objects:
                if object.layer == i:
                    object.render(window, cameraRect)
    
    def addObject(self, object):
        self.objects.append(object)
    
    def removeObject(self, object):
        for i in range(len(self.objects)):
            if self.objects[i] == object:
                self.objects.pop(i)
                return True
        return False
    
    def getObjectsByID(self, ID):
        objects = []
        for object in self.objects:
            if object.ID == ID:
                objects.append(object)
        return objects

    def collide(self, collider):
        objects = []
        for object in self.objects:
            if collider.colliderect(object.rect):
                objects.append(object)
        return objects