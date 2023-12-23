import pygamebg
import pygame as pg
from pygame import Color, Vector2

prozor = pygamebg.open_window(600, 600, "frame_loop primer")

pozicija = Vector2(200, 0)
sunce = Vector2(300, 300)
boja_svemira = Color('black')
boja_planete = Color('lightblue')
boja_sunca = Color('yellow')

def update_frame():
    global pozicija
    prozor.fill(boja_svemira)
    pg.draw.circle(prozor, boja_sunca, sunce, 50)
    pg.draw.circle(prozor, boja_planete, sunce+pozicija, 20)
    pozicija = pozicija.rotate(5)

pygamebg.frame_loop(30, update_frame)
