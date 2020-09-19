# файл cloud.py
from const import *
import random
from objects import objectNature


class cloud(objectNature):

    position_x = DISPLAY_WIDTH
    position_y = random.randrange(50, 250)
    default_speed = 2

    def __init__(self, display, image, height, width, speed=default_speed):
        objectNature.__init__(self, display, image, height, width, speed)

    # прорисовка объекта
    def draw(self):
        if self.position_x >= -self.width:
            self.display.blit(self.image, (self.position_x, self.position_y))
            self.position_x -= self.speed
            return True
        else:
            self.position_x = DISPLAY_WIDTH + random.randrange(0, 300)
            return False

    # меняем картинку
    def return_self(self, display, image, height, width):
        self.position_x = DISPLAY_WIDTH + random.randrange(0, 600)
        self.image = image
        self.height = height
        self.width = width
        self.position_y = random.randrange(50, 250)
        display.blit(self.image, (self.position_x, self.position_y))
