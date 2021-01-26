import sys
import pygame
from settings import Settings
# p232

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height)
    )
    pygame.display.set_caption('Alien Invasion')
    # 设置背景色
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标
        screen.fill(ai_setting.bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
