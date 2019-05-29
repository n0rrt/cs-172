from Drawable import *
from Ball import *
from Block import *
from Text import *
import pygame
import random
pygame.init()
surface = pygame.display.set_mode((400, 300))
colors = {"blue": (51, 119, 255), "red": (255, 42, 0), "green": (34, 204, 0), "white" : (255, 255, 255), "black" : (0, 0, 0)}
drawables = []
blocks = []
rects = []
ball = Ball((30,200), True, 15, colors["blue"])
initBlock = Block((300, 200), True, 15, colors["red"])
text = Text((0, 0), True, colors["green"])
yv = 0
xv = 0
drawables.append(ball)
drawables.append(initBlock)
drawables.append(text)
rects.append(pygame.Rect(0,0,0,0))
while len(blocks) < 6:
    newblock = Block((random.randrange(200, 300), 200), True, 15, colors["red"])  
    newrect = newblock.get_rect()
    if newrect.collidelist(rects) == -1:
        blocks.append(newblock)
        rects.append(newrect)


def intersect(rect1, rect2):
    if (rect1.x < rect2.x + rect2.width) and(rect1.x + rect1.width > rect2.x) and  (rect1.y < rect2.y + rect2.height) and(rect1.height + rect1.y > rect2.y):
        return True
    return False
clock = pygame.time.Clock()
score = 0
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5

y = ball.getPos()[1]
x = ball.getPos()[0]
while True:
    
    surface.fill(colors["white"])
    pygame.draw.line(surface, colors["black"], (400, 215), (0, 215))
    text.draw(surface, "score: " + str(score))
    ball.draw(surface)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q)):
            pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            initX = pygame.mouse.get_pos()[0]
            initY = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONUP:
            finX = pygame.mouse.get_pos()[0]
            finY = pygame.mouse.get_pos()[1]

            xv = finX - initX
            yv = -1 * (finY - initY)
    if abs(yv) > 0.0001:
        x += (dt * xv)
        y -= (dt * yv)
        ball.setPos(int(x), int(y))

        if y > 200:
            yv = -1 * R * yv
            xv = eta * xv
        if x > 300:
            xv = -1 * R * xv
        else:
            yv = yv - (g * dt)
        ball.draw(surface)
        #pygame.draw.rect(surface, colors["black"], ball.get_rect())
    for block in blocks:
       
        if intersect(ball.get_rect(), block.get_rect()):
            block.setVis(False)
            score += 1
        block.draw(surface)
        # pygame.draw.rect(surface, colors["green"], rects[z])

    
    pygame.display.update()
    clock.tick(30)
