import pygamebg
import pygame as pg
from pygame import Color, Surface

prozor = pg.display.set_mode((1000, 750), pg.RESIZABLE)

samurai = pg.image.load('Samurai/Attack_1.png')

platno = Surface((200, 150))

trenutna_slika = 0

def update_frame():
    global trenutna_slika
    global prozor

    platno.fill(Color('white'))
    platno.blit(samurai, (0,0), (128*trenutna_slika,0,128,128))
    
    trenutna_slika += 1
    if trenutna_slika == 6:
        trenutna_slika = 0
    
    s, v = 200, 150
    sp, vp = pg.display.get_window_size()
    prozor.fill(Color('black'))
    prozor.blit(pg.transform.scale_by(platno, min(sp/s, vp/v)), (0,0))

pygamebg.frame_loop(15, update_frame)
