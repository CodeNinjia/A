import pygame
from pygame.locals import *
import time


class BattenDown(object):

    def __init__(self, screen_temp):
        self.x = 160
        self.y = 646
        self.screen = screen_temp
        self.image = pygame.image.load("./tupian/progress.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        # self.ball.display()

    def move_left(self):
        self.x -= 20
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += 20
        if self.x > 320:
            self.x = 320

    def key_control(self):
        """用来检测玩家按下的键盘"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        key_pressed = pygame.key.get_pressed()  # 注意这种方式是能够检测到连续按下的，比之前的版本要新

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            print("left")
            self.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            print("right")
            self.move_right()


class BattenUp(object):

    def __init__(self, screen_temp):
        self.x = 160
        self.y = 2
        self.screen = screen_temp
        self.image = pygame.image.load("./tupian/progress.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Ball(object):

    def __init__(self, screen_temp):
        self.x = 229
        self.y = 24
        self.screen = screen_temp
        self.image = pygame.image.load("./tupian/bullet.png")
        self.direction_x = "left"
        self.direction_y = "down"

    def __del__(self):
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.direction_y == "up":
            self.y -= 20
        elif self.direction_y == "down":
            self.y += 20
        if self.x < 0:
            self.direction_x = "right"
        elif self.x > 458:
            self.direction_x = "left"
        if self.direction_x == "right":
            self.x += 20
        elif self.direction_x == "left":
            self.x -= 20


def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)
    background_image = pygame.image.load("./tupian/background.png")
    batten_down = BattenDown(screen)
    batten_up = BattenUp(screen)
    ball = Ball(screen)
    while True:
        screen.blit(background_image, (0, 0))
        batten_down.display()
        batten_down.key_control()
        batten_up.x = ball.x-80
        batten_up.display()
        ball.display()
        ball.move()
        if (ball.y == (batten_down.y-22)) and (ball.x > (batten_down.x-11)) and (ball.x < (batten_down.x+171)):
            ball.direction_y = "up"
        if ball.y == (batten_up.y+22):
            ball.direction_y = "down"
        if ball.y > 852:
            # del ball
            exit()
        pygame.display.update()
        time.sleep(0.1)
if __name__ == "__main__":
    main()