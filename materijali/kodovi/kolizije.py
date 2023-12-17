import pygame as pg
from pygame import Vector2, Color, Rect
import pygamebg

w, h = 400, 400

surface = pygamebg.open_window(w, h, "Read mouse state")

A = Rect(100, 100, 200, 100)
B = Rect(250, 150, 100, 100)

# presek dva pravougaonika
C = A.clip(B)

# print(A.colliderect(B))

def update():
    surface.fill(pg.Color("white"))
    x, y = pg.mouse.get_pos()

    # pg.draw.circle(surface , Color("red"), (x, y), 30)

    if A.collidepoint((x, y)):
        pg.draw.rect(surface, Color("red"), A)
    else:
        pg.draw.rect(surface, Color("green"), A)

    if B.collidepoint((x, y)):
        pg.draw.rect(surface, Color("red"), B)
    else:
        pg.draw.rect(surface, Color("green"), B)

    pg.draw.rect(surface, Color("blue"), C)

pygamebg.frame_loop(30, update)
