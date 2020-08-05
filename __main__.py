from time_on_game import tbg
from menu import *
from camp_cactus import *
from camp_nature import *
from camp_health import *
from interface_on_game import *


# инцилизация модулей
pygame.init()
pygame.mixer.init()


# самая игра
def run_game():
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    # назввание игры
    pygame.display.set_caption("Run Dino!")

    # иконка
    icon = pygame.image.load("Backgrounds/dinosaur-icon.png")
    pygame.display.set_icon(icon)

    # интерфейс
    pas = button(display, 380, 10, 90, 50, "Stop", Silver, Gold)

    # background
    land = tbg()

    # музыка
    pygame.mixer.music.load("Sounds/Background.wav")
    pygame.mixer.music.set_volume(ALL_SOUNDS * BACKGROUND_SOUND)
    pygame.mixer.music.play(-1)
    game_over_sound = pygame.mixer.Sound('Sounds/Game_over.wav')
    game_over_sound.set_volume(ALL_SOUNDS * SOUND_DAMAGE)

    # прочие объекты
    stn = arr_create_stone(display)
    cld = arr_create_cloud(display)
    array_health = arr_create_health(display)

    point = 0

    # таймер
    clock = pygame.time.Clock()

    # герой
    dino = player(display, clock)

    # противники
    camp_enemy = arr_create_enemy(display)

    game = True

    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # действия
        pause(display, clock, pas)

        # background
        display.blit(land.now(point), (0, 0))
        print_text(display, "Point", 30, 30)
        print_text(display, point, 110, 30)
        print_text(display, "Record", DISPLAY_WIDTH - 200, 30)
        score(display, point)
        health_draw(display, dino)
        pas.draw()

        # движение прочих объектов
        draw_random_stone(stn, display)
        draw_random_cloud(cld, display)
        array_draw_health(array_health, point)

        # отрисовка героя главного
        point = dino.draw(point)

        # действия героя
        dino.jump()
        dino.check_max_health(array_health, point)
        if dino.check_health(camp_enemy):
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(game_over_sound)
            game = False
        dino.tick_death()

        # отрисовка противника
        arr_draw_enemy(camp_enemy, display)

        # обновление дисплея
        pygame.display.update()

        # кадров в секунду
        clock.tick(FPS)

    return game_over(display, clock)


if __name__ == "__main__":
    while menu():
        while run_game():
            pass
    pygame.quit()
    quit()
