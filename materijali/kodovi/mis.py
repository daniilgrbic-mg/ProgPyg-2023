import pygame as pg
import pygamebg

w, h = 500, 500

surface = pygamebg.open_window(w, h, "Read mouse state")

def update():
    surface.fill(pg.Color("white"))
    mouse = pg.mouse.get_pos()
    pg.draw.circle(surface , pg.Color("red"), mouse, 30)

pygamebg.frame_loop(30, update)