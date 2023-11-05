import pygamebg
import pygame as pg
from pygame import Vector2, Color

prozor = pygamebg.open_window(600, 400, "frame_loop primer")

pozicija_lopte = Vector2(50, 200)
boja_pozadine = Color('white')
boja_lopte = Color('red')

def update_frame():
    global pozicija_lopte
    prozor.fill(boja_pozadine)
    pg.draw.circle(prozor, boja_lopte, pozicija_lopte, 20)
    pozicija_lopte += Vector2(10, 0)
    if pozicija_lopte.x > 550:
        pozicija_lopte = Vector2(50, 200)

pygamebg.frame_loop(30, update_frame)
