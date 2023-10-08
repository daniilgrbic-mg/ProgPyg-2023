import pygame
import pygamebg

prozor = pygamebg.open_window(400, 400, "Trougao")

prozor.fill(pygame.Color('white'))

pygame.draw.polygon(prozor, (255,0,0), [ (200,100), (100,300), (300,300) ])

pygamebg.wait_loop()
