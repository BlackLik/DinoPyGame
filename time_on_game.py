import pygame
from const import *


class tbg:

    day = []
    for i in range(1, 16):
        path = "Backgrounds/land-sand" + str(i) + ".png"
        day.append(pygame.image.load(path))

    night = []
    for i in range(0, len(day)):
        night.append(day[len(day) - i - 1])

    __animation = False
    __true_day = False
    __now_time = day[0]
    __tick = 0

    # возвращает текущию локацию
    def now(self, point):

        point = int(point)
        if point % FLIP_TIME_POINT == 1 and point >= FLIP_TIME_POINT + 1:
            self.__animation = True

        if self.__animation:
            self.__tick += 1

            if self.__tick == 15:
                self.__tick = 0
                self.__animation = False
                if self.__true_day:
                    self.__true_day = False
                else:
                    self.__true_day = True

            if self.__true_day:
                self.__now_time = self.night[self.__tick]
            else:
                self.__now_time = self.day[self.__tick]

        return self.__now_time
