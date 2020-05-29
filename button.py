import pygame

class Button():
    '''按钮的类'''

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 按钮属性
        self.width, self.height = 200, 50
        self.button_color = (0, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # 按钮的rect对象
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 渲染按钮上的标签
        self.prep_msg()

    def prep_msg(self):
        '''把按钮上的标签文字渲染成图像'''
        self.msg = 'PLAY'
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center

    def draw_button(self):
        '''把按钮显示在屏幕上'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)