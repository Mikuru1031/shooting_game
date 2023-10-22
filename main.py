import sys
import pygame as pg
from setting import *
from game import Game
                
##ゲームを初期化
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
    
#ゲームを生成
game = Game()

##ループ
while True:
    #ゲームを開始
    game.gameStage()

    ##画面を更新
    pg.display.update()
    pg.time.Clock().tick(60)

    ##イベント処理
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()