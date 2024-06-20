import pygame
import sys
def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    eye_delta_x = 0
    eye_delta_y = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((255, 255, 255))  # white
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            eye_delta_y = eye_delta_y - 4
        if pressed_keys[pygame.K_DOWN]:
            eye_delta_y = eye_delta_y + 4
        if pressed_keys[pygame.K_LEFT]:
            eye_delta_x = eye_delta_x - 4
        if pressed_keys[pygame.K_RIGHT]:
            eye_delta_x = eye_delta_x + 4
        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline
        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil
        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_delta_x, 162 + eye_delta_y), 7)  # black pupil
        pygame.draw.circle(screen,"red",(320,240),(40),)
        pygame.draw.circle(screen, "black", (320, 240), (40),(5) )
        pygame.draw.circle(screen, "white", (330, 230), (20), )
        pygame.draw.rect(screen, "black", (320-90, 300, 180, 30),)
        pygame.display.update()
main()
