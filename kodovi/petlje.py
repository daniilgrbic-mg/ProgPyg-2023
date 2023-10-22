import pygame
import pygamebg

prozor = pygamebg.open_window(400, 400, "Skelet Uvod")

boja = pygame.Color('red')
crvena = boja
zelena = pygame.Color('green')

#x = 40
#while x <= 360:
#    pygame.draw.circle(prozor, boja, [x, 200], 30)
#    x += 80

#for x in [40,120,200,280,360]:
#    pygame.draw.circle(prozor, boja, [x, 200], 30)

#for x in range(40, 361, 80):
#    pygame.draw.circle(prozor, boja, [x, 200], 30)

for x in range(40, 361, 80):
    if x == 200:
        pygame.draw.circle(prozor, zelena, [x, 200], 30)
    else:
        pygame.draw.circle(prozor, crvena, [x, 200], 30)

pygamebg.wait_loop()