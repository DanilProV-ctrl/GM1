# pip - hranilishe moduley;pip install (--user(ne windows)) -U pygame
# import- obrashenie k moduliu
# pygame.init() - vajnaya commanda,iniciacia,tolko pygame
# as - sokrashenya
# for - medlenny cikl,konechnyi
# while - beskonechnyi,cikl s usloviemt
# // napomny
#
import pygame as pg
import sounddevice as sd
from pygame import gfxdraw
import numpy


from time import sleep
i = 0
while i < 11:
    sleep(0.1)
    print(i)
    i += 1


level = [
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------',
    '-                                                 -                       -          --                                           -                            -',
    '-                                              -                                                                              ----                             -',
    '-                                                 -                                      ----     !                                                            -',
    '-                                               -                               ----                                                                           -',
    '-                                                 -                                                                             ----                           -',
    '-                                        !      -                                          !       -                             ----                          -',
    '-                 !                               -                                                               -            ----       !                    -',
    '-                                               -                                                                  ----                                        -',
    '-                                                                                                                      ----                                    -',
    '-                       !                                                 !!                         ! !                   ----                                -',
    '-                                                                         !!                                                   ----                            -',
    '-                                                                                                      !                           ----                        -',
    '-                                                                                                                                      ----                    -',
    '-                 !                              -                                                     ! ---                                                   -',
    '-                                                  -                                                   !    ---                                                -',
    '-                                        !       -                           !                                 ---                                             -',
    '-                                                  -                         !                   !              - ---                                          -',
    '-                                                -                            !                                -     ---                                       -',
    '-                                                  -                                                                    ---  -                                 -',
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BG_COLOR1 = (102, 129, 192)
BRICK_COLOR_2 = (255, 78, 0)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (10, 128, 100)
BRICK1_COLOR = (0, 0, 0)
BRICK1_WIDTH = BRICK1_HEIGHT = 30
BRICK1_COLOR_1 = (255, 255, 255)
FPS = 60
clock = pg.time.Clock()
RED = (255, 0, 0)
BG_SPEED = 3
PLAER_SIZE = 40
dx = 0
PL_SPEED = 3
penalty = 0.0
BTN_W, BTN_H = 220, 60
GOLD = (255, 215, 0)
BLUE = (0, 0, 190)
RED1 = (200, 50, 50)
WHITE = (255, 255, 255)
pg.init()
# pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


player = pg.Surface((PLAER_SIZE, PLAER_SIZE), pg.SRCALPHA)
player.set_colorkey((0, 0, 0))
# brick.fill(BRICK_COLOR)


def face(color):
    pg.gfxdraw.aacircle(player, PLAER_SIZE // 2, PLAER_SIZE // 2, PLAER_SIZE // 2, color)
    pg.draw.circle(player, color, (PLAER_SIZE // 2, PLAER_SIZE // 2), PLAER_SIZE // 2)
    pg.gfxdraw.aacircle(player, 12, 15, 4, GOLD)
    pg.draw.circle(player, RED1, (12, 15), 4)
    pg.draw.circle(player, (0, 0, 190), (8, 3), 8)
    pg.draw.circle(player, (0, 0, 190), (30, 3), 8)
    pg.draw.circle(player, GOLD, (28, 15), 4)
    pg.draw.arc(player, GOLD, (8, 12, 24, 20), 3.6, 6.0, 3)
    pg.draw.arc(player, (150, 150, 150), (6, 19, 29, 20), 3.6, 6.0, 3)


player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
txt = pg.font.SysFont('Arial', 22, True, True)
text_xy = ((WIN_WIDTH - txt.size(f'Штрафных очков = {penalty}')[0] - 300, 3),)


button = pg.Surface((BTN_W, BTN_H))
button.fill(BLUE)
txte = pg.font.SysFont('Arial', 22, True, False)
text1 = 'Play again?'
text1_pos = txte.size(text1)

result = [WIN_HEIGHT // 2]
yyy = [player_rect.y] * 100


def audio_callback(indata, frames, time, status):
    volume = numpy.linalg.norm(indata) * 20
    yyy.append(volume)
    yyy.pop(0)
    result[0] = sum(yyy) / len(yyy)


color = BLUE
face(color)
run = True
stream = sd.InputStream(callback=audio_callback)
with stream:
    while run:
        for e in pg.event.get():
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                run = False
            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                    mouse_position = pg.mouse.get_pos()
                    if (mouse_position[0] >= 280
                        and mouse_position[0] <= 500
                        and mouse_position[1] >= WIN_HEIGHT // 2
                        and mouse_position[1] <= WIN_HEIGHT // 2 + BTN_H):
                        print(101010)
                        penalty = 0
                        dx = 0
                        player_rect.center = WIN_WIDTH // 2, WIN_HEIGHT // 2
                        result = [WIN_HEIGHT // 2]
                        yyy = [player_rect.y] * 100
                        color = BLUE
                        face(color)

        player_rect.y = WIN_HEIGHT - result[0]
        '''
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            player_rect.x += PL_SPEED
        if keys[pg.K_LEFT]:
            player_rect.x -= PL_SPEED
        if keys[pg.K_UP]:
            player_rect.y -= PL_SPEED
        if keys[pg.K_DOWN]:
            player_rect.y += PL_SPEED
        '''
        if color == RED:
            color = BLUE
            face(color)

        screen.fill(BG_COLOR)
        if dx > -WIN_WIDTH * 4:
            dx -= BG_SPEED
        else:
            if player_rect.x < WIN_WIDTH - PLAER_SIZE:
                player_rect.x += PL_SPEED

        x = dx
        y = 0
        for row in level:
            for col in row:
                if col == "-":
                    # screen.blit(brick, (x, y))
                    brick = pg.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                    pg.draw.rect(screen, BRICK_COLOR_2, [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
                    if brick.colliderect(player_rect):
                        if player_rect.x < WIN_WIDTH - PLAER_SIZE * 2:
                            if color == BLUE:
                                color = RED
                                face(color)
                            penalty += 0.1
                x += BRICK_WIDTH
            y += BRICK_HEIGHT
            x = dx

        if player_rect.x < WIN_WIDTH - PLAER_SIZE:
            screen.blit(player, player_rect)
            pg.display.set_caption(f' FPS: {round(clock.get_fps(), 1)}')
            screen.blit(
                txt.render(f'penalty point = {round(penalty, 1)}', True, RED, None), text_xy
            )
        else:
            screen.blit(button, ((WIN_WIDTH - BTN_W) // 2, WIN_HEIGHT // 2))
            button.blit(
                txt.render(text1, True, WHITE, None),
                ((BTN_W - text1_pos[0]) // 2, (BTN_H - text1_pos[1]) // 2))
            screen.blit(
                txt.render(f'penalty point = {round(penalty, 1)}', True, RED, None),
                ((WIN_WIDTH - txte.size(f'penalty point = {round(penalty, 1)}')[0]) // 2,
                 WIN_HEIGHT // 2 - BTN_H))
        pg.display.update()
        clock.tick(FPS)
