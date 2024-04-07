import pygame as pg
from pygame import Color, Vector2
import pygamebg

prozor = pygamebg.open_window(1600, 900, "Transformacije")

avion = pg.image.load('avion_side.png')
avion = pg.transform.flip(avion, flip_x=True, flip_y=False)
avion = pg.transform.scale_by(avion, 0.4)

pozicija = Vector2(0, 900)
brzina = Vector2(240, -300)
g = Vector2(0, 90)

def draw():
    global brzina, pozicija

    pozicija += brzina * 1/30
    brzina += g * 1/30

    x_pravac = Vector2(1, 0)
    ugao = brzina.angle_to(x_pravac)
    rot = pg.transform.rotate(avion, ugao)
    rot_size = Vector2(rot.get_size())

    prozor.fill(Color("black"))
    prozor.blit(rot, pozicija - rot_size/2)

pygamebg.frame_loop(30, draw)
