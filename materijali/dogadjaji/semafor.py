import pygame as pg
import pygamebg
from pygame import Color

surface = pygamebg.open_window(200, 400, "Keyboard and mouse events")
pg.key.set_repeat(10,10)

semafor = "crvena"

def clicked(e):
    global semafor
    if semafor == "crvena":
        semafor = "zelena"
    else:
        semafor = "crvena"
    return True

def paint():
    surface.fill(pg.Color("black"))
    
    if semafor == "crvena":
        pg.draw.circle(surface, Color("red"), (100,100), 60)
    else:
        pg.draw.circle(surface, Color("gray15"), (100,100), 60)

    if semafor == "zelena":
        pg.draw.circle(surface, Color("green"), (100,300), 60)
    else:
        pg.draw.circle(surface, Color("gray15"), (100,300), 60)

pygamebg.event_loop(paint, {pg.MOUSEBUTTONDOWN:clicked})
