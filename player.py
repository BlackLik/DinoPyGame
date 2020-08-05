import pygame
import random
from functools import lru_cache
from health import HP
from const import *


# игрок
class player:

    # инцилизация музыки
    pygame.mixer.init()

    # стандартные значения для игрока
    width = 70
    height = 97
    height_jump = 23
    health = 1
    max_health = 3
    img_ticket = 0
    god_mod = False
    default_time_not_death = 45

    # картинки для анимации
    img_animation = [
        pygame.image.load("Dino/Dino0.png"),
        pygame.image.load("Dino/Dino1.png"),
        pygame.image.load("Dino/Dino2.png"),
        pygame.image.load("Dino/Dino3.png"),
        pygame.image.load("Dino/Dino4.png")
    ]
    img_death = []
    for i in range(0, len(img_animation)):
        path = "Dino/Dino-Lose" + str(i) + ".png"
        img_death.append(pygame.image.load(path))
    health_image = pygame.image.load("Effects/heart.png")
    health_image = pygame.transform.scale(health_image, (30, 30))

    # звуки
    jump_sound = pygame.mixer.Sound('Sounds/down.wav')
    jump_sound.set_volume(ALL_SOUNDS * PLAYER_SOUND)
    take_damage_sound = pygame.mixer.Sound('Sounds/drop_1_health.wav')
    take_damage_sound.set_volume(ALL_SOUNDS * SOUND_DAMAGE)

    # позиция объекта
    position_x = DISPLAY_WIDTH // 10
    position_y = DISPLAY_HEIGHT - height - 100

    __make_jump = False
    __jump_counter = height_jump

    def __init__(self, display, clock, time_not_death=default_time_not_death):
        self.display = display
        self.clock = clock
        self.default_time_not_death = self.time_not_death = time_not_death

    # анимация бега
    @lru_cache()
    def draw(self, point):
        if self.img_ticket == 25:
            self.img_ticket = 0
        if not self.__make_jump:
            self.position_y = DISPLAY_HEIGHT - self.img_animation[self.img_ticket // 5].get_height() - 96
            self.display.blit(self.img_animation[self.img_ticket // 5], (self.position_x, self.position_y))
            self.img_ticket += 1
        else:
            self.display.blit(self.img_animation[self.img_ticket // 5], (self.position_x, self.position_y))
        return int(point + 1)

    # проверка на столкновения
    def check_collision(self, barriers, point=0):
        for barrier in barriers:
            if not self.god_mod:
                if barrier.position_y == DISPLAY_HEIGHT - 100 - 50:  # маленький кактус
                    if self.position_y + self.height - 20 >= barrier.position_y:
                        if barrier.position_x <= self.position_x - 10 <= barrier.position_x + barrier.width:
                            self.god_mod = True
                            return True
                        elif barrier.position_x <= self.position_x + self.width - 30 <= barrier.position_x + barrier.width:
                            self.god_mod = True
                            return True
                elif barrier.position_y == DISPLAY_HEIGHT - 100 - 79:
                    if self.__jump_counter <= -1:
                        if self.position_y + self.height - 20 >= barrier.position_y:
                            if barrier.position_x <= self.position_x - 5 <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                            elif barrier.position_x <= self.position_x + self.width - 60 <= barrier.position_x\
                                    + barrier.width:
                                self.god_mod = True
                                return True
                    else:
                        if self.position_y + self.height >= barrier.position_y:
                            if barrier.position_x <= self.position_x <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                            elif barrier.position_x <= self.position_x + self.width <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                elif barrier.position_y == DISPLAY_HEIGHT - 100 - 89:
                    if self.__jump_counter <= -1:
                        if self.position_y + self.height - 20 >= barrier.position_y:
                            if barrier.position_x <= self.position_x - 5 <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                            elif barrier.position_x <= self.position_x + self.width <= barrier.position_x \
                                    + barrier.width:
                                self.god_mod = True
                                return True
                    elif 9 <= self.__jump_counter <= 25:
                        if self.position_y + self.height>= barrier.position_y:
                            if barrier.position_x <= self.position_x - 5 <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                            elif barrier.position_x <= self.position_x + self.width + 20 <= barrier.position_x \
                                    + barrier.width:
                                self.god_mod = True
                                return True
                    else:
                        if self.position_y + self.height >= barrier.position_y:
                            if barrier.position_x <= self.position_x <= barrier.position_x + barrier.width:
                                self.god_mod = True
                                return True
                            elif barrier.position_x <= self.position_x + self.width <= barrier.position_x\
                                    + barrier.width:
                                self.god_mod = True
                                return True
                else:
                    if self.position_y + self.height >= barrier.position_y:
                        if barrier.position_x <= self.position_x <= barrier.position_x + barrier.width:
                            if type(barrier) is HP:
                                barrier.position_x = DISPLAY_WIDTH + random.randrange(barrier.radius,
                                                                                      barrier.radius + point + 1)
                            self.god_mod = True
                            return True
                        elif barrier.position_x <= self.position_x + self.width <= barrier.position_x + barrier.width:
                            if type(barrier) is HP:
                                barrier.position_x = DISPLAY_WIDTH + random.randrange(barrier.radius,
                                                                                      barrier.radius + point + 1)
                            self.god_mod = True
                            return True
        return False

    # максимальное количество жизней
    def check_max_health(self, array_health, point):
        if self.check_collision(array_health, point):
            if self.health < self.max_health:
                self.health += 1

    # проверка на наличие жизей игрока
    def check_health(self, barriers):
        if self.health == 0 and self.check_collision(barriers):
            if not self.__make_jump:
                if self.img_ticket % 5 == 0:
                    self.img_ticket -= 1
                self.display.blit(self.img_death[self.img_ticket // 5], (self.position_x, self.position_y))
                self.clock.tick(FPS)
                pygame.display.update()

            return True
        elif self.check_collision(barriers):
            self.health -= 1
            pygame.mixer.Sound.play(self.take_damage_sound)
        return False

    # время бессмертия
    def tick_death(self):
        if self.god_mod and self.time_not_death >= 0:
            self.time_not_death -= 1
        elif self.god_mod:
            self.time_not_death = self.default_time_not_death
            self.god_mod = False

    # прыжок
    def jump(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.__make_jump:
            self.__make_jump = True
        if self.__make_jump:
            if self.__jump_counter == -18:
                pygame.mixer.Sound.play(self.jump_sound)
            if self.__jump_counter >= -self.height_jump:
                self.position_y -= self.__jump_counter
                self.__jump_counter -= 1
            else:
                self.__jump_counter = self.height_jump
                self.__make_jump = False
