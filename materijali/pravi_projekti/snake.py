import pygame as pg
import pygamebg
from pygame import Color, Vector2
import random

polja = 19    # broj polja
velicina = 40 # velicina polja
window = pygamebg.open_window(polja*velicina, polja*velicina, "Zmijica")

zmija = [
    Vector2(3,9), # rep
    Vector2(4,9), 
    Vector2(5,9), 
    Vector2(6,9)  # glava
]
pravac = Vector2(1,0) # desno
hrana = Vector2(9,9)

def update():

    stara_glava = zmija[-1]
    nova_glava = stara_glava + pravac

    # proveravam dal se zmija udarila sama u sebe
    if nova_glava in zmija:
        exit()
    else:
        zmija.append(nova_glava) # append dodaje element na kraj liste (nova glava)

    # proveravam dal je zmija pojela hranu
    if nova_glava == hrana:
        hrana.x = random.randint(0, polja-1)
        hrana.y = random.randint(0, polja-1)
    else:
        zmija.pop(0) # brise 0-ti element (rep)

    window.fill(pg.Color("black"))

    pg.draw.ellipse(window, Color('red'), (
        velicina*hrana.x+1,
        velicina*hrana.y+1,
        velicina-2,
        velicina-2
    ))
    
    for komad in zmija:
        pg.draw.rect(window, Color('green'), (
            velicina*komad.x+1,
            velicina*komad.y+1,
            velicina-2,
            velicina-2
        ))

def key_pressed(event):
    global pravac
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
