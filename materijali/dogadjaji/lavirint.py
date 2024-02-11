import pygame as pg
import pygamebg

w, h = 100, 100
window = pygamebg.open_window(w, h, "Read keyboard state")

lavirint = [
    list("1111111"),
    list("1*    1"),
    list("111 1 1"),
    list("1   111"),
    list("11 11 1"),
    list("11     "),
    list("1111111")
]

r, k = 1, 1

def draw():
    window.fill(pg.Color("black"))

def key_pressed(event):
    global r, k
    nr, nk = r, k
    if event.key == pg.K_DOWN:
        nr += 1
    if event.key == pg.K_UP:
        nr -= 1
    if event.key == pg.K_RIGHT:
        nk += 1
    if event.key == pg.K_LEFT:
        nk -= 1
    
    if lavirint[nr][nk] == '1':
        return 
    
    lavirint[r][k] = ' '
    lavirint[nr][nk] = '*'
    r, k = nr, nk

    print('----------------------')
    for i in range(7):
        print("".join(lavirint[i]))



pygamebg.event_loop(draw, {
    pg.KEYDOWN : key_pressed
})
