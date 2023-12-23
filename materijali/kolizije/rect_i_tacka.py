import pygame as pg
from pygame import Vector2, Color, Rect
import pygamebg

w, h = 400, 400

surface = pygamebg.open_window(w, h, "Presek pravougaonika i tacke (kursora)")

# A i B crtamo zelenim ako kursor nije preko njih, a crvenim inace
A = Rect(100, 100, 200, 100)
B = Rect(250, 150, 100, 100)

# presek dva pravougaonika, iscrtavacemo ga uvek plavom bojom
C = A.clip(B)

# print(A.colliderect(B))

def update():
    surface.fill(pg.Color("white"))
    x, y = pg.mouse.get_pos()

    if A.collidepoint((x, y)):
        pg.draw.rect(surface, Color("red"), A)
    else:
        pg.draw.rect(surface, Color("green"), A)

    if B.collidepoint((x, y)):
        pg.draw.rect(surface, Color("red"), B)
    else:
        pg.draw.rect(surface, Color("green"), B)

    pg.draw.rect(surface, Color("blue"), C)

    # iscrtavanje malog kruzica spod kursora misa
    pg.draw.circle(surface , Color("black"), (x, y), 5)

pygamebg.frame_loop(60, update)
