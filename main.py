import random
import sys
import pygame as pg
from setting import *

#プレイヤークラス
class Player:
    def __init__(self):
        self.player_rect = pg.Rect(100, HEIGHT / 2 - 50, 50, 50)
        self.bullet_rect = pg.Rect(self.player_rect.x+50, self.player_rect.y+20, 10, 10)
        self.isShoot = False
    
    def playerDisp(self):
        pg.draw.rect(screen, "red", self.player_rect)

    def bulletDisp(self):
        pg.draw.rect(screen, "black", self.bullet_rect)

    def shoot(self):
        self.bullet_rect.x = self.player_rect.x+50
        self.bullet_rect.y = self.player_rect.y+20
        self.isShoot = True

#敵クラス
class Enemy:
    def __init__(self):
        self.enemy_rect = pg.Rect(random.randint(200, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)
    
    def enemyDisp(self):
        pg.draw.rect(screen, "blue", self.enemy_rect)

#ゲームクラス
class Game:
    def __init__(self):
        #プレイヤーを生成
        self.player = Player()
        #敵を生成
        self.enemy = Enemy()

    def gameStage(self):
        #---画面を初期化
        screen.fill("white")
        #プレイヤーを描画
        self.player.playerDisp()
        #敵を描画
        self.enemy.enemyDisp()

        #---入力
        key = pg.key.get_pressed()
        vy = 0
        if key[pg.K_UP]:
            vy = -10
        if key[pg.K_DOWN]:
            vy = 10
        if key[pg.K_SPACE]:
            if not self.player.isShoot:
                self.player.shoot()
            
        #---描画、処理
        #プレイヤーの移動
        self.player.player_rect.y += vy
        #プレイヤーが画面外に出ないようにする
        if self.player.player_rect.y < 0:
            self.player.player_rect.y -= vy
        elif self.player.player_rect.y > HEIGHT-50:
            self.player.player_rect.y -= vy

        #弾の処理
        if self.player.isShoot:
            #弾を描画
            self.player.bulletDisp()
            self.player.bullet_rect.x += 40
            #弾が敵に当たったら
            if self.player.bullet_rect.colliderect(self.enemy.enemy_rect):
                #敵を再生成
                self.enemy.enemy_rect.x = random.randint(200, WIDTH - 50)
                self.enemy.enemy_rect.y = random.randint(0, HEIGHT - 50)
                self.player.isShoot = False
            #弾が画面外に出たら装填
            if self.player.bullet_rect.x >= WIDTH:
                self.player.isShoot = False
                
#---ゲームを初期化
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
    
#ゲームを生成
game = Game()

#---ループ
while True:
    #ゲームを開始
    game.gameStage()

    #---画面を更新
    pg.display.update()
    pg.time.Clock().tick(60)

    #---イベント処理
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()