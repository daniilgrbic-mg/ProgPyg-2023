import pygame as pg
import pygamebg

w, h = 800, 800

surface = pygamebg.open_window(w, h, "Svemir")

x, y = w//2, h//2
vx, vy = 0, 0

def update():
    global x, y, vx, vy
    surface.fill(pg.Color("black"))
    pressed = pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        vx += 0.5
    if pressed[pg.K_LEFT]:
        vx -= 0.5
    if pressed[pg.K_DOWN]:
        vy += 0.5
    if pressed[pg.K_UP]:
        vy -= 0.5
    x += vx
    y += vy

    # teleportuje sa na drugu stranu ekrana kad stigne do granice
    # npr ako se krece desno 802 postane 2, a ako se krece levo -10 postane 790...
    x = x % w
    y = y % h

    pg.draw.circle(surface , pg.Color("gray"), (x, y), 30)

pygamebg.frame_loop(30, update)
