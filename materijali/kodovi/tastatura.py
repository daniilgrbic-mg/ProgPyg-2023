import pygame as pg
import pygamebg

w, h = 500, 500

surface = pygamebg.open_window(w, h, "Read keyboard state")

x, y = w//2, h//2
brzina = 5

def update():
    global x, y
    surface.fill(pg.Color("white"))
    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        x += brzina
    if pressed[pg.K_LEFT]:
        x -= brzina
    if pressed[pg.K_DOWN]:
        y += brzina
    if pressed[pg.K_UP]:
        y -= brzina
    pg.draw.circle(surface , pg.Color("red"), (x, y), 30)

pygamebg.frame_loop(30, update)
