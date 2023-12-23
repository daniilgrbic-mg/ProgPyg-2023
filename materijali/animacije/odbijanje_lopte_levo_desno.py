import pygamebg
import pygame as pg
from pygame import Vector2, Color

prozor = pygamebg.open_window(600, 400, "Odbijanje lopte (levo-desno)")

lopta = 50 # pozicija lopte
pravac = "desno"

boja_pozadine = Color('white')
boja_lopte = Color('red')

def update_frame():
    global lopta
    global pravac

    prozor.fill(boja_pozadine)
    pg.draw.circle(prozor, boja_lopte, (lopta, 200), 20)

    if pravac == "desno":
        lopta += 10
    else:
        lopta -= 10

    if lopta >= 580 or lopta <= 20:
        if pravac == "desno":
            pravac = "levo"
        else:
            pravac = "desno"

pygamebg.frame_loop(30, update_frame)