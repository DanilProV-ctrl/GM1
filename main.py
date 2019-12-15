# pip - hranilishe moduley;pip install (--user(ne windows)) -U pygame
# import- obrashenie k moduliu
# pygame.init() - vajnaya commanda,iniciacia,tolko pygame
# as - sokrashenya
# for - medlenny cikl,konechnyi
# while - beskonechnyi,cikl s usloviemt
# // napomny
import webbrowser

from time import sleep
i = 0
while i < 11:
    sleep(0.3)
    print(i)
    i += 1
webbrowser.open('https://github.com/DanilProV-ctrl?tab=repositories')


import pygame as pg

level = [
    '--------------------------',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        -',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '-                        - ',
    '----------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (10, 128, 100)
FPS = 60
clock = pg.time.Clock()
x1, y1 = WIN_HEIGHT // 2, WIN_WIDTH // 2
PLAER_SIZE = 50

pg.init()
pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

player = pg.Surface((PLAER_SIZE, PLAER_SIZE))
player.set_colorkey((0, 0, 0))
# brick.fill(BRICK_COLOR)

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            run = False



    screen.fill(BG_COLOR)


    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "-":
                # screen.blit(brick, (x, y))
                brick = pg.draw.rect(screen, BRICK_COLOR, [x, y, BRICK_WIDTH, BRICK_HEIGHT])
                pg.draw.rect(screen, (0, 0, 0), [x, y, BRICK_WIDTH, BRICK_HEIGHT], 2)
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = 0

    screen.blit(player, (x1, y1))
    pg.display.set_caption(f' FPS: {round(clock.get_fps(), 1)}')
    pg.display.update()
    clock.tick(FPS)
