import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self, position = (0,0), visible = True):
        self.position = position
        self.visible = visible
    @abc.abstractmethod
    def draw(self, surface):
        pass
    
    @abc.abstractmethod
    def get_rect(self):
        pass

    def getPos(self):
        return self.position

    def getVisible(self):
        return self.visible

    def getColor(self):
        return self.color

    def setPos(self, x, y):
        self.position = (x, y)

    