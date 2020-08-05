import pygame
from const import *
import random
from stone import stone
from cloud import cloud


# объекты возможных камней
def arr_cloud():
    array_cloud = [
        {
            "image": pygame.image.load("Objects/Cloud0.png"),
            "height": 34,
            "width": 62
        },
        {
            "image": pygame.image.load("Objects/Cloud1.png"),
            "height": 37,
            "width": 80
        }
    ]
    return array_cloud


# объекты возможных облаков
def arr_stone():
    array_stone = [
        {
            "image": pygame.image.load("Objects/Stone0.png"),
            "height": 9,
            "width": 9
        },
        {
            "image": pygame.image.load("Objects/Stone1.png"),
            "height": 9,
            "width": 12
        }
    ]
    return array_stone


# создание массива с камнями
def arr_create_stone(display):
    array = []
    for i in range(5):
        array += arr_stone()
    choice = []
    for index in range(len(array)):
        choice.append(random.randrange(0, len(array)))

    camp_stone = []
    for index in range(0, len(array)):
        camp_stone.append(stone(display, array[choice[index]]["image"], array[choice[index]]["height"],
                                array[choice[index]]["width"]))
    return camp_stone


# создание массива с облаками
def arr_create_cloud(display):
    array = []
    for i in range(3):
        array += arr_cloud()
    choice = []
    for index in range(len(array)):
        choice.append(random.randrange(0, len(array)))

    camp_cloud = []
    for index in range(0, len(array)):
        camp_cloud.append(cloud(display, array[choice[index]]["image"], array[choice[index]]["height"],
                                array[choice[index]]["width"]))
    return camp_cloud


# движение камней
def draw_random_stone(array, display):
    stones = arr_stone()
    for stone in array:
        check = stone.draw()
        if not check:
            choice = random.randrange(0, len(stones))
            stone.return_self(display,
                              stones[choice]["image"],
                              stones[choice]["height"],
                              stones[choice]["width"])


# движение облаков
def draw_random_cloud(array, display):
    clouds = arr_cloud()
    for cloud in array:
        check = cloud.draw()
        if not check:
            choice = random.randrange(0, len(clouds))
            cloud.return_self(display,
                              clouds[choice]["image"],
                              clouds[choice]["height"],
                              clouds[choice]["width"])
