
from pygame.sprite import Sprite
import pygame

class Square(Sprite):
    '''表示每个格子的类'''

    def __init__(self, screen, ng_settings):
        '''初始化'''
        super(Square, self).__init__()
        self.screen = screen
        self.ng_settings = ng_settings

        # 创建矩形
        self.rect = pygame.Rect(10, 10, ng_settings.squares_size, 
            ng_settings.squares_size)

        # 基础属性
        self.color = ng_settings.squares_color

        # 格子状态
        self.FILL = False
        self.NOTHING = True

    def set_fill_color(self):
        '''把格子设置成FILL颜色'''
        self.color = self.ng_settings.squares_fill_color
    
    def set_nothing_color(self):
        '''把格子设置成NOTHING颜色'''
        self.color = self.ng_settings.squares_nothing_color

    def draw_square(self):
        '''绘制格子'''
        # pygame.draw.rect(self.screen, self.color, self.rect, self.ng_settings.rim_size)
        pygame.draw.rect(self.screen, self.color, self.rect)

        


