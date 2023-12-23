import pygamebg
import pygame as pg
from pygame import Vector2, Color

prozor = pygamebg.open_window(600, 400, "Odbijanje lopte (4 zida)")

lopta = Vector2(50, 200)
pomeraj = Vector2(10, 5)

boja_pozadine = Color('white')
boja_lopte = Color('red')

def update_frame():
    global lopta
    global pomeraj

    prozor.fill(boja_pozadine)
    pg.draw.circle(prozor, boja_lopte, lopta, 20)

    lopta += pomeraj

    if lopta.x >= 580 or lopta.x <= 20:
        pomeraj.x *= -1
    if lopta.y >= 380 or lopta.y <= 20:
        pomeraj.y *= -1

pygamebg.frame_loop(30, update_frame)