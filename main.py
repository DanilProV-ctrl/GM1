# pip - hranilishe moduley;pip install (--user(ne windows)) -U pygame
# import- obrashenie k moduliu
# pygame.init() - vajnaya commanda,iniciacia,tolko pygame
# as - sokrashenya
# for - medlenny cikl,konechnyi
# while - beskonechnyi,cikl s usloviemt
# // napomny
from time import sleep
i = 0
while i < 11:
    sleep(0.1)
    print(i)
    i += 1



import pygame as pg

level = [
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------',
    '-                                                 -                       -          --                                           -                            -',
    '-                                              -                                                                              ----                             -',
    '-                                                 -                                      ----                                                                  -',
    '-                                               -                               ----                                                                           -',
    '-                                                 -                                                                             ----                           -',
    '-                                               -                                                  -                             ----                          -',
    '-                                                 -                                                               -            ----                            -',
    '-                                               -                                                                  ----                                        -',
    '-                                                                                                                      ----                                    -',
    '-                                                                                                                          ----                                -',
    '-                                                                                                                              ----                            -',
    '-                                                                                                                                  ----                        -',
    '-                                                                                                                                      ----                    -',
    '-                                                -                                                       ---                                                   -',
    '-                                                  -                                                        ---                                                -',
    '-                                                -                                                             ---                                             -',
    '-                                                  -                                                            - ---                                          -',
    '-                                                -                                                             -     ---                                       -',
    '-                                                  -                                                                    ---  -                                 -',
    '----------------------------------------------------------------------------------------------------------------------------------------------------------------'
]

WIN_WIDTH, WIN_HEIGHT = 780, 630
BG_COLOR = (192, 192, 192)
BRICK_COLOR_2 = (255, 78, 0)
BRICK_WIDTH = BRICK_HEIGHT = 30
BRICK_COLOR = (10, 128, 100)
FPS = 60
clock = pg.time.Clock()
RED = (255, 0, 0)
BG_SPEED = 3
PLAER_SIZE = 40
dx = 0
PL_SPEED = 3
penalty = 0.0
BTN_W, BTN_H = 220, 60

pg.init()
# pg.display.set_caption('first game')
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))



player = pg.Surface((PLAER_SIZE, PLAER_SIZE))
player.set_colorkey((0, 0, 0))
# brick.fill(BRICK_COLOR)
pg.draw.circle(player, (0, 0, 190), (PLAER_SIZE // 2, PLAER_SIZE // 2), PLAER_SIZE // 2)
pg.draw.circle(player, (255, 215, 0), (12, 15), 4)
pg.draw.circle(player, (0, 0, 190), (8, 3), 8) 
pg.draw.circle(player, (0, 0, 190), (30, 3), 8) 
pg.draw.circle(player, (255, 215, 0), (28, 15), 4)
pg.draw.arc(player, (255, 215, 0), (8, 12, 24, 20), 3.6, 6.0, 3)
player_rect = player.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

txt = pg.font.SysFont('Sans Serif', 22, True, False)
text_xy = ((WIN_WIDTH - txt.size(f'Штрафных очков = {round(penalty, 1)}')[0] - 300, 30),
)

button = pg.Surface((BTN_W, BTN_H))
txte = pg.font.SysFont('Sans Serif', 22, True, False)
text1 = 'Play again?'
text1_pos = txte.size(text1)


run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        player_rect.x += PL_SPEED
    if keys[pg.K_LEFT]:
        player_rect.x -= PL_SPEED
    if keys[pg.K_UP]:
        player_rect.y -= PL_SPEED
    if keys[pg.K_DOWN]:
        player_rect.y += PL_SPEED

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
                    penalty += 0.1
                    
            x += BRICK_WIDTH
        y += BRICK_HEIGHT
        x = dx

    screen.blit(player, player_rect)
    pg.display.set_caption(f' FPS: {round(clock.get_fps(), 1)}')
    screen.blit(
        txt.render(f'Штрафных очков = {penalty}', True, RED, None), text_xy)
        


    

    pg.display.update()
    clock.tick(FPS)
