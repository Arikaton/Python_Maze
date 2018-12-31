import pygame as pg
from pyganim import *
from random import choice

WALL_WIDTH = 32
WALL_HEIGHT = 32
SIZE = (64, 64)
COLOR = '#333333'

ANIMATION_DELAY = 1000
SNOW_WOOD1 = [('Sprites/Background/snow_wood1.png'), ('Sprites/Background/snow_wood2.png')]
SNOW_MAN_BACK = [('Sprites/Background/snowmanB1.png'), ('Sprites/Background/snowmanB2.png')]
OLEN = [('Sprites/Background/olen1.png'), ('Sprites/Background/olen2.png'), ('Sprites/Background/olen3.png'), ('Sprites/Background/olen4.png')]


class WoodWall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        images = ['Sprites/Background/snow_wood1.png',
                  'Sprites/Background/snowmanB1.png',
                  'Sprites/Background/olen1.png']
        self.image = pg.image.load(choice(images))
        self.rect = self.image.get_rect(x=x, y=y)


class Gift(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Sprites/Background/gift.png')
        self.rect = self.image.get_rect(x=x, y=y)


class AnimWall(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.Surface((32, 32))
        self.image.fill(pg.Color(COLOR))
        self.rect = self.image.get_rect(x=x, y=y)
        boltanim = []
        for anim in SNOW_WOOD1:
            boltanim.append((anim, ANIMATION_DELAY))
        self.anim_wood_1 = PygAnimation(boltanim)
        self.anim_wood_1.play()

        boltanim = []
        for anim in SNOW_MAN_BACK:
            boltanim.append((anim, ANIMATION_DELAY))
        self.snow_man_back = PygAnimation(boltanim)
        self.snow_man_back.play()

        boltanim = []
        for anim in OLEN:
            boltanim.append((anim, ANIMATION_DELAY))
        self.olen = PygAnimation(boltanim)
        self.olen.play()

        self.all_anim = [self.snow_man_back, self.anim_wood_1, self.olen]
        self.current_anim = choice(self.all_anim)
        self.current_anim.blit(self.image, (0, 0))

    def update(self):
        self.image.fill(pg.Color(COLOR))
        self.current_anim.blit(self.image, (0, 0))


class Road(pg.sprite.Sprite):
    def __init__(self, x, y, lvl):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((WALL_WIDTH, WALL_HEIGHT))
        self.lvl = lvl

        i, j = y//WALL_HEIGHT, x//WALL_WIDTH
        up, down, left, right = False, False, False, False
        if i != 0 and self.lvl[i-1][j] == ' ':
            up = True
        if i != (len(self.lvl) - 1) and self.lvl[i+1][j] == ' ':
            down = True
        if j != (len(self.lvl[0]) - 1) and self.lvl[i][j+1] == ' ':
            right = True
        if j != 0 and self.lvl[i][j-1] == ' ':
            left = True

        if left and right and up and down:
            self.image = pg.image.load('Sprites/road_center.png')
        elif left and right and up:
            self.image = pg.image.load('Sprites/road3.png')
        elif left and right and down:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road3.png'), 180)
        elif down and up and left:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road3.png'), 90)
        elif down and up and right:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road3.png'), -90)
        elif right and down:
            self.image = pg.image.load('Sprites/road_turn.png')
        elif left and down:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_turn.png'), -90)
        elif up and left:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_turn.png'), 180)
        elif up and right:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_turn.png'), 90)
        elif up and down:
            self.image = pg.image.load('Sprites/road.png')
        elif left and right:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road.png'), 90)
        elif right:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_end.png'), 90)
        elif left:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_end.png'), -90)
        elif down:
            self.image = pg.image.load('Sprites/road_end.png')
        elif up:
            self.image = pg.transform.rotate(pg.image.load('Sprites/road_end.png'), 180)

        self.rect = pg.Rect(x, y, WALL_WIDTH, WALL_HEIGHT)

