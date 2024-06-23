import pygame
import sys
import time
import random


class Raindrop:
    def __init__(self, screen, x, y):
        """ Creates a Raindrop sprite that travels down at a random speed. """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)


    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        self.y = self.y + self.speed



    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        return self.y > self.screen.get_height()


        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.



    def draw(self):
        pygame.draw.line(self.screen, pygame.Color("blue"),(self.x, self.y),(self.x, self.y+5),2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0



    def draw(self):
        """ Draws this sprite onto the screen. """
        self.screen.blit(self.image_no_umbrella, (self.x, self.y))

        if time.time() - self.last_hit_time > 1:
            self.screen.blit(self.image_no_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_umbrella, (self.x, self.y))


    def hit_by(self, raindrop):
        """ Returns true if the given raindrop is hitting this Hero, otherwise false. """

        hero_hit_box = pygame.Rect(self.x, self.y, self.image_no_umbrella.get_width(),self.image_no_umbrella.get_height())
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)




class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """

        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []


    def draw(self):
        """ Draws this sprite onto the screen. """

        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """

        new_drop = Raindrop(self.screen, random.randint(self.x, self.x + self.image.get_width()), self.y + self.image.get_height())
        self.raindrops.append(new_drop)

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    clock = pygame.time.Clock()
    test_drop = Raindrop(screen, 300, 10)
    mike = Hero (screen, 200, 400,"Mike_umbrella.png","Mike.png")
    alyssa = Hero (screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    cloud = Cloud(screen,300, 50, "cloud.png")


    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()




        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10
        screen.fill(pygame.Color("white"))

        # --- begin area of test_drop code that will be removed later

        # test_drop.move()
        # if test_drop.off_screen():
        #     test_drop.y = 10
        # test_drop.draw()
        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()
        #     test_drop.x = 750
        #     test_drop.y = 10
        # if alyssa.hit_by(test_drop):
        #     alyssa.last_hit_time = time.time()
        #     test_drop.x = 300
        #     test_drop.y = 10




        # --- end area of test_drop code that will be removed later



            # TODO  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        cloud.draw()
        mike.draw()
        alyssa.draw()

        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        pygame.display.update()



main()
