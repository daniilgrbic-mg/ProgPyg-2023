import pygame as pg
import pygamebg

w, h = 500, 500
window = pygamebg.open_window(w, h, "Read keyboard state")

boja = "red"

def draw():
    window.fill(pg.Color(boja))

def click(event):
    global boja
    
    print("Klik misa na poziciji", event.pos)
    print("Levo dugme:", bool(event.button == pg.BUTTON_LEFT))
    print("Desno dugme:", bool(event.button == pg.BUTTON_RIGHT))

    if boja == "red":
        boja = "green"
    else:
        boja = "red"
    return True # ponovo iscrtaj ekran

def key_pressed(event):
    # print("Stisnut taster", chr(event.key))
    pass

pygamebg.event_loop(draw, {
    pg.MOUSEBUTTONDOWN : click,
    pg.KEYDOWN : key_pressed
})
