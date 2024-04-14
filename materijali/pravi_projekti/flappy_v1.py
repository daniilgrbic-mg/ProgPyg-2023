"""
U ovoj verziji Fallpy Eagle imamo orla (loptu) koji se krece mimo stubova
i moze da odskace, ali ne i da se sudari
"""

import pygamebg
import pygame as pg
from pygame import Color, Vector2, Rect
from random import randint

window = pygamebg.open_window(width=600, height=800, caption="Fallpy Eagle")
pg.key.set_repeat(100, 100)

bird_pos = Vector2(50, 400) # position
bird_vel = Vector2(0, 0)    # velocity - brzina
bird_acc = Vector2(0, 1.5)  # acceleration - ubrzanje

column_distance = 250
columns = [
    Vector2(column_distance*1, randint(200, 600)),
    Vector2(column_distance*2, randint(200, 600)),
    Vector2(column_distance*3, randint(200, 600)),
    Vector2(column_distance*4, randint(200, 600)),
]

def top_rect(column: Vector2) -> Rect:
    return Rect(column.x, column.y-900, 30, 800)
def bottom_rect(column):
    return Rect(column.x, column.y+100, 30, 800)

def update_frame():
    global bird_pos, bird_vel, bird_acc
    global columns

    bird_vel += bird_acc
    bird_pos += bird_vel

    for column in columns:
        column.x -= 10

    if columns[0].x < -100:
        columns.pop(0)
        new_column = Vector2(
            columns[-1].x+column_distance, 
            randint(200, 600)
        )
        columns.append(new_column)

    window.fill(Color("black"))
    pg.draw.circle(window, Color("white"), bird_pos, 10)
    for column in columns:
        pg.draw.rect(window, Color("green"), top_rect(column))
        pg.draw.rect(window, Color("green"), bottom_rect(column))

def flap():
    global bird_vel
    bird_vel = Vector2(0, -15)

def handle_event(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        flap()

pygamebg.frame_loop(30, update_frame, handle_event)
