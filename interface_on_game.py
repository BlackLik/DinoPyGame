import pygame
from const import *
from player import player


def print_text(display, message, x, y, font_color=(0, 0, 0),
               font_type='Effects/PingPong.ttf', font_size=30):
    message = str(message)
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


# лучший результат
def score(display, point):
    sc = open("score.txt", "r")
    high_score = sc.read()
    high_score_in_no = int(high_score)
    print_text(display, high_score_in_no, DISPLAY_WIDTH - 100, 30)
    sc.close()
    if point > high_score_in_no:
        sc = open("score.txt", "w")
        sc.write(str(point))
        sc.close()


# пауза
def pause(display, clock, button_pause):
    key = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if key[pygame.K_ESCAPE] or (button_pause.x < mouse[0] < button_pause.x + button_pause.width and button_pause.y
                                < mouse[1] < button_pause.y + button_pause.height and click[0] == 1):
        paused = True
        pygame.mixer.music.pause()

        while paused:

            key = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text(display, "Paused! Press ENTER to continue", DISPLAY_WIDTH // 4, 150)
            print_text(display, "Paused! Press Q to quit the game", DISPLAY_WIDTH // 4, 200)

            if key[pygame.K_RETURN]:
                paused = False
            if key[pygame.K_q]:
                pygame.quit()
                quit()

            pygame.display.update()
            clock.tick(FPS)

        pygame.mixer.music.unpause()


def game_over(display, clock):
    stopped = True
    while stopped:
        key = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text(display, "Game Over.", 300, 150, font_size=40)
        print_text(display, "Press Enter to play again", 210, 225, font_size=23)
        print_text(display, "Press Q to go to the menu", 210, 275, font_size=23)

        if key[pygame.K_RETURN]:
            return True
        if key[pygame.K_q]:
            return False

        pygame.display.update()
        clock.tick(FPS)


# выводит на экран колличество hp игрока
def health_draw(display, dino: player):
    show = 0
    health_player = dino.health
    x = 25
    while show != health_player:
        display.blit(dino.health_image, (x, 60))
        x += dino.health_image.get_width() + 5
        show += 1
