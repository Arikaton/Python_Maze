from pygame import *
from pyganim import *

PLAYER_WIDTH = 21
PLAYER_HEIGHT = 32
MOVE_SPEED = 6
COLOR = '#000022'

ANIMATION_DELAY = 150
ANIMATION_RIGHT = [('Sprites/Newton/newtonR1.png'), ('Sprites/Newton/newtonR2.png'), ('Sprites/Newton/newtonR3.png'), ('Sprites/Newton/newtonR4.png')]
ANIMATION_LEFT = [('Sprites/Newton/newtonL1.png'), ('Sprites/Newton/newtonL2.png'), ('Sprites/Newton/newtonL3.png'), ('Sprites/Newton/newtonL4.png')]
ANIMATION_UP = [('Sprites/Newton/newtonU1.png'), ('Sprites/Newton/newtonU2.png'), ('Sprites/Newton/newtonU3.png'), ('Sprites/Newton/newtonU4.png')]
ANIMATION_DOWN = [('Sprites/Newton/newtonD1.png'), ('Sprites/Newton/newtonD2.png'), ('Sprites/Newton/newtonD3.png'), ('Sprites/Newton/newtonD4.png')]


class Hero(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.start_x = x
        self.start_y = y
        self.xvel = 0
        self.yvel = 0
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(Color(COLOR))
        self.image.set_colorkey(Color(COLOR))
        self.rect = Rect(x, y+2, PLAYER_WIDTH, PLAYER_HEIGHT-2)

        boltanim = []
        for anim in ANIMATION_RIGHT:
            boltanim.append((anim, ANIMATION_DELAY))
        self.anim_right = PygAnimation(boltanim)
        self.anim_right.play()

        boltanim = []
        for anim in ANIMATION_LEFT:
            boltanim.append((anim, ANIMATION_DELAY))
        self.anim_left = PygAnimation(boltanim)
        self.anim_left.play()

        boltanim = []
        for anim in ANIMATION_UP:
            boltanim.append((anim, ANIMATION_DELAY))
        self.anim_up = PygAnimation(boltanim)
        self.anim_up.play()

        boltanim = []
        for anim in ANIMATION_DOWN:
            boltanim.append((anim, ANIMATION_DELAY))
        self.anim_down = PygAnimation(boltanim)
        self.anim_down.play()
        self.anim_down.blit(self.image, (0, 0))

    def update(self, left, right, up, down, walls):
        if up:
            self.yvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.anim_up.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.anim_left.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            self.anim_right.blit(self.image, (0, 0))

        if down:
            self.yvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
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


