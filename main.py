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

WIN_WIDTH,WIN_HEIGHT, = 780,780
BG_COLOR = (192, 192, 192)

pg.init()
pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            run = False

    screen.fill(BG_COLOR)
    pg.display.update()


