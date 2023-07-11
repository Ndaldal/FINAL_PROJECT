import random
import pygame
import time

pygame.init()

screen_width = 1600
screen_height = int(screen_width * (9 / 16))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("20221133 한동국")
clock = pygame.time.Clock()

gear_line = int(screen_width * 0.005)
gear_position = (int(screen_width * 0.01),
                 -gear_line)
gear_size = (int(screen_width * 0.32),
             int(screen_height * 0.9))

score_position = (int(screen_width * 0.01),
                  -gear_line + int(screen_height * 0.9))
score_size = (int(screen_width * 0.32),
              int(screen_height * 0.1))

judgement_line = int(screen_height * 0.005)
judgement_position = (int(screen_width * 0.01),
                      int(screen_height * 0.8))
judgement_size = (int(screen_width * 0.32),
                  int(screen_height * 0.05))

line1_position = (int(screen_width * 0.01) + int(screen_width * 0.08) * 0,
                  -gear_line)
line2_position = (int(screen_width * 0.01 + int(screen_width * 0.08) * 1),
                  -gear_line)
line3_position = (int(screen_width * 0.01) + int(screen_width * 0.08) * 2,
                  -gear_line)
line4_position = (int(screen_width * 0.01) + int(screen_width * 0.08) * 3,
                  -gear_line)
line_size = (int(screen_width * 0.08),
             int(screen_height * 0.9))

note_position = 350
note_size = (int(screen_width * 0.08),
             int(screen_height * 0.05))

key_set = [0, 0, 0, 0]

max_frame = 60
fps = 0

start = time.time()
Time = time.time() - start

t1 = []
t2 = []
t3 = []
t4 = []

BGI = pygame.image.load("assets/P1_00.jpg")
SOUND = pygame.mixer.Sound("./assets/key01.mp3")

font = pygame.font.SysFont("NotoSansKR-Bold.otf", 32, True, True)
text = font.render("", False, 0x111111)


def sum_note(n, t):
    ty = 0
    tst = time.time() - start + t - 0.6

    if n == 1:
        t1.append([ty, tst])
    if n == 2:
        t2.append([ty, tst])
    if n == 3:
        t3.append([ty, tst])
    if n == 4:
        t4.append([ty, tst])


rate_data = [0, 0]

combo, rate_data[1], rate = 0, 0, 0
life = -10
score = 0
score_list = []

speed = 1.0

note_sum_t = 0

a = 0
aa = 0

done = True

starting = True

