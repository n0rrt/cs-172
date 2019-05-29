import time
import random
from Drawable import *



surface = pygame.display.set_mode((400,300))

drawables = []
GREEN = (0, 153, 51)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
ground = Rectangle(0, 200, 400, 100, GREEN)
sky = Rectangle(0, 0, 400, 200, BLUE)

drawables.append(ground)
drawables.append(sky)
clock = pygame.time.Clock()
display_rect = False
while True:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q)):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_SPACE:
            
            display_rect = not display_rect
    
    if display_rect:
        if (random.randrange(0, 10) in range(0, 3)):
            newSnow = Snowflake(random.randrange(0, 400), 0, WHITE)
            drawables.append(newSnow)
        for drawable in drawables:
            if (isinstance(drawable, Snowflake)):
                drawable.setLoc([drawable.getX(), drawable.getY() + 1]) 
            
            drawable.draw(surface)
    pygame.display.update()
    
    clock.tick(30)
    
