import pygame as pg
import pygamebg

w, h = 400, 600
prozor = pygamebg.open_window(w, h, "Power up")

jacina = 20

def update():
    global jacina

    pressed = pg.key.get_pressed()

    if pressed[pg.K_SPACE]:
        jacina += 20
        jacina = min(jacina, h)
    else:
        jacina  -= 20
        jacina = max(jacina, 20)

    prozor.fill(pg.Color("black"))
    pg.draw.rect(prozor, pg.Color("green"), (100, 0, 200, jacina))

pygamebg.frame_loop(30, update)
