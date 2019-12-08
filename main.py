#pip - hranilishe moduley;pip install (--user(ne windows)) -U pygame
#import- obrashenie k moduliu
#pygame.init() - vajnaya commanda,iniciacia,tolko pygame
#as - sokrashenya
#for - medlenny cikl,konechnyi
#while - beskonechnyi,cikl s usloviem


from time import sleep
i = 0
while i < 10:
    sleep(0.5)
    print(i)
    i += 1
    
  

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

WIN_WIDTH,WIN_HEIGHT, = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (10, 128, 100)

pg.init()
pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

brick = pg.Surface((BRICK_WIDTH, BRICK_HEIGHT))
brick.fill(BRICK_COLOR)

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
                screen.blit(brick, (x, y))
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = 0

    
    pg.display.update()


