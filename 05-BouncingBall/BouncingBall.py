import pygame
import sys
import random
class ball:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(101, 899)
        self.y = random.randint(101, 599)
        self.speedx = random.randint(-10, 10)
        self.speedy = random.randint(-10, 10)
        self.size = random.randint(10,50)
        self.color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    def draw(self):
         pygame.draw.circle(self.screen, color=self.color,center=(self.x, self.y), radius=self.size)
    def move(self):
        self.x = self.x + self.speedx
        self.y = self.y + self.speedy
        if self.x < 0 + self.size:
            self.speedx = self.speedx * -1
        if self.x > 1000 - self.size:
            self.speedx = self.speedx * -1
        if self.y < 0 + self.size:
            self.speedy = self.speedy * -1
        if self.y > 700 - self.size:
            self.speedy = self.speedy * -1
def main():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    for i in range(0, 100):
        new_ball = ball(screen)
        balls.append(new_ball)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        for new_ball in balls:
            new_ball.move()
            new_ball.draw()
        pygame.display.update()
main()