
import pygame
import game_functions as gf

class Hintboard():
    '''显示hint的类'''

    def __init__(self, screen, ng_settings, squares, stats):
        self.screen = screen
        self.ng_settings = ng_settings
        self.squares = squares
        self.stats = stats
        self.count_hint(squares)

        # hint字体设置
        self.text_color = (0, 100, 100)
        self.font = pygame.font.SysFont(None, 20)

        # 准备行列hint
        self.prep_vertical()
        self.prep_horizontal()
        self.prep_mouse_func()
        self.prep_lives_left()

    def count_hint(self, squares):
        '''计算hint'''
        self.verhint = gf.count_vertical(squares)
        self.horhint = gf.count_horizontal(squares)

    def prep_vertical(self):
        '''将垂直方向的hint转换为渲染的图像'''
        self.verhint_images = []
        self.verhint_rects = []
        for i in range(15):
            # 把一行的hint转换为图像
            blank = ' '
            hint_str = blank.join([str(n) for n in self.verhint[i]])
            verhint_image = self.font.render(hint_str, True, self.text_color, self.ng_settings.bg_color)

            # 设置hint图像位置
            verhint_rect = verhint_image.get_rect()
            verhint_rect.centery = self.squares[14][i].rect.centery
            verhint_rect.left = self.squares[14][i].rect.right + 30

            # 保存数据
            self.verhint_images.append(verhint_image)
            self.verhint_rects.append(verhint_rect)

    def prep_horizontal(self):
        '''将水平方向的hint转换为渲染的图像'''
        self.horhint_images = []
        self.horhint_rects = []
        for i in range(15):
            # 把一列的hint转换为图像
            blank_line = ' '
            hint_str = blank_line.join([str(n) for n in self.horhint[i]])
            horhint_image = self.font.render(hint_str, True, self.text_color, self.ng_settings.bg_color)
            horhint_image = pygame.transform.rotate(horhint_image, -90.0)

            # 设置hint图像位置
            horhint_rect = horhint_image.get_rect()
            horhint_rect.centerx = self.squares[i][14].rect.centerx
            horhint_rect.top = self.squares[i][14].rect.bottom + 30

            # 保存数据
            self.horhint_images.append(horhint_image)
            self.horhint_rects.append(horhint_rect)

    def prep_mouse_func(self):
        '''渲染鼠标当前点击功能为FILL或NOTHING'''
        if self.stats.set_FILL:
            self.func_str = "FILL"
        else:
            self.func_str = "NOTHING"
        self.func_image = self.font.render(self.func_str, True, self.text_color, self.ng_settings.bg_color)

        # 图像位置
        self.func_rect = self.func_image.get_rect()
        self.func_rect.right = self.ng_settings.screen_size[0] - 30
        self.func_rect.top = 30
     
    def prep_lives_left(self):
        '''渲染剩余生命的多少'''
        self.life_str = str(self.stats.lives_left)
        self.life_image = self.font.render(self.life_str, True, self.text_color, self.ng_settings.bg_color)

        self.life_rect = self.life_image.get_rect()
        self.life_rect.right = self.ng_settings.screen_size[0] - 30
        self.life_rect.top = 70


    def show_hint(self):
        '''在屏幕上显示hint'''
        for i in range(15):
            self.screen.blit(self.verhint_images[i], self.verhint_rects[i])
            self.screen.blit(self.horhint_images[i], self.horhint_rects[i])
        self.screen.blit(self.func_image, self.func_rect)
        self.screen.blit(self.life_image, self.life_rect)
        
    


