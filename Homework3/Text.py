from Drawable import Drawable
import pygame

class Text(Drawable):
    def __init__(self, position, visible, color=(0,0,0)):
        self.color = color
        super().__init__(position, visible)
    def draw(self, surface, message):
        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(message, True, super().getColor())
        surface.blit(text, self.get_rect())
    def get_rect(self):
        return pygame.Rect(self.getPos(), self.getPos())
