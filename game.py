import pygame as pg
from setting import *
import random
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        #スクリーンを取得
        self.screen = pg.display.get_surface()
        #プレイヤーを生成
        self.player = Player()
        #敵を生成
        self.enemy = Enemy()

    def gameStage(self):
        ##画面を初期化
        self.screen.fill("white")

        ##入力
        key = pg.key.get_pressed()
        vy = 0
        if key[pg.K_UP]:
            vy = -10
        if key[pg.K_DOWN]:
            vy = 10
        if key[pg.K_SPACE]:
            #弾を撃つ
            if not self.player.isShoot:
                self.player.shoot()
        
        mdown = pg.mouse.get_pressed()
        (mx, my) = pg.mouse.get_pos()
        if mdown[0]:
            #敵をクリックで倒す
            if self.enemy.enemy_rect.collidepoint(mx, my):
                self.enemy.enemy_rect.x = random.randint(200, WIDTH - 50)
                self.enemy.enemy_rect.y = random.randint(0, HEIGHT - 50)
            
        ##描画、処理
        #プレイヤーを描画
        self.player.playerDisp()

        #敵を描画
        self.enemy.enemyDisp()

        #プレイヤーの移動
        self.player.player_rect.y += vy
        #プレイヤーが画面外に出ないようにする
        if self.player.player_rect.y < 0:
            self.player.player_rect.y -= vy
        elif self.player.player_rect.y > HEIGHT-50:
            self.player.player_rect.y -= vy

        #弾を撃った時の処理
        if self.player.isShoot:
            #弾を描画
            self.player.bulletDisp()
            self.player.bullet_rect.x += 30
            #弾が敵に当たったら
            if self.player.bullet_rect.colliderect(self.enemy.enemy_rect):
                #敵を再生成
                self.enemy.enemy_rect.x = random.randint(200, WIDTH - 50)
                self.enemy.enemy_rect.y = random.randint(0, HEIGHT - 50)
                self.player.isShoot = False
            #弾が画面外に出たら装填
            if self.player.bullet_rect.x >= WIDTH:
                self.player.isShoot = False