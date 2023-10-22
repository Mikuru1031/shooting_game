import pygame as pg
from setting import *

#プレイヤークラス
class Player:
    def __init__(self):
        self.player_rect = pg.Rect(100, HEIGHT / 2 - 50, 50, 50)
        self.bullet_rect = pg.Rect(self.player_rect.x+50, self.player_rect.y+20, 10, 10)
        self.isShoot = False
        self.screen = pg.display.get_surface()
    
    def playerDisp(self):
        pg.draw.rect(self.screen, "red", self.player_rect)

    def bulletDisp(self):
        pg.draw.rect(self.screen, "black", self.bullet_rect)

    def shoot(self):
        self.bullet_rect.x = self.player_rect.x+50
        self.bullet_rect.y = self.player_rect.y+20
        pg.mixer.Sound("./audio/shoot.mp3").play()
        self.isShoot = True
