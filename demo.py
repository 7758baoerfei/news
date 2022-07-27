# 导入pygame
import pygame
#   设置窗口大小
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BG_COLOR = pygame.Color(100, 149, 237)
TEXT_COLOR = (220, 20, 60)

# 主类
class MainGamg():
    window = None
    # 初始化
    def __init__(self):
        pass
    # 开始游戏
    def startGame(self):
        # 加载主窗口, 初始化窗口
        pygame.display.init()
    #  设置窗口的大小及显示
        MainGamg.widow = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # 设置窗口名称
        pygame.display.set_caption('坦克大战')
        # 初始化我方坦克
        MainGamg.my_tank = Tank(300, 200)
        while True:
            # 给窗口填充颜色
            MainGamg.widow.fill(BG_COLOR)
    # 调用事件
            self.getEvent()
            #     绘制文字,不能用字符串显示
            MainGamg.widow.blit(self.getTtextSuface('敌方坦克剩余数量%d'% 10), (10, 10))
    #         调用显示坦克的方法
            MainGamg.my_tank.displaytank()

    # 更新窗口
            pygame.display.update()
    #         左上角文字绘制
    def getTtextSuface(self, text):
        # 初始化字体模块
        pygame.font.init()
    #     查看字体名称
    #     print(pygame.font.get_fonts())
    # 获取字体Font对象
        font = pygame.font.SysFont('Kaiti', 18)
    #     绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return  textSurface
    # 获取事件（在屏幕中的所有操作都为事件）
    def getEvent(self):
        # 获取所有事件
        eventlist = pygame.event.get()
        # 遍历事件
        for event in eventlist:
            # 判断是否点击关闭
            if event.type == pygame.QUIT:
                self.endGame()
    #         判断键盘是否操作
            if event.type == pygame.KEYDOWN:
                #   判断方向键
                if event.key == pygame.K_LEFT:
                    print('按下左键，坦克是否向左移动')
                elif event.key == pygame.K_RIGHT:
                    print('按下右键，坦克是否向右移动')
                elif event.key == pygame.K_UP:
                    print('按下上键，坦克是否向上移动')
                elif event.key == pygame.K_DOWN:
                    print('按下下键，坦克是否向左移动')


    # 结束游戏
    def endGame(self):
        print('下次再见')
        exit()
# 坦克类
class Tank():
    def __init__(self, left, top):
        # 保存加载图片
        self.images = {'U':pygame.image.load('img/bullet_up'),
                       'D':pygame.image.load('img/bullet_down'),
                       'L':pygame.image.load('img/bullet_left'),
                       'R':pygame.image.load('img/bullet_right') }
        # 方向
        self.direction = 'U'
        # 根据当前图片的方向获取图片
        self.images = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.images.ge_rect()  # 默认位置为左上角
        # 设置区域
        self.rect.left = left
        self.rect.top = top
        # pass
    # 移动
    def move(self):
        pass
    # 射击
    def shot(self):
        pass
    # 展示坦克的方法
    def displaytank(self):
        # 获取展示对象
        self.images = self.images[self.direction]
        # 调用bilt方法展示
        MainGamg.window.blit(self.images, self.rect)
        pass
# 我方坦克
class MyTank(Tank):
     def __init__(self):
         pass
# 敌方坦克
class EnemyTank(Tank):
      def __init__(self):
         pass
# 墙壁
class wall():
    def __init__(self):
        pass
    # 展示墙壁的方法
    def displaywall(self):
        pass
# 子弹类
class Bullet():
    def __init__(self):
        pass
    # 移动
    def move(self):
        pass
    # 展示子弹的方法
    def displayBullet(self):
        pass
# 爆炸类
class Explode():
    def __init__(self):
        pass
    def displayExplode(self):
        pass
# 播放音乐
class Music():
    def __init__(self):
        pass
    # 播放音乐
    def play(self):
        pass
t = MainGamg()
t.startGame()
