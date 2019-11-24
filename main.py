#pip - hranilishe moduley;pip install (--user(ne windows)) -U pygame
#import- obrashenie k moduliu
#pygame.init() - vajnaya commanda,iniciacia,tolko pygame
#as - sokrashenya
#for - medlenny cikl,konechnyi
#while - beskonechnyi,cikl s usloviem

import pygame as pg

WIN_WIDTH,WIN_HEIGHT, = 780,780

pg.init()
pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH,WIN_HEIGHT))

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            run = False


