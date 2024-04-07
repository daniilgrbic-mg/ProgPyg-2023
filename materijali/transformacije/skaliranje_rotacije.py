import pygame as pg
import pygamebg

prozor = pygamebg.open_window(800, 800, "Transformacije")

avion = pg.image.load('avion.png')
avion = pg.transform.scale_by(avion, 1.2)
# avion = pg.transform.scale(avion, (400,400))

ugao = 0

def draw():
    global ugao
    ugao += 4
    rotavion = pg.transform.rotate(avion, ugao)
    avion_w, avion_h = rotavion.get_size()
    prozor.fill(pg.Color("black"))
    prozor.blit(rotavion, (400 - avion_w/2, 400 - avion_h/2))


pygamebg.frame_loop(60, draw)
