import pygame as pg
import pygamebg
from pygame import Color

prozor = pygamebg.open_window(600, 600, "Skelet Uvod")

def jelka(x, y):
    zelena = Color('green')
    braon = Color('brown')
    pg.draw.polygon(prozor, zelena, [ (x-30,y-20), (x+30,y-20), (x,y-100) ])
    pg.draw.rect(prozor, braon, (x-10, y-20, 20, 20))

jelka(150,450)
jelka(300,450)
jelka(450,450)

pygamebg.wait_loop()