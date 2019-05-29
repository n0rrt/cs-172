from Drawable import Drawable
import pygame
class Ball(Drawable):
    def __init__(self, position, visible, radius = 0, color = (0,0,0)):
        self.radius = radius
        self.color = color
        super().__init__(position, visible)
    def draw(self, surface):
        pygame.draw.circle(surface, super().getColor(), super().getPos(), self.getRadius())

    def get_rect(self):
        return pygame.Rect((super().getPos()[0] - self.getRadius(), super().getPos()[1] - self.getRadius()), (2 * self.getRadius(), 2 * self.getRadius()))
        
    def getRadius(self):
        return self.radius
    