import pygame
from const import *
import random
from objects import objectNature


class stone(objectNature):

    position_x = DISPLAY_WIDTH
    position_y = DISPLAY_HEIGHT - random.randrange(0, 95)
    default_speed = 6

    def __init__(self, display, image, height, width, speed=default_speed):
        objectNature.__init__(self, display, image, height, width, speed)

    # прорисовка объекта
    def draw(self):
        if self.position_x >= -self.width:
            self.display.blit(self.image, (self.position_x, self.position_y))
            self.position_x -= self.speed
            return True
        else:
            self.position_x = DISPLAY_WIDTH
            return False

    # меняем картинку
    def return_self(self, display, image, height, width):
        self.position_x = DISPLAY_WIDTH + random.randrange(0, 500)
        self.image = image
        self.height = height
        self.width = width
        self.position_y = DISPLAY_HEIGHT - random.randrange(0, 95)
        display.blit(self.image, (self.position_x, self.position_y))
