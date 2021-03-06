import sys
import pygame

from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    # pygame.display.set_caption("Alien Invasion")
    # #设置背景色
    # bg_color = (230,230,230)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    # #创建一个外星人
    # alien = Alien(ai_settings,screen)
    #创建一个外星人编组
    aliens =Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)




    #开始游戏的主循环
    while True:
        #监视键盘和鼠标
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings,screen,ship,bullets)
            #每次循环是重绘屏幕
            # screen.fill(bg_color)
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        ship.update()
        # bullets.update()
        #
        # #删除已消失的子弹
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        gf.update_bullets(aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


        #让最近的屏幕绘制可见
        pygame.display.flip()

run_game()
