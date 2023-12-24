import pygamebg
import pygame as pg
from pygame import Vector2, Color

prozor = pygamebg.open_window(1000, 800, "Jurenje sa vise protivnika")

enemies = [
    Vector2(900, 700),
    Vector2(900, 100),
    Vector2(100, 700)
] 
player = Vector2(100, 100)
vidokrug = 150

def update_frame():

    global player
    global enemy
    
    # interakcija korsinika
    tastatura = pg.key.get_pressed()
    if tastatura[pg.K_LEFT]: # da li je stisnuta streica levo
        player.x -= 5
    if tastatura[pg.K_RIGHT]:
        player.x += 5
    if tastatura[pg.K_UP]:
        player.y -= 5
    if tastatura[pg.K_DOWN]:
        player.y += 5

    # racun kretanja i pozcije
    for enemy in enemies:
        # za svakog enemy-ja iz liste radimo istu stvar: ako je igrac blizu jurimo ga
        razlika = player - enemy
        if razlika.length() <= vidokrug:
            enemy += razlika.normalize() * 5

    # iscrtavanje
    prozor.fill(Color('white'))
    pg.draw.circle(prozor, Color('black'), player, 15)

    for enemy in enemies:
        # za svakog enemy-ja iz liste radimo istu stvar: crtamo ga na njegovoj pozicji i vidokrug oko njega
        pg.draw.circle(prozor, Color('red'), enemy, 20)
        pg.draw.circle(prozor, Color('red'), enemy, vidokrug, 2)

pygamebg.frame_loop(30, update_frame)
