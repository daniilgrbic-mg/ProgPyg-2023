import pygame as pg
import pygamebg
from pygame import Rect, Color

w, h = 500, 500
surface = pygamebg.open_window(w, h, "Presek 2 pravougaonika")

brzina = 5

pokretni_pravougaonik = Rect(50, 50, 130, 80)
staticki_pravougaonik = Rect(250, 300, 200, 150)

def update():
    global x, y
    surface.fill(Color("white"))

    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        pokretni_pravougaonik.x += brzina
    if pressed[pg.K_LEFT]:
        pokretni_pravougaonik.x -= brzina
    if pressed[pg.K_DOWN]:
        pokretni_pravougaonik.y += brzina
    if pressed[pg.K_UP]:
        pokretni_pravougaonik.y -= brzina

    pg.draw.rect(surface, Color("black"), staticki_pravougaonik)

    if staticki_pravougaonik.colliderect(pokretni_pravougaonik):
        pg.draw.rect(surface, Color("red"), pokretni_pravougaonik)
    else:
        pg.draw.rect(surface, Color("green"), pokretni_pravougaonik)


pygamebg.frame_loop(30, update)
