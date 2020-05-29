
class GameStats():
    '''跟踪游戏信息'''
    def __init__(self):
        self.reset_stats()

        # 鼠标点击功能属性
        self.set_FILL = True

        # 游戏状态
        self.game_active = False

    def change_mouse_func(self):
        '''更改鼠标点击功能'''
        if self.set_FILL:
            self.set_FILL = False
        else:
            self.set_FILL = True

    def reset_stats(self):
        '''初始化游戏运行期间的信息'''
        # 游戏生命次数剩余量
        self.lives_left = 3
        self.fill_total = 0        
