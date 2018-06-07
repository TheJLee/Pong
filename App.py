import pygame as pygame
from Paddle import Paddle
from Ball import Ball

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
FPS = 200

class App:
    def __init__(self):
        self.display = None
        self.clock = None
        self.paddle1 = Paddle(WINDOWWIDTH/2,0)
        self.paddle2 = Paddle(WINDOWWIDTH/2,WINDOWHEIGHT)
        self.ball = Ball(WINDOWWIDTH/2,WINDOWHEIGHT/2)

    def setup(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        
    def play(self):
        self.setup()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    App = App()
    App.play()
