import pygame as pg
import pygamebg
from pygame import Color, Vector2, Rect

window = pygamebg.open_window(800, 600, "Pong")

# spremamo font za prikazivanje teksta (za poene)
font = pg.font.SysFont("Arial", 36)

# loptu posmatramo kao pravougaonik sto se tice kolizije,
# a iscrtavamo krug oko centra tog pravougaonika
lopta_p = Rect(400,300,34,34)
lopta_v = Vector2(10, 5)

# reketi su (logicno) takodje pravougaonici
reket_l = Rect(0,270,20,60)
reket_d = Rect(780,270,20,60)

# poeni oba igraca
poeni_l = 0
poeni_d = 0

# zidovi su debeli pravougaonici odmah izvan granica ekrana,
# smeju da se preklapaju
zid_n = Rect(-50,-50,900,50) # gornji (n - north)
zid_s = Rect(-50,600,900,50) # donji (s - south)
zid_w = Rect(-50,-50,50,700) # levi (w - west)
zid_e = Rect(800,-50,50,700) # desni (e - east)

def update():

    global lopta_p
    global poeni_l, poeni_d

    # svaki frejm se pomera lopta
    # lopta_p = lopta_p.move(lopta_v)
    lopta_p.x += lopta_v.x
    lopta_p.y += lopta_v.y

    # kontrole za reket (uslovi posle `and` ogranicavaju rekete da ne izadju van ekrana)
    keys = pg.key.get_pressed()
    if keys[pg.K_DOWN] and reket_d.y <= 530:
        reket_d.y += 15
    if keys[pg.K_UP] and reket_d.y >= 10:
        reket_d.y -= 15
    if keys[pg.K_s] and reket_l.y <= 530:
        reket_l.y += 15
    if keys[pg.K_w] and reket_l.y >= 10:
        reket_l.y -= 15

    # odbijanje od reketa i zidova (gornjeg i donjeg)
    if lopta_p.collideobjects([zid_n, zid_s]):
        lopta_v.y *= -1
    if lopta_p.collideobjects([reket_l, reket_d]):
        lopta_v.x *= -1

    # ako se slupa lopta u levi ili desni zid, azuriramo poene i vracamo loptu u sredinu ekrana
    if lopta_p.colliderect(zid_w):
        poeni_d += 1
    if lopta_p.colliderect(zid_e):
        poeni_l += 1
    if lopta_p.collideobjects([zid_e, zid_w]):
        lopta_p.x = 400
        lopta_p.y = 300
        pg.time.wait(1000)

    # azuriramo naslov prozora da se prikazuju poeni
    pg.display.set_caption(f'Pong {poeni_l}:{poeni_d}')

    # renderujemo (pravimo sliku) teksta koji prikazuje trenutne poene
    rendered_text = font.render(f'{poeni_l}:{poeni_d}', True, Color("pink"))

    window.fill(Color("black"))
    window.blit(rendered_text, (400-18,300-18))
    pg.draw.circle(window, Color("white"), lopta_p.center, 20)
    pg.draw.rect(window, Color("red"), reket_l)
    pg.draw.rect(window, Color("green"), reket_d)

pygamebg.frame_loop(30, update)
