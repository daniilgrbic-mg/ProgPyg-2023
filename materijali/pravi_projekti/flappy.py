"""
U ovoj verziji Fallpy Eagle dodali smo sliku orla, sa okretanjem u pravcu kretanja
"""

import pygamebg
import pygame as pg
from pygame import Color, Vector2, Rect
from random import randint
import os

WIDTH, HEIGHT = 800, 800
window = pygamebg.open_window(WIDTH, HEIGHT, "Fallpy Eagle | 0")
pg.key.set_repeat(100, 100)

parent_dir = os.path.dirname(__file__)

eagle_image = pg.image.load(f"{parent_dir}/eagle.png") # velicina 9x12
eagle_image = pg.transform.scale_by(eagle_image, 3)    # velicina 27x36

mountains_image = pg.image.load(f"{parent_dir}/mountains.png")
mountains_image = pg.transform.scale_by(mountains_image, HEIGHT/mountains_image.get_size()[1])

# spremamo font za prikazivanje teksta (za poene)
font = pg.font.SysFont("Arial", 36)

f = open(f"{parent_dir}/high.txt", "r")
highscore = int(f.read())
f.close()

def save_score(score):
    print(f"SCORE: {score}")
    global highscore
    if score > highscore:
        highscore = score
    print(f"Highscore: {highscore}")
    f = open(f"{parent_dir}/high.txt", "w")
    f.write(f"{highscore}")
    f.close()

def init():
    global bird, bird_vel, bird_acc
    global columns, column_distance
    global score
    bird = Rect(50, 400, 20, 30) # position
    bird_vel = Vector2(10, -15) # velocity - brzina
    bird_acc = Vector2(0, 1.5) # acceleration - ubrzanje
    score = 0
    pg.display.set_caption("Fallpy Eagle | 0")

    # kolone su predstavljeni preko vektora, gde su zadate tacke sredine otvora izmedju kolona
    column_distance = 250
    columns = [
        Vector2(column_distance*1, randint(200, 600)),
        Vector2(column_distance*2, randint(200, 600)),
        Vector2(column_distance*3, randint(200, 600)),
        Vector2(column_distance*4, randint(200, 600)),
    ]

    draw_frame()
    while True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                return
            if event.type == pg.QUIT:
                exit(0)

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
    global score

    # pomernanje ptice i azuriranje brzine
    bird_vel.y += bird_acc.y
    bird.y += bird_vel.y

    # pomeranje svake kolone ulevo
    for column in columns:
        column.x -= 10

    # provera kolizija, prvo sa kolonama pa sa podom/plafonom
    for column in columns:
        if hit_column(column, bird):
            save_score(score)
            init()
            return
    if bird.colliderect(ceiling) or bird.colliderect(floor):
        save_score(score)
        init()
        return

    # kolone se krecu za po 10 piksela, ptica predje kolonu kad se kolona nadje na poziciji x=20
    # (u svakom frejmu proveravamo da li je vodeca kolona bas na toj pozicji)
    if columns[0].x == 20:
        score += 1
        pg.display.set_caption(f"Fallpy Eagle | {score}")

    # izbacivanje vodece kolone koja izadje van granice, i ubacivanje nove na kraj liste 
    if columns[0].x < -100:
        columns.pop(0)
        new_column = Vector2(
            columns[-1].x+column_distance, 
            randint(200, HEIGHT-200)
        )
        columns.append(new_column)

def draw_frame():
    # iscrtavanje
    # window.fill(Color("black"))
    window.blit(mountains_image, (0,0))
    rotated_eagle = pg.transform.rotate(eagle_image, bird_vel.angle_to(Vector2(1, 0)))
    # pg.draw.rect(window, Color("red"), bird)
    window.blit(rotated_eagle, (bird.x-8, bird.y-5))
    for column in columns:
        pg.draw.rect(window, Color("green"), top_rect(column))
        pg.draw.rect(window, Color("green"), bottom_rect(column))
    rendered_score = font.render(f'{score}', False, Color("red"))
    window.blit(pg.transform.scale_by(rendered_score, 4), (0,0))
    rendered_highscore = font.render(f'{highscore}', False, Color("red"))
    rendered_highscore = pg.transform.scale_by(rendered_highscore, 4)
    window.blit(rendered_highscore, (WIDTH-rendered_highscore.get_size()[0],0))
    pg.display.update()

# funkcija koja se pozove kad igrac klikne dugme za skok
def flap():
    global bird_vel
    bird_vel = Vector2(10, -15)

def handle_event(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
        flap()

init()

clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit(0)
        else:
            handle_event(event)
    update_frame()
    draw_frame()
    clock.tick(30)

