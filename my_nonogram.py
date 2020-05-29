
import pygame
import sys
from settings import Ng_settings
from pygame.sprite import Group
from square import Square
import game_functions as gf
from hintboard import Hintboard
from game_stats import GameStats
from button import Button

def run_game():
    # 初始化游戏并创建一个屏幕
    ng_settings = Ng_settings()
    pygame.init()
    screen = pygame.display.set_mode(ng_settings.screen_size)

    # 创建游戏开始按钮
    button = Button(screen)
    # 创建游戏统计数据
    stats = GameStats()
    # 创建格子
    squares = []
    gf.create_lattice(squares, ng_settings, screen, stats)
    # 创建hint显示板
    hintboard = Hintboard(screen, ng_settings, squares, stats)

    # 游戏主循环
    while True:

        gf.check_events(ng_settings, squares, stats, hintboard, button, screen)
        
        # 重绘屏幕
        screen.fill(ng_settings.bg_color)

        # 根据游戏状态显示开始按钮或者方格盘
        if not stats.game_active:
            button.draw_button()
        else:
            for x in range(15):
                for y in range(15):
                    squares[x][y].draw_square()
            hintboard.show_hint()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()