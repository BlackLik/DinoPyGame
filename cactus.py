from const import *
import random
from objects import objectNature


class cactus(objectNature):

    first_circle = True
    default_height = 70
    default_width = 20
    default_speed = 6

    def __init__(self, display, image, height=default_height, width=default_width, speed=default_speed):
        objectNature.__init__(self, display, image, height, width, speed)
        self.position_y = DISPLAY_HEIGHT - self.height - 100
        random_number = random.randrange(0, 300)
        if random_number <= 100:
            self.position_x = DISPLAY_WIDTH + random_number
        else:
            self.position_x = DISPLAY_WIDTH + random.randrange(275, 300)
        self.path_image = image

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
    def return_self(self, display, radius, image, height, width):
        self.position_x = radius
        self.image = image
        self.height = height
        self.width = width
        self.position_y = DISPLAY_HEIGHT - 100 - height
        display.blit(self.image, (self.position_x, self.position_y))
