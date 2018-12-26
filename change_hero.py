import pygame as pg
from pyganim import *
from Amazing_Maze import main_game

DISPLAY = (900, 600)
WIDTH = 150
HEIGHT = 300

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

NEWTON = [('Sprites/Newton/newtonD1.png'), ('Sprites/Newton/newtonL1.png'), ('Sprites/Newton/newtonU1.png'), ('Sprites/Newton/newtonR1.png')]
TEST_HERO = [('Sprites/hero2_2.png'), ('Sprites/hero2_3.png')]


class Character(pg.sprite.Sprite):
    def __init__(self, x, y, person, delay):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((WIDTH, HEIGHT))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        boltanim = []
        for anim in person:
            boltanim.append((pg.transform.scale(pg.image.load(anim), (WIDTH, HEIGHT)), delay))
        self.hero = PygAnimation(boltanim)
        self.hero.play()
        self.rect = self.image.get_rect(centerx=x, centery=y)

    def update(self):
        self.image.fill(BLACK)
        self.hero.blit(self.image, (0, 0))



def choose():
    pg.init()
    time = pg.time.Clock()
    screen = pg.display.set_mode(DISPLAY)
    background = pg.transform.scale(pg.image.load('Sprites/Background/main_menu.png'), DISPLAY)
    screen.blit(background, (0, 0))
    pg.display.update()

    my_mother = Character(150, 300, NEWTON, 500)
    my_father = Character(DISPLAY[0] / 2, 300, TEST_HERO, 1000)
    my_marina = Character(750, 300, NEWTON, 250)

    characters = pg.sprite.Group()
    characters.add(my_father, my_marina, my_mother)

    font = pg.font.Font(None, 80)
    back = font.render('назад', 1, BLACK)
    back_rect = back.get_rect(centerx=DISPLAY[0]-120, y=DISPLAY[1]-80)
    screen.blit(back, back_rect)

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    main_game.main_menu()
            if event.type == pg.MOUSEMOTION:
                if back_rect.collidepoint(event.pos):
                    back = font.render('назад', 1, RED)
                    screen.blit(back, back_rect)
                if not back_rect.collidepoint(event.pos):
                    back = font.render('назад', 1, BLACK)
                    screen.blit(back, back_rect)
        for e in characters:
            screen.blit(e.image, e.rect)
        characters.update()
        pg.display.update()
        time.tick(60)








