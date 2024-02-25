import pygame as pg
import pygamebg
from pygame import Color, Vector2

polja = 27    # broj polja
velicina = 30 # velicina polja
window = pygamebg.open_window(polja*velicina, polja*velicina, "Read keyboard state")
pg.event.set_grab(True)

zmija = [Vector2(3,13), Vector2(4,13), Vector2(5,13), Vector2(6,13)]
pravac = Vector2(1,0) # desno

def update():

    glava = zmija[-1]
    nova_glava = glava + pravac
    zmija.append(nova_glava)
    zmija.pop(0)

    window.fill(pg.Color("black"))
    for komad in zmija:
        col, row = komad
        x = col*velicina + 1
        y = row*velicina + 1
        pg.draw.rect(window, pg.Color('green'), (x, y, velicina-2, velicina-2))

def key_pressed(event):
    global pravac, zmija

    if event.key == pg.K_DOWN:
        pravac = Vector2(0,1)
    if event.key == pg.K_UP:
        pravac = Vector2(0,-1)
    if event.key == pg.K_RIGHT:
        pravac = Vector2(1,0)
    if event.key == pg.K_LEFT:
        pravac = Vector2(-1,0)

pygamebg.frame_loop(5, update, {
    pg.KEYDOWN : key_pressed
})
