import pygame
import random
from const import *
from objects import objectNature


class HP(objectNature):

    default_width = 30
    default_height = 30
    default_speed = 6
    radius = 2000
    position_x = DISPLAY_WIDTH + random.randrange(radius, radius+500)
    position_y = 400

    def __init__(self, display, path_image, height=default_height, width=default_width, speed=default_speed):
        objectNature.__init__(self, display, path_image, height, width, speed)
        self.image = pygame.image.load(self.image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    # прорисовка объекта
    def draw(self, point):
        if self.position_x >= -self.width:
            self.display.blit(self.image, (self.position_x, self.position_y))
            self.position_x -= self.speed
        else:
            self.position_x = DISPLAY_WIDTH + random.randrange(self.radius, self.radius + point)
