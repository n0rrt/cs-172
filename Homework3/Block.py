from Drawable import Drawable
import pygame

class Block(Drawable):
    def __init__(self, position, visible, size = 0, color = (0,0,0)):
        self.color = color
        self.size = size
        super().__init__(position, visible)
    def draw(self, surface):
        pygame.draw.rect(surface, super().getColor(), self.get_rect(), 0)
    def get_rect(self):    
        return pygame.Rect(super().getPos(), (self.getSize(), self.getSize()))
    
    def getSize(self):
        return self.size
    def setPos(self, pos):
        self.position = pos

    def setVis(self, bool):
        self.visible = bool
