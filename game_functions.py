
import pygame
import sys
from square import Square
from random import randint


def check_events(ng_settings, squares, stats, hintboard, button, screen):
    '''检测键盘和鼠标事件'''
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        # 键盘
        if event.type == pygame.KEYDOWN:
            if stats.game_active:
                if event.key == pygame.K_SPACE:
                    stats.change_mouse_func()
                    hintboard.prep_mouse_func()
        # 鼠标
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if stats.game_active:
                check_click_squares(squares, ng_settings, mouse_x, mouse_y, stats, hintboard)
            else:
                check_click_button(mouse_x, mouse_y, button, stats, squares, ng_settings, screen, hintboard)

def create_square(ng_settings, screen, squares_l, x_number, y_number, stats):
    '''创建一个格子'''
    square = Square(screen, ng_settings)
    square.rect.x = 10 + x_number * (ng_settings.squares_size + ng_settings.gap_space)
    square.rect.y = 10 + y_number * (ng_settings.squares_size + ng_settings.gap_space)

    # 格子有50%可能为FILL
    r = randint(0, 1)
    if r:
        square.FILL = True
        square.NOTHING = False
        stats.fill_total += 1
        square.set_fill_color()

    squares_l.append(square)

def create_lattice(squares, ng_settings, screen, stats):
    '''创建格子板'''
    # 15列
    for x_number in range(15):
        squares_l = []
        # 15行
        for y_number in range(15):
            create_square(ng_settings, screen, squares_l, x_number, y_number, stats)
        squares.append(squares_l)
    # 控制FILL的比例
    if stats.fill_total < int((ng_settings.game_size ** 2) * 0.5):
        squares.clear()
        create_lattice(squares, ng_settings, screen, stats)
    else:
        print(stats.fill_total)

def count_single_x(squares, y):
    '''计算一行的hint'''
    count = []
    n = 0
    for i in range(15):
        if squares[i][y].FILL:
            if i != 14 and squares[i+1][y].FILL is not True:
                n += 1
                count.append(n)
                n = 0
            elif i == 14:
                n += 1
                count.append(n)
            else:
                n += 1
    return count

def count_single_y(squares, x):
    '''计算一列的hint'''
    count = []
    n = 0
    for j in range(15):
        if squares[x][j].FILL:
            if j != 14 and squares[x][j+1].FILL is not True:
                n += 1
                count.append(n)
                n = 0
            elif j == 14:
                n += 1
                count.append(n)
            else:
                n += 1
    return count

def count_vertical(squares):
    '''计算垂直（全部行）的hint'''
    verhint = []
    for y in range(15):
        xhint = count_single_x(squares, y)
        verhint.append(xhint)
    return verhint

def count_horizontal(squares):
    '''计算水平（全部列）的hint'''
    horhint = []
    for x in range(15):
        yhint = count_single_y(squares, x)
        horhint.append(yhint)
    return horhint

def check_click_squares(squares, ng_settings, mouse_x, mouse_y, stats, hintboard):
    '''检测鼠标的点击'''
    for list in squares:
        for square in list:
            # 检测鼠标点击与方块的碰撞
            square_clicked = square.rect.collidepoint(mouse_x, mouse_y)
            if square_clicked:
                # 点击成功
                if stats.set_FILL:
                    # 鼠标功能为判断FILL
                    check_fill(square, stats, hintboard)
                else:
                    # 鼠标功能为判断NOTHING
                    check_nothing(square, stats, hintboard)

def check_fill(square, stats, hintboard):
    '''点击后检测方格是否为FILL'''
    if square.FILL:
        print("判断为FILL成功")
        square.set_fill_color()
        stats.fill_total -= 1
        if stats.fill_total == 0:
            print("解题成功!")
    else:
        print("判断为FILL失败")
        stats.lives_left -= 1
        hintboard.prep_lives_left()
        if stats.lives_left == 0:
            print("解题失败！")
            stats.game_active = False

def check_nothing(square, stats, hintboard):
    '''点击后检测方格是否为NOTHING'''
    if square.NOTHING:
        print("判断为NOTHING成功")
        square.set_nothing_color()
    else :
        print("判断为NOTHING失败")
        # 如果判断NOTHING错误，生命值-1，该方格显示为FILL
        stats.lives_left -= 1
        hintboard.prep_lives_left()
        if stats.lives_left == 0:
            print("解题失败！")
            stats.game_active = False
        else:
            square.set_fill_color()

def check_click_button(mouse_x, mouse_y, button, stats, squares, ng_settings, screen, hintboard):
    '''检测鼠标点击与button的碰撞'''
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(stats, squares, ng_settings, screen, hintboard)

def start_game(stats, squares, ng_settings, screen, hintboard):
    '''重新开始游戏'''
    stats.game_active = True
    stats.reset_stats()
    # 创建格子
    squares.clear()
    create_lattice(squares, ng_settings, screen, stats)
    # 计算hint
    hintboard.count_hint(squares)
    # 创建hint显示板
    hintboard.prep_vertical()
    hintboard.prep_horizontal()
    hintboard.prep_mouse_func()
    hintboard.prep_lives_left()


                
