"""
U ovoj verziji Fallpy Eagle dodali smo kolizije sa stubovima i plafonom/zemljom
"""

import pygamebg
import pygame as pg
from pygame import Color, Vector2, Rect
from random import randint

WIDTH, HEIGHT = 600, 800
window = pygamebg.open_window(WIDTH, HEIGHT, "Fallpy Eagle")
pg.key.set_repeat(100, 100)

bird = Rect(50, 400, 10, 10) # position
bird_vel = Vector2(0, -15)     # velocity - brzina
bird_acc = Vector2(0, 1.5)   # acceleration - ubrzanje

# kolone su predstavljeni preko vektora, gde su zadate tacke sredine otvora izmedju kolona
column_distance = 250
columns = [
    Vector2(column_distance*1, randint(200, 600)),
    Vector2(column_distance*2, randint(200, 600)),
    Vector2(column_distance*3, randint(200, 600)),
    Vector2(column_distance*4, randint(200, 600)),
]

# pod i plafon (pravougaonici direktno ispod i iznad ptice)
ceiling = Rect(0, -20, 100, 20)
floor = Rect(0, HEIGHT, 100, 20)

# funkcije koje za vektor kolone nalaze njen gornji i donji deo
def top_rect(column: Vector2) -> Rect:
    return Rect(column.x, column.y-100-HEIGHT, 30, HEIGHT)
def bottom_rect(column: Vector2) -> Rect:
    return Rect(column.x, column.y+100, 30, HEIGHT)

# funkcija koja gleda dal se ptica sudarila sa datom kolonom
def hit_column(column: Vector2, bird: Rect) -> bool:
    return bird.collidelist([top_rect(column), bottom_rect(column)]) != -1

# funkcija koju sa poziva svaki frejm, tu se desava celokupno kretanje i iscrtavanje
def update_frame():
    global bird, bird_vel, bird_acc
    global columns

    # pomernanje ptice i azuriranje brzine
    bird_vel += bird_acc
    bird = bird.move(bird_vel)

    # pomeranje svake kolone ulevo
    for column in columns:
        column.x -= 10

    # provera kolizija, prvo sa kolonama pa sa podom/plafonom
    for column in columns:
        if hit_column(column, bird):
            pygamebg.wait_loop()
            exit(0)
    if bird.colliderect(ceiling) or bird.colliderect(floor):
        pygamebg.wait_loop()
        exit(0)

    # izbacivanje vodece kolone koja izadje van granice, i ubacivanje nove na kraj liste 
    if columns[0].x < -100:
        columns.pop(0)
        new_column = Vector2(
            columns[-1].x+column_distance, 
            randint(200, HEIGHT-200)
        )
        columns.append(new_column)

    # iscrtavanje
    window.fill(Color("black"))
    pg.draw.rect(window, Color("white"), bird)
    for column in columns:
        pg.draw.rect(window, Color("green"), top_rect(column))
        pg.draw.rect(window, Color("green"), bottom_rect(column))

# funkcija koja se pozove kad igrac klikne dugme za skok
def flap():
    global bird_vel
    bird_vel = Vector2(0, -15)

def handle_event(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        flap()

pygamebg.frame_loop(30, update_frame, handle_event)
