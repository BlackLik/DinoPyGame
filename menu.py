# файл menu.py
import pygame
from interface_on_game import print_text
from col import *
from const import *


class button:
    sound = pygame.mixer.Sound("Sounds/button.wav")

    def __init__(self,
                 display,
                 x: int,
                 y: int,
                 width: int,
                 height: int,
                 message,
                 inactive_color=CadetBlue,
                 active_color=LightSteelBlue,
                 font_size: int = 30
                 ):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.message = message
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.font_size = font_size

    def draw(self, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(self.display, self.active_color, (self.x, self.y, self.width, self.height))

            if click[0] == 1:
                pygame.mixer.Sound.play(self.sound)
                pygame.time.delay(300)
                if action is not None:
                    action()

        else:
            pygame.draw.rect(self.display, self.inactive_color, (self.x, self.y, self.width, self.height))
        print_text(self.display, self.message, self.x + 10, self.y + 10, font_size=self.font_size)


def menu():
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # назввание игры
    pygame.display.set_caption("Run Dino!")

    # иконка
    icon = pygame.image.load("Backgrounds/dinosaur-icon.png")
    pygame.display.set_icon(icon)

    # background
    menu_background = []
    for i in range(1, 3):
        path_img = "Backgrounds/menu" + str(i) + ".png"
        menu_background.append(pygame.image.load(path_img))
    background_tick = 0

    # музыка
    pygame.mixer.music.load("Sounds/Background.wav")
    pygame.mixer.music.set_volume(ALL_SOUNDS * BACKGROUND_SOUND)
    pygame.mixer.music.play(-1)

    # таймер
    clock = pygame.time.Clock()

    # интерфейс
    start_button = button(display, 350, 200, 100, 50, "Start", Lime, Green)
    exit_button = button(display, 350, 300, 100, 50, " Exit", Lime, Green)

    show = True
    while show:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if exit_button.x < mouse[0] < exit_button.x + exit_button.width \
                and exit_button.y < mouse[1] < exit_button.y + exit_button.height \
                and click[0] == 1:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(menu_background[background_tick // 25], (0, 0))

        # анимация главного меню
        if background_tick == 49:
            background_tick = 0
        else:
            background_tick += 1

        # интерфейс
        start_button.draw()
        exit_button.draw()

        # действия
        show = start_gm(show, start_button)

        # обновление дисплея
        pygame.display.update()

        # кадров в секунду
        clock.tick(FPS)

    return exit_program(exit_button)


def start_gm(show, start_game: button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    new_show = show
    if start_game.x < mouse[0] < start_game.x + start_game.width \
            and start_game.y < mouse[1] < start_game.y + start_game.height \
            and click[0] == 1 \
            and new_show:
        new_show = False

    return new_show


def exit_program(exit_btn: button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if exit_btn.x < mouse[0] < exit_btn.x + exit_btn.width \
            and exit_btn.y < mouse[1] < exit_btn.y + exit_btn.height \
            and click[0] == 1:
        return False
    return True