while done:

    if starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    starting = False
                    life = 100
                    start = time.time()
                    Time = time.time() - start
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()

        screen.blit(BGI, BGI.get_rect())

        MANUAL = font.render(f'YOU CAN USE \' f \' \' g \' \' j \' \' k \' KEY ', False, 0xEEEEEE)
        STARTING = font.render(f'START : SPACEBAR BUTTON', False, 0xEEEEEE)

        pygame.draw.rect(screen, 0x111111, (screen_width / 2 - 270, 400, 600, 100))
        screen.blit(MANUAL, (screen_width / 2 - 130, 435))
        screen.blit(STARTING, (screen_width / 2 - 130, 465))

    if life > 0:
        if Time > 0.2 * note_sum_t:
            note_sum_t += 1
            while a == aa:
                a = random.randint(1, 4)
            sum_note(a, 3)
            aa = a

        fps = clock.get_fps()
        if fps == 0:
            fps = max_frame

        Time = time.time() - start

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
                elif event.key == pygame.K_f:
                    key_set[0] = 1
                elif event.key == pygame.K_g:
                    key_set[1] = 1
                elif event.key == pygame.K_j:
                    key_set[2] = 1
                elif event.key == pygame.K_k:
                    key_set[3] = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    done = False
                elif event.key == pygame.K_f:
                    key_set[0] = 0
                    pass
                elif event.key == pygame.K_g:
                    key_set[1] = 0
                    pass
                elif event.key == pygame.K_j:
                    key_set[2] = 0
                    pass
                elif event.key == pygame.K_k:
                    key_set[3] = 0
                    pass

        screen.blit(BGI, BGI.get_rect())

        pygame.draw.rect(screen, 0x111111, (gear_position, gear_size))
        pygame.draw.rect(screen, 0xEEEEEE, (gear_position, gear_size), gear_line)

        pygame.draw.rect(screen, 0xFF8888, (judgement_position, judgement_size))
        pygame.draw.rect(screen, 0x88DBFF, (judgement_position, judgement_size), judgement_line)

        #  Note Drop
        for tile_data in t1:
            tile_data[0] = int(screen_height * 0.8) + (Time - tile_data[1]) * \
                           note_position * speed * (screen_height / 900)
            pygame.draw.rect(screen, 0x88DBFF, (line1_position[0], int(tile_data[0]),
                                                note_size[0], note_size[1]))
            if (int(screen_height * 0.9)) >= tile_data[0] >= (int(screen_height * 0.7)):
                if key_set[0]:
                    SOUND.play(1, 100)
                    rate_data[0] += 1
                    combo += 1
                    rate = "SUCCESS"
                    score += 1
                    if combo <= 10:
                        score += combo
                    elif combo > 10:
                        score += 10
                    if combo >= 10:
                        if combo % 10 == 0:
                            if life + 10 <= 100:
                                life += 10
                    text = font.render(rate, False, 0xEEEEEE)
                    t1.remove(tile_data)
            elif tile_data[0] > (int(screen_height * 0.9)):
                rate_data[1] += 1
                combo = 0
                life -= 10
                rate = "MISS"
                text = font.render(rate, False, 0xEEEEEE)
                if life == 0:
                    score_list.append(score)
                t1.remove(tile_data)

        for tile_data in t2:
            tile_data[0] = int(screen_height * 0.8) + (Time - tile_data[1]) * \
                           note_position * speed * (screen_height / 900)
            pygame.draw.rect(screen, 0xFF8888, (line2_position[0], int(tile_data[0]),
                                                note_size[0], note_size[1]))
            if (int(screen_height * 0.9)) >= tile_data[0] >= (int(screen_height * 0.7)):
                if key_set[1]:
                    SOUND.play(1, 100)
                    rate_data[0] += 1
                    combo += 1
                    rate = "SUCCESS"
                    score += 1
                    if combo <= 10:
                        score += combo
                    elif combo > 10:
                        score += 10
                    if combo >= 10:
                        if combo % 10 == 0:
                            if life + 10 <= 100:
                                life += 10
                    text = font.render(rate, False, 0xEEEEEE)
                    t2.remove(tile_data)
            elif tile_data[0] > (int(screen_height * 0.9)):
                rate_data[1] += 1
                combo = 0
                life -= 10
                rate = "MISS"
                text = font.render(rate, False, 0xEEEEEE)
                if life == 0:
                    score_list.append(score)
                t2.remove(tile_data)

        for tile_data in t3:
            tile_data[0] = int(screen_height * 0.8) + (Time - tile_data[1]) * \
                           note_position * speed * (screen_height / 900)
            pygame.draw.rect(screen, 0x88DBFF, (line3_position[0], int(tile_data[0]),
                                                note_size[0], note_size[1]))
            if (int(screen_height * 0.9)) >= tile_data[0] >= (int(screen_height * 0.7)):
                if key_set[2]:
                    SOUND.play(1, 100)
                    rate_data[0] += 1
                    combo += 1
                    rate = "SUCCESS"
                    score += 1
                    if combo <= 10:
                        score += combo
                    elif combo > 10:
                        score += 10
                    if combo >= 10:
                        if combo % 10 == 0:
                            if life + 10 <= 100:
                                life += 10
                    text = font.render(rate, False, 0xEEEEEE)
                    t3.remove(tile_data)
            elif tile_data[0] > (int(screen_height * 0.9)):
                rate_data[1] += 1
                combo = 0
                life -= 10
                rate = "MISS"
                text = font.render(rate, False, 0xEEEEEE)
                if life == 0:
                    score_list.append(score)
                t3.remove(tile_data)

        for tile_data in t4:
            tile_data[0] = int(screen_height * 0.8) + (Time - tile_data[1]) * \
                           note_position * speed * (screen_height / 900)
            pygame.draw.rect(screen, 0xFF8888, (line4_position[0], int(tile_data[0]),
                                                note_size[0], note_size[1]))
            if (int(screen_height * 0.9)) >= tile_data[0] >= (int(screen_height * 0.7)):
                if key_set[3]:
                    SOUND.play(1, 100)
                    rate_data[0] += 1
                    combo += 1
                    rate = "SUCCESS"
                    score += 1
                    if combo <= 10:
                        score += combo
                    elif combo > 10:
                        score += 10
                    if combo >= 10:
                        if combo % 10 == 0:
                            if life + 10 <= 100:
                                life += 10
                    text = font.render(rate, False, 0xEEEEEE)
                    t4.remove(tile_data)
            elif tile_data[0] > (int(screen_height * 0.9)):
                rate_data[1] += 1
                combo = 0
                life -= 10
                rate = "MISS"
                text = font.render(rate, False, 0xEEEEEE)
                if life == 0:
                    score_list.append(score)
                t4.remove(tile_data)

        if combo >= 10:
            if combo % 10 == 0:
                speed += 0.01

        pygame.draw.rect(screen, 0xA0A0A0, (score_position, score_size))

        COMBO = font.render("COMBO : " + str(combo), False, 0xEEEEEE)
        screen.blit(COMBO, (judgement_position[0] + 200, judgement_position[1] - 150))
        screen.blit(text, (judgement_position[0] + 200, judgement_position[1] - 100))

        SUCCESS = font.render(f'SUCCESS : {str(rate_data[0])}', False, 0xEEEEEE)
        MISS = font.render(f'MISS : {str(rate_data[1])}', False, 0xEEEEEE)
        SCORE = font.render(f'SCORE : {str(score)}', False, 0xEEEEEE)
        screen.blit(SUCCESS, (score_position[0], score_position[1]))
        screen.blit(MISS, (score_position[0] + 200, score_position[1]))
        screen.blit(SCORE, (score_position[0], score_position[1] + 50))

        pygame.draw.rect(screen, 0xEEEEEE, (gear_position[0] + gear_size[0], 100, 40, life *5))
        pygame.draw.rect(screen, 0xFF8888, (gear_position[0] + gear_size[0], 100, 40, 100 * 5), 5)

    elif life == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_SPACE:
                    life = 100
                    note_sum_t = 0
                    combo = 0
                    rate_data[0] = 0
                    rate_data[1] = 0
                    score = 0
                    t1.clear()
                    t2.clear()
                    t3.clear()
                    t4.clear()
                    start = time.time()
                    Time = time.time()
                    text = font.render("RESTART", False, 0xEEEEEE)
        screen.blit(BGI, BGI.get_rect())

        SCORE_LIST = font.render(f'', False, 0xEEEEEE)
        RESTART = font.render(f'RESTART : SPACEBAR BUTTON', False, 0xEEEEEE)

        pygame.draw.rect(screen, 0x111111, (screen_width / 2 - 270, 270, 600, 30 + 30 * len(score_list)))
        screen.blit(RESTART, (screen_width / 2 - 140, 270))

        score_list.sort(reverse=True)
        for i in range(len(score_list)):
            SCORE_LIST = font.render(f'{i + 1}. : {str(score_list[i])}', False, 0xEEEEEE)
            screen.blit(SCORE_LIST, (screen_width / 2, 300 + 30 * i))

    pygame.display.flip()
    clock.tick(max_frame)

pygame.quit()
