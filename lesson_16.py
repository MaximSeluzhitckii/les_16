import pygame as pg
import pygame.draw

pg.init()
win = pg.display.set_mode((500, 500))

x = 100
y = 50

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    x = x + 1
    if x > 500:
        x = 0

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))
    pygame.display.update()

    pygame.time.delay(10)

