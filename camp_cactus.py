import pygame
from cactus import cactus
from const import *
import random


# список врагов
def arr_image():
    arr_enemy = [
        {
            "image": pygame.image.load('Objects/Cactus0.png'),
            "height": 50,
            "width": 69
        },
        {
            "image": pygame.image.load('Objects/Cactus1.png'),
            "height": 89,
            "width": 37
        },
        {
            "image": pygame.image.load('Objects/Cactus2.png'),
            "height": 79,
            "width": 40
        },
    ]
    return arr_enemy


# создание врагов врагов
def arr_create_enemy(display):
    array = arr_image()
    choice = []
    for index in range(len(array)):
        choice.append(random.randrange(0, len(array)))

    camp_enemy = []
    for index in range(0, len(array)):
        camp_enemy.append(cactus(display, array[choice[index]]["image"], array[choice[index]]["height"],
                                 array[choice[index]]["width"]))
    return camp_enemy


# проверка на спавн врагов
def arr_draw_enemy(array, display):
    array_enemy = arr_image()
    for enemy in array:
        check = enemy.draw()
        if not check:
            radius = find_radius(array)
            choice = random.randrange(0, len(array))
            enemy.return_self(display, radius,
                              array_enemy[choice]["image"],
                              array_enemy[choice]["height"],
                              array_enemy[choice]["width"])


# алгоритм спавна кактусов
def find_radius(array):
    maximum = max(array[0].position_x, array[1].position_x, array[2].position_x)

    if maximum < DISPLAY_WIDTH:
        radius = DISPLAY_WIDTH
        if radius - maximum < 200:
            radius += 200
    else:
        radius = maximum

    choice = random.randrange(0, 5)

    if choice == 0:
        radius += random.randrange(15, 85)
    else:
        radius += random.randint(300, 450)

    return radius
