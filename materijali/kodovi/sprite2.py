import pygamebg
import pygame as pg
from pygame import Color, Surface

prozor = pg.display.set_mode((1000, 750), pg.RESIZABLE)

samurai = pg.image.load('Samurai/Attack_1.png')
samurai = [
    samurai.subsurface(0, 0, 128, 128),   # 0
    samurai.subsurface(128, 0, 128, 128), # 1
    samurai.subsurface(256, 0, 128, 128), # 2
    samurai.subsurface(384, 0, 128, 128), # 3
    samurai.subsurface(512, 0, 128, 128), # 4
    samurai.subsurface(640, 0, 128, 128)  # 5
]

platno = Surface((200, 150))

trenutna_slika = 0

def update_frame():
    global trenutna_slika
    global prozor

    platno.fill(Color('white'))
    platno.blit(samurai[trenutna_slika], (0,0))
    
    trenutna_slika += 1
    if trenutna_slika == 6:
        trenutna_slika = 0
    
    s, v = 200, 150
    sp, vp = pg.display.get_window_size()
    prozor.fill(Color('black'))
    prozor.blit(pg.transform.scale_by(platno, min(sp/s, vp/v)), (0,0))

pygamebg.frame_loop(15, update_frame)
