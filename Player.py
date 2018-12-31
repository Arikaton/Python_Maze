from pygame import *
from pyganim import *
from Amazing_Maze import Walls

PLAYER_WIDTH = 21
PLAYER_HEIGHT = 32
MOVE_SPEED = 8
COLOR = (0, 0, 0)

#Анимации идут в порядке - лево, право, назад, вперед
HERO_SPRITES = {'Vitalya': [[('Sprites/Vitalya/vl1.png'), ('Sprites/Vitalya/vl1.png'), ('Sprites/Vitalya/vl3.png'), ('Sprites/Vitalya/vl4.png')],
                            [('Sprites/Vitalya/vr1.png'), ('Sprites/Vitalya/vr2.png'), ('Sprites/Vitalya/vr3.png'), ('Sprites/Vitalya/vr4.png')],
                            [('Sprites/Vitalya/vb1.png'), ('Sprites/Vitalya/vb2.png'), ('Sprites/Vitalya/vb3.png'), ('Sprites/Vitalya/vb4.png')],
                            [('Sprites/Vitalya/vf1.png'), ('Sprites/Vitalya/vf2.png'), ('Sprites/Vitalya/vf3.png'), ('Sprites/Vitalya/vf4.png')],
                            (13, 32)],
                'default': [[('Sprites/Newton/newtonL1.png'), ('Sprites/Newton/newtonL2.png'), ('Sprites/Newton/newtonL3.png'), ('Sprites/Newton/newtonL4.png')],
                            [('Sprites/Newton/newtonR1.png'), ('Sprites/Newton/newtonR2.png'), ('Sprites/Newton/newtonR3.png'), ('Sprites/Newton/newtonR4.png')],
                            [('Sprites/Newton/newtonU1.png'), ('Sprites/Newton/newtonU2.png'), ('Sprites/Newton/newtonU3.png'), ('Sprites/Newton/newtonU4.png')],
                            [('Sprites/Newton/newtonD1.png'), ('Sprites/Newton/newtonD2.png'), ('Sprites/Newton/newtonD3.png'), ('Sprites/Newton/newtonD4.png')],
                            (21, 32)],
                'Sveta':   [[('Sprites/Sveta/sl1.png'), ('Sprites/Sveta/sl2.png'), ('Sprites/Sveta/sl3.png'), ('Sprites/Sveta/sl4.png')],
                            [('Sprites/Sveta/sr1.png'), ('Sprites/Sveta/sr2.png'), ('Sprites/Sveta/sr3.png'), ('Sprites/Sveta/sr4.png')],
                            [('Sprites/Sveta/sb1.png'), ('Sprites/Sveta/sb2.png'), ('Sprites/Sveta/sb3.png'), ('Sprites/Sveta/sb4.png')],
                            [('Sprites/Sveta/sf1.png'), ('Sprites/Sveta/sf2.png'), ('Sprites/Sveta/sf3.png'), ('Sprites/Sveta/sf4.png')],
                            (21, 32)],
                'marina':  [[('Sprites/Marina/ml1.png'), ('Sprites/Marina/ml2.png'), ('Sprites/Marina/ml3.png'), ('Sprites/Marina/ml4.png')],
                            [('Sprites/Marina/mr1.png'), ('Sprites/Marina/mr2.png'), ('Sprites/Marina/mr3.png'), ('Sprites/Marina/mr4.png')],
                            [('Sprites/Marina/mb1.png'), ('Sprites/Marina/mb2.png'), ('Sprites/Marina/mb3.png'), ('Sprites/Marina/mb4.png')],
                            [('Sprites/Marina/mf1.png'), ('Sprites/Marina/mf2.png'), ('Sprites/Marina/mf3.png'), ('Sprites/Marina/mf4.png')],
                            (18, 32)]
                }

ANIMATION_DELAY = 150


class Hero(sprite.Sprite):
    def __init__(self, x, y, name):
        sprite.Sprite.__init__(self)
        self.name = HERO_SPRITES.get(name)
        self.sprite_size = self.name[4]
        self.start_x = x
        self.start_y = y
        self.xvel = 0
        self.yvel = 0
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(COLOR)
        self.image.set_colorkey(COLOR)
        self.rect = Rect(x, y+2, PLAYER_WIDTH, PLAYER_HEIGHT-2)

        boltanim = []
        for anim in self.name[1]:
            boltanim.append((transform.scale(image.load(anim), self.sprite_size), ANIMATION_DELAY))
        self.anim_right = PygAnimation(boltanim)
        self.anim_right.play()

        boltanim = []
        for anim in self.name[0]:
            boltanim.append((transform.scale(image.load(anim), self.sprite_size), ANIMATION_DELAY))
        self.anim_left = PygAnimation(boltanim)
        self.anim_left.play()

        boltanim = []
        for anim in self.name[2]:
            boltanim.append((transform.scale(image.load(anim), self.sprite_size), ANIMATION_DELAY))
        self.anim_up = PygAnimation(boltanim)
        self.anim_up.play()

        boltanim = []
        for anim in self.name[3]:
            boltanim.append((transform.scale(image.load(anim), self.sprite_size), ANIMATION_DELAY))
        self.anim_down = PygAnimation(boltanim)
        self.anim_down.play()
        self.anim_down.blit(self.image, (0, 0))

    def update(self, left, right, up, down, walls):
        if up:
            self.yvel = -MOVE_SPEED
            self.image.fill(COLOR)
            self.anim_up.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(COLOR)
            self.anim_left.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(COLOR)
            self.anim_right.blit(self.image, (0, 0))

        if down:
            self.yvel = MOVE_SPEED
            self.image.fill(COLOR)
            self.anim_down.blit(self.image, (0, 0))

        if not(left or right):
            self.xvel = 0
        if not(up or down):
            self.yvel = 0

        self.rect.y += self.yvel
        self.collide(0, self.yvel, walls)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, walls)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        if self.rect.top < 0:
            self.rect.top = 0


