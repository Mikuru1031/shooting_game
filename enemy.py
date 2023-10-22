import pygame as pg
import random
from setting import *

class Enemy:
    def __init__(self):
        self.enemy_rect = pg.Rect(random.randint(200, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)
        self.screen = pg.display.get_surface()
    
    def enemyDisp(self):
        pg.draw.rect(self.screen, "blue", self.enemy_rect)